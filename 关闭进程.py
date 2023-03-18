#copyright zengz
#inclouding utf-8
#ver 1.0
import os
import tkinter
import tkinter.messagebox
root = tkinter.Tk()
root.title('关闭程序')
root.geometry('300x300')

def close_jy(*args):
    close_progress = close_pid.get()
    if not close_progress:
        tkinter.messagebox.showerror('Error','进程名不能为空!')
    else:
        os.system("taskkill /F /IM "+str(close_progress)+" /T")
        tkinter.messagebox.showinfo('Information','进程已尝试关闭!')

def admin_mode():
    os.startfile("admin.py")#admin.py放于该文件的相同文件夹下

text_tip = tkinter.Label(root,text='请输入进程名:',fg='blue').place(x=0,y=0)
text = tkinter.Label(root,text='按下按钮以关闭进程').place(x=90,y=60)
text_warn = tkinter.Label(root,text='输入进程名称且必须要带上后缀名!',fg='red').place(x=50,y=200)
close_button = tkinter.Button(root,text='关闭进程',command=close_jy).place(x=120,y=120)
administrator_button = tkinter.Button(root,text='管理员模式',fg='green',command=admin_mode).place(x=220,y=260)
close_pid = tkinter.Entry(root, width=50)
close_pid.place(x=80, y=0, width=220, height=20)

close_pid.bind('<Return>', close_jy)

root.resizable(0,0)
root.mainloop()
