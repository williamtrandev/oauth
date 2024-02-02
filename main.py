from fastapi import FastAPI
from starlette.responses import RedirectResponse
import httpx
app = FastAPI()

github_client_id = '80b69168319514d98ddd'
github_client_secret = '4accd92d566eca759e28162add4ff30f72726037'
google_client_id = '834328556535-mpjbtdqc05akd0e9oemvhsnfgsh6o0lt.apps.googleusercontent.com'
google_client_secret = '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'


@app.get("/")
async def root():
    return {"Github login": "/api/auth/github-login", "Google login": "/api/auth/google-login"}

# API login with github
@app.get("/api/auth/github-login")
async def github_login():
    return RedirectResponse(f'https:github.com/login/oauth/authorize?client_id={github_client_id}',
                            status_code=302)

# API get access token
@app.get("/api/auth/callback/github")
async def github_access_token(code: str):
    # Get access token
    async with httpx.AsyncClient() as client:
        access_token_url = 'https://github.com/login/oauth/access_token'
        params = {
            'client_id': github_client_id,
            'client_secret': github_client_secret,
            'code': code
        }
        headers = {'Accept': 'application/json'}
        response = await client.post(url=access_token_url,
                                     params=params,
                                     headers=headers)
        access_token = response.json()['access_token']
    return {"access_token": access_token}

# API callback to show information of github account
@app.get("/api/auth/github/info")
async def github_information(access_token: str):
    # Get information of github account
    async with httpx.AsyncClient() as client:
        user_info_url = 'https://api.github.com/user'
        headers = {'Authorization': f'Bearer {access_token}'}
        response = await client.get(user_info_url, headers=headers)
        response.raise_for_status()

    return response.json()

# API login with Google
@app.get("/api/auth/google-login")
async def google_login():
    scope = "openid profile email"
    redirect_uri = 'http://localhost:8000/api/auth/callback/google'
    return RedirectResponse("https://accounts.google.com/o/oauth2/auth?"
        f"client_id={google_client_id}&"
        "response_type=code&"
        f"redirect_uri={redirect_uri}&"
        f"scope={scope}",
        status_code=302)




# API get access token
@app.get("/api/auth/callback/google")
async def google_access_token(code: str):
    token_url = "https://oauth2.googleapis.com/token"
    google_redirect_uri = "http://localhost:8000/api/auth/callback/google"
    data = {
        "code": code,
        "client_id": google_client_id,
        "client_secret": google_client_secret,
        "redirect_uri": google_redirect_uri,
        "grant_type": "authorization_code",
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(token_url, data=data)
        # response.raise_for_status()
        # return response.json()

    return response.json()["access_token"]

@app.get("/api/auth/google/info")
async def get_google_user_info(access_token: str):
    user_info_url = "https://www.googleapis.com/oauth2/v3/userinfo"

    async with httpx.AsyncClient() as client:
        headers = {"Authorization": f"Bearer {access_token}"}
        response = await client.get(user_info_url, headers=headers)
        response.raise_for_status()
        return response.json()
