import hashlib
import hashlib
from tkinter import Tk, Label, Entry, Button

def save_credentials():
    username = username_entry.get()
    password = password_entry.get()


    hashed_password = hashlib.sha256(password.encode()).hexdigest()


    with open('credentials.txt', 'a') as file:
        file.write(f'Username: {username}\n')
        file.write(f'Hashed Password: {hashed_password}\n')
        file.write('------------------------\n')


    username_entry.delete(0, 'end')
    password_entry.delete(0, 'end')



window = Tk()
window.title("Сохранение учетных данных")
window.geometry('300x150')


username_label = Label(window, text="Логин:")
username_label.pack()
username_entry = Entry(window)
username_entry.pack()

password_label = Label(window, text="Пароль:")
password_label.pack()
password_entry = Entry(window, show='*')
password_entry.pack()

save_button = Button(window, text="Сохранить", command=save_credentials)
save_button.pack()


window.mainloop()
