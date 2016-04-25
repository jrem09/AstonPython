import tkinter
import tkinter.messagebox as tm

users = {'user1': '123456', 'user2': '654321', 'user3': 'password'}

window = tkinter.Tk()
window.title("Authentification C&C")
w = 300
h = 110
ws = window.winfo_screenwidth()
hs = window.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
window.geometry('%dx%d+%d+%d' % (w, h, x, y))

label_login = tkinter.Label(window, text="Login :")
input_login = tkinter.Entry(window)

label_password = tkinter.Label(window, text="Password :")
input_password = tkinter.Entry(window, show="*")


def _login_btn_clickked():
    username = input_login.get()
    password = input_password.get()
    if username in users.keys():
        if password == users.get(username):
            tm.showinfo("Login info", "Welcome " + username)
    else:
        tm.showerror("Login error", "Login Failed !")


login_btn = tkinter.Button(window, text="Login", command=_login_btn_clickked)
label_login.pack()
input_login.pack()
label_password.pack()
input_password.pack()
login_btn.pack()
window.mainloop()












