# OAuth với Github và Google

Callback URL sẽ được gọi khi Github ủy quyền (Google cũng tương tự):

![image](https://github.com/williamtrandev/oauth/assets/102520170/2cafb478-8b49-475d-83c3-6469a9932a7f)

Các constants sau có được sau khi đã đăng ký app trên Google và Github:

![image](https://github.com/williamtrandev/oauth/assets/102520170/23d107fb-6eb7-4cf8-8deb-77bb4564c480)

## Github OAuth
![image](https://github.com/williamtrandev/oauth/assets/102520170/50196e7a-e959-4c1f-ba8a-f1f9a8f40612)

Khi truy cập vào ``` localhost:8000/api/auth/github-login ```, người dùng sẽ được chuyển đến trang đăng nhập vào Github, sau khi chọn tài khoản và nhập mật khẩu.
Khi tài khoản xác thực thành công, callback URL sẽ được gọi lại (là URL đã được đăng ký trên Github App) kèm theo mã xác thực gọi là code.
Dùng code này để lấy access token, sau khi có access token, lấy thông tin của tài khoản bằng access token đó

![image](https://github.com/williamtrandev/oauth/assets/102520170/446639dd-000f-4bd8-9c60-4aa3ded61017)

## Google OAuth
Tương tự với Github sẽ gồm có 3 route: Login, lấy access token và cuối cùng là thông tin của người dùng

![image](https://github.com/williamtrandev/oauth/assets/102520170/c4ef361c-c3be-4109-8c90-a5ab9b285949)

![image](https://github.com/williamtrandev/oauth/assets/102520170/21336f6a-0637-406b-96e6-e32bc7983305)

![image](https://github.com/williamtrandev/oauth/assets/102520170/99f97db0-3425-4913-9f96-a96353148044)

# Demo chạy:

## Github

Truy cập vào ``` localhost:8000/api/auth/github-login ``` và đăng nhập

![image](https://github.com/williamtrandev/oauth/assets/102520170/c5f381e4-81bd-4221-bb2f-8978aeb89a0a)

Login thành công nhận access token

![image](https://github.com/williamtrandev/oauth/assets/102520170/8d2b57db-b3ca-4f5f-acc8-b418081bdfdd)

Truy cập vào ``` localhost:8000/api/auth/google/info?access_token={...} ``` với access token vừa nhận

![image](https://github.com/williamtrandev/oauth/assets/102520170/42f8f531-9916-4e5e-8af7-d37243f8d976)


## Google

Các bước tương tự với Github

![image](https://github.com/williamtrandev/oauth/assets/102520170/12e1dad9-b5db-4779-9f16-a49a7c7cc8c0)

![image](https://github.com/williamtrandev/oauth/assets/102520170/e380a9b6-a3bb-4ffa-b971-fe192046839b)

![image](https://github.com/williamtrandev/oauth/assets/102520170/6b48ff15-33ac-422f-80ba-c39129882c04)


