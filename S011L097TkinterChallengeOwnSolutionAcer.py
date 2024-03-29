#
# TIM BUCHALKA'S COMPLETE PYTHON MASTERCLASS Created by Tim Buchalka, Jean-Paul Roberts,
# Tim Buchalka's Learn Programming Academy.
# This is a collection of my codes, generated by myself for learning Python
# This challenge is about understanding tkinter and making GUI in Python.
# Here is a link to the course: https://www.udemy.com/python-the-complete-python-developer-course/
# Authors of the challenge (definition of what to code)
#
# Tim Buchalka
# https://www.udemy.com/user/timbuchalka/
# https://github.com/tim-buchalka
#
# Jean-Paul Roberts
# https://www.udemy.com/user/jeanpaulroberts/
#
# START OF CHALLENGE (TIM BUCHALKA, JEAN-PAUL ROBERTS)
#
# Write a GUI program to create a simple calculator
# layout that looks like the screenshot.
#
# Try to be as Pythonic as possible - it's ok if you
# end up writing repeated Button and Grid statements,
# but consider using lists and a for loop.
#
# There is no need to store the buttons in variables.
#
# As an optional extra, refer to the documentation to
# work out how to use minsize() to prevent your window
# from being shrunk so that the widgets vanish from view.
#
# Hint: You may want to use the widgets .winfo_height() and
# winfo_width() methods, in which case you should know that
# they will not return the correct results unless the window
# has been forced to draw the widgets by calling its .update()
# method first.
#
# If you are using Windows you will probably find that the
# width is already constrained and can't be resized too small.
# The height will still need to be constrained, though.
#
# END OF THE CHALLENGE (TIM BUCHALKA, JEAN-PAUL ROBERTS)
#
# Python 3.7.0
# IntelliJ IDEA 2019.1.3 (Community Edition)
# Windows 10, 64 bit
#
# START OF MY OWN CODE
#

try:
    import tkinter
except ImportError:  # Python 2
    import Tkinter as tkinter

mainWindow = tkinter.Tk()

mainWindow.title("Calculator")
mainWindow.geometry('240x220+8+400')
mainWindow['padx'] = 5

keyboardFrame = tkinter.LabelFrame(mainWindow)
keyboardFrame.grid(row=1, column =0, sticky='nsew')
keyboardFrame.config(border=2, relief='sunken')

buttonList = [["C", "CE"],
              ["7", "8", "9", "+"],
              ["4", "5", "6", "-"],
              ["1", "2", "3", "*"],
              ["0", "=", "/"]]

columnSpanList = [[1, 1],
                  [1, 1, 1, 1],
                  [1, 1, 1, 1],
                  [1, 1, 1, 1],
                  [1, 2, 1]]

for i in range(0, len(buttonList)):
    for j in range(0, len(buttonList[i])):
        button = tkinter.Button(keyboardFrame, text="{}".format(buttonList[i][j]))
        button.grid(row=i+1, column=j+columnSpanList[i][j-1], sticky='new', columnspan=columnSpanList[i][j])  # adapting
        button.config(padx=5)

display = tkinter.Entry(mainWindow)
display.grid(row=0, column=0, sticky='w')

mainWindow.mainloop()

# to do
# constrain minimum height and width
# create list and loop for button generation













