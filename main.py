from tkinter import *
from playsound import playsound
from morse_code_dict import MORSE_CODE_DICTIONARY
import time
import threading

stop = False

def encrypt():
    encrypted_message = ''
    message = message_entry.get("1.0", 'end-1c')

    for char in message.lower():
        if char == ' ':
            encrypted_message += ' / '
        elif char == '\n':
            encrypted_message += '\n'
        else:
            encrypted_message += MORSE_CODE_DICTIONARY[char] + ' '

    cipher_entry.delete("1.0", 'end')
    cipher_entry.insert(INSERT, encrypted_message)


def decrypt():
    decrypted_message = ''
    encrypted_message = cipher_entry.get("1.0", 'end-1c')
    char_codes = encrypted_message.split(' ')
    inv_morse_code_dict = {code: char for char, code in MORSE_CODE_DICTIONARY.items()}

    for char_code in char_codes:

        if '\n' in char_code:
            decrypted_message += '\n'
            char_code = char_code.strip('\n')   
        if char_code == '/':
            decrypted_message += ' '
        else:
            decrypted_message += inv_morse_code_dict[char_code]

    message_entry.delete("1.0", 'end')
    message_entry.insert(INSERT, decrypted_message)


def play_thread():
    global stop
    stop = False
    t1 = threading.Thread(target=play)
    t1.start()


def play():
    encrypted_message = cipher_entry.get("1.0", 'end-1c')

    for char in encrypted_message:
        if stop:
            break
        elif char == '.':
            playsound('dot.mp3')
        elif char == '-':
            playsound('dash.mp3')
        elif char == ' ':
            time.sleep(0.3)
        elif char == '/':
            time.sleep(0.6)


def play_stop():
    global stop
    stop = True


root = Tk()
root.title('English to Morse Code Translator')
root.config(padx=40, pady=40)
root.resizable(False, False)

multiple_btn_frame = Frame(root, borderwidth=0, relief="groove")
multiple_btn_frame.grid(column=2, row=5, sticky='NE')

message_label = Label(text="English", font=("Inter", 20))
message_label.grid(sticky='W', column=0, row=0, pady=(0, 16))

message_entry = Text(width=50, height=10, font=("Inter", 16))
message_entry.grid(column=0, row=1, columnspan=3)

msg_translate_button = Button(text="Translate", bg='blue', command=encrypt)
msg_translate_button.grid(column=2, row=2, sticky='NE')

cipher_label = Label(text="Morse", font=("Inter", 20))
cipher_label.grid(sticky='W', column=0, row=3, pady=(48, 16))

cipher_entry = Text(width=50, height=10, font=("Inter", 16))
cipher_entry.grid(column=0, row=4, columnspan=3)

cph_translate_button = Button(multiple_btn_frame, text="Translate", command=decrypt)
cph_translate_button.grid(column=2, row=0, sticky='NE')

cph_play_button = Button(multiple_btn_frame, text='Play', command=play_thread)
cph_play_button.grid(column=1, row=0)

cph_stop_button = Button(multiple_btn_frame, text='Stop', command=play_stop)
cph_stop_button.grid(column=0, row=0)

root.mainloop()
