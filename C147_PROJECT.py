# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 05:31:47 2024

@author: Eshaan Gurjar
"""

from tkinter import *
root = Tk()
root.geometry("960x540")
root.configure(background='bisque')



username = Entry(root)
letters_display = Label(root, text="No. of letters = ")
encrypted_word = Label(root, text="Encrypted username is = ")
letters = []
words = []

def encryptor():
     
    username_value = username.get()
    new_letter = ""
    
    for every_letter in username_value:
        letters.append(every_letter)
        words.append(new_letter)
        letter_ord = ord(every_letter)
        new_letter_a = letter_ord - 1
        new_letter = chr(new_letter_a)
        
    letters_display["text"] += str(len(letters))
    word = "" . join(words)
    encrypted_word["text"] += str(word)
    
    
username.place(relx = 0.5, rely = 0.5, anchor = CENTER)

btn = Button(root, text = "Show encrypted word", command = encryptor)
btn.place(relx = 0.5, rely = 0.6, anchor = CENTER)

letters_display.place(relx = 0.5, rely = 0.7, anchor = CENTER)
encrypted_word.place(relx = 0.5, rely = 0.8, anchor = CENTER)

root.mainloop()
    
        
