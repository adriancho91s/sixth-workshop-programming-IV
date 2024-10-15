import tkinter as tk
from tkinter import messagebox


class Authenticator:
    def authenticate(self, username: str, password: str) -> bool:
        return username == "admin" and password == "password"


class LoginInterface:
    def __init__(self, authenticator: Authenticator):
        self.authenticator = authenticator
        self.window = tk.Tk()
        self.window.title("Login Interface")
        self.window.geometry("300x200")
        self.create_widgets()

    def create_widgets(self):
        self.label_username = tk.Label(self.window, text="Username")
        self.label_username.pack(pady=5)
        self.entry_username = tk.Entry(self.window)
        self.entry_username.pack(pady=5)

        self.label_password = tk.Label(self.window, text="Password")
        self.label_password.pack(pady=5)
        self.entry_password = tk.Entry(self.window, show="*")
        self.entry_password.pack(pady=5)

        self.login_button = tk.Button(self.window, text="Login", command=self.login)
        self.login_button.pack(pady=20)

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        if self.authenticator.authenticate(username, password):
            messagebox.showinfo("Login Success", "Welcome!")
        else:
            messagebox.showerror("Login Failed", "Invalid credentials")

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    authenticator = Authenticator()
    login_interface = LoginInterface(authenticator)
    login_interface.run()
