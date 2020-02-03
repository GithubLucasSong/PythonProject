# 2，定义一个用户类, 用户名和密码是这个类的属性, 实例化两个用户, 分别有不同的用户名和密码
# 登陆成功之后才创建用户对象
# 设计一个方法
# 修改密码

class User():
    user_dic = {'alex': '123', 'blex': '456'}

    def __init__(self,unm,pwd):
        self.unm = unm
        self.pwd = pwd


    def set_pwd(self,newpwd):
        self.pwd = newpwd
        User.user_dic[self.unm] = self.pwd
        print('修改密码成功')

    @classmethod
    def login(cls):
        unm = input('请输入账号：')
        pwd = input('请输入密码：')

        if pwd == cls.user_dic.get(unm):
            return User(unm,pwd)

        else:
            print('登陆失败')
            return None


login_user = User.login()
if login_user:
    print(f'用户{login_user.unm}登陆成功!')
    data = input('输入1修改密码')
    if int(data) == 1:
        new_pwd = input('请输入新密码')
        login_user.set_pwd(new_pwd)



