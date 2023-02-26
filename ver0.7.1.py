import tkinter,datetime,sys,time,webbrowser
import tkinter as tk
import tkinter.messagebox # import this to fix messagebox error
try_num = 5
year = datetime.date.today().strftime('%Y') #获取当前年份
user_name = ''
def sign_up(*args):
    tkinter.messagebox.showinfo('温馨提示','该功能还在创建中，请耐心等待')

def login(*args):
    global try_num,user_name
    user_name = login_username.get()
    user_password = login_password.get()
    if user_name == 'admin' and user_password == '123456':#用户名的正确用户名和密码
        tkinter.messagebox.showinfo('Info','登录成功')
        admin_login.destroy()
        admin_main()
    else:
        if user_name:
            try_num -= 1
            if try_num > 0:        
                LoginInfo = tkinter.Label(admin_login,fg='red',text='用户名或密码错误,您还剩'+str(try_num)+'次机会').place(x=200,y=250)
                tkinter.messagebox.showerror('Error','用户名或密码错误,您还剩:'+str(try_num)+'次机会!')
            elif try_num <= 0:
                tkinter.messagebox.showwarning('Warn','您已多次输入错误的用户名或密码, 程序自动关闭!')
                admin_login.destroy()
                sys.exit()
        else:
            tkinter.messagebox.showwarning('Warn','请输入您的用户名')

def admin_main():
    global user_name
    admin = tkinter.Tk()
    if user_name != 'zengz':
        admin.title(user_name+" '© zengz'")
    else:
        admin.title(user_name)
    def copyright_admin():
        def close_about():
            about.destroy()
        
        def updates():
            about.destroy()
            tkinter.messagebox.showinfo('提示','请自行检查是否有新版本')
            updates_webside = 'https://github.com/wavedalansan/Public.git'
            webbrowser.open(updates_webside)
        about = tk.Tk()
        about.geometry('250x160')
        about.title('About')
        about.resizable(0,0)
        ver = tk.Label(about,text='版本:0.7.1 (快照版)',fg='red').place(x=5,y=0)
        copyrights = tk.Label(about,text='© 2023 zengz',fg='blue').place(x=5,y=20)
        creattime = tk.Label(about,text='发布时间:2023/2/18 20:38',fg='green').place(x=5,y=40)
        if user_name == 'zengz':
            _admin_ = tk.Label(about,text='当前用户权限:拥有所有权',fg='purple').place(x=5,y=60)
        elif user_name == 'admin':
            _admin_ = tk.Label(about,text='当前用户权限:修改权',fg='purple').place(x=5,y=60)
        else:
            _admin_ = tk.Label(about,text='当前用户权限:使用权',fg='purple').place(x=5,y=60)
        sureBut = tk.Button(about,text='确认信息',command=close_about,fg='orange',width=10).place(x=40,y=80)
        update = tk.Button(about,text='检查更新',fg='grey',width=10,command=updates).place(x=130,y=80)

    admin.geometry('1000x700')
    about_button = tk.Button(admin,text='版本信息',fg='blue',command=copyright_admin).place(x=0,y=0)
    admin.mainloop()

admin_login = tkinter.Tk()
admin_login.title('请先登录')
admin_login.geometry('600x500')
copyrights_login = tkinter.Label(admin_login,fg='blue',text='© '+str(year)+' zengz').place(x=500,y=470)#版权
version_login = tkinter.Label(admin_login,fg='blue',text='Ver:0.7.1').place(x=520,y=450)

login_welcome = tkinter.Label(admin_login,fg='orange',text='欢迎,请先登录',font=('微软雅黑',20)).place(x=205,y=10)#欢迎
login_username = tkinter.Label(admin_login,fg='purple',text='用户名:').place(x=120,y=60)#输入提示-用户名
login_username = tkinter.Entry(admin_login,width=40)#输入框
login_username.bind('<Return>', sign_up)
login_username.place(x=170,y=60)#位置设置

login_password = tkinter.Label(admin_login,fg='purple',text='密码:').place(x=120,y=120)#输入提示-密码
login_password = tkinter.Entry(admin_login,width=40,show='•')#隐藏密码
login_password.bind('<Return>', login)#回车登录
login_password.place(x=170,y=120)#位置设置

login_button = tkinter.Button(admin_login,fg='green',text='登录',width=10,height=2,command=login).place(x=200,y=160)#登录按钮
sign_up_button = tkinter.Button(admin_login,fg='green',text='注册',width=10,height=2,command=sign_up).place(x=300,y=160)

admin_login.resizable(0,0)#锁定窗口大小
admin_login.mainloop()#显示窗口
