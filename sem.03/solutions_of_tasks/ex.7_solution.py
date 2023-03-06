from tkinter import *

gui = Tk(className='Python Examples - Window Color')
gui.geometry("400x200")

background_color = ''
#####################
# !!Попълнете своя скрипт в това поле!!
str_16_elements = '0123456789ABCDEF'

red = int(input())
green = int(input())
blue = int(input())

temp = int(red / 16)
result_red = str_16_elements[red % 16]
red = temp

temp = int(red / 16)
result_red += str_16_elements[red % 16]

temp = int(green / 16)
result_green = str_16_elements[green % 16]
green = temp

temp = int(green / 16)
result_green += str_16_elements[green % 16]

temp = int(blue / 16)
result_blue = str_16_elements[blue % 16]
blue = temp

temp = int(blue / 16)
result_blue += str_16_elements[blue % 16]

background_color = "#" + result_red[::-1] + result_green[::-1] + result_blue[::-1]
#####################
gui.configure(bg=background_color)

gui.mainloop()
