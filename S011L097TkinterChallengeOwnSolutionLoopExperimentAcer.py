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

# # test 1 - experimenting with loops
# for i in range(1, 4):
#     print(i)
#
# for i in range(1, 4):
#     for j in range(1, 4):
#         print(i, j)

# test 2 - generating buttons with loop in tkinter (with grid)
# only in the first row
# try:
#     import tkinter
# except ImportError:  # Python 2
#     import Tkinter as tkinter
#
# mainWindow = tkinter.Tk()
#
# mainWindow.title("tkinter button loop test 2")
# mainWindow.geometry('250x250+8+400')
# mainWindow['padx'] = 10
#
# for i in range (1, 6):
#     button = tkinter.Button(mainWindow, text ="{}".format(i))
#     button.grid(row=0, column=i, sticky='new')
#
# mainWindow.mainloop()

# test 3 - generating buttons with loop in tkinter (with grid)
# only in the first row
# try:
#     import tkinter
# except ImportError:  # Python 2
#     import Tkinter as tkinter
#
# mainWindow = tkinter.Tk()
#
# mainWindow.title("tkinter button loop test 3")
# mainWindow.geometry('250x250+8+400')
# mainWindow['padx'] = 10
#
# for i in range (1, 6):
#     for j in range(1,6):
#         button = tkinter.Button(mainWindow, text ="{}, {}".format(i, j))
#         button.grid(row=i, column=j, sticky='new')
#
# mainWindow.mainloop()

# test 4 - generating buttons with loop in tkinter (with grid)
# only in the first row
# try:
#     import tkinter
# except ImportError:  # Python 2
#     import Tkinter as tkinter
#
# mainWindow = tkinter.Tk()
#
# mainWindow.title("tkinter button loop test 4")
# mainWindow.geometry('250x250+8+400')
# mainWindow['padx'] = 10
#
# buttonList = ["A", "B", "C", "D", "E"]
#
# for i in range (0, 5):
#     button = tkinter.Button(mainWindow, text ="{}".format(buttonList[i]))
#     button.grid(row=0, column=i, sticky='new')
#
# mainWindow.mainloop()

# test 5 - generating buttons with loop in tkinter (with grid)
# multiple rows and columns
# try:
#     import tkinter
# except ImportError:  # Python 2
#     import Tkinter as tkinter
#
# mainWindow = tkinter.Tk()
#
# mainWindow.title("tkinter button loop test 5")
# mainWindow.geometry('250x250+8+400')
# mainWindow['padx'] = 10
#
# buttonRowList = ["R1", "R2", "R3", "R4", "R5"]
# buttonColumnList = ["C1", "C2", "C3", "C4", "C5"]
#
#
# for i in range(0, 5):
#     for j in range(0, 5):
#         button = tkinter.Button(mainWindow, text ="{}, {}".format(buttonRowList[i], buttonColumnList[j]))
#         button.grid(row=i, column=j, sticky='new')
#
# mainWindow.mainloop()

# test 6 - generating buttons with loop in tkinter (with grid)
# multiple rows and columns with range for more flexibility
# try:
#     import tkinter
# except ImportError:  # Python 2
#     import Tkinter as tkinter
#
# mainWindow = tkinter.Tk()
#
# mainWindow.title("tkinter button loop test 6")
# mainWindow.geometry('250x250+8+400')
# mainWindow['padx'] = 10
#
# buttonRowList = ["R1", "R2", "R3", "R4", "R5", "R6"]
# buttonColumnList = ["C1", "C2", "C3"]
#
# print(len(buttonRowList))
# print(len(buttonColumnList))
#
# for i in range(0, len(buttonRowList)):
#     for j in range(0, len(buttonColumnList)):
#         button = tkinter.Button(mainWindow, text ="{}, {}".format(buttonRowList[i], buttonColumnList[j]))
#         button.grid(row=i, column=j, sticky='new')
#
# mainWindow.mainloop()


# test 7 - generating buttons with loop in tkinter (with grid)
# multiple rows and columns with range for more flexibility
# try:
#     import tkinter
# except ImportError:  # Python 2
#     import Tkinter as tkinter
#
# mainWindow = tkinter.Tk()
#
# mainWindow.title("tkinter button loop test 7")
# mainWindow.geometry('250x250+8+400')
# mainWindow['padx'] = 10
#
# buttonRowList = ["R1", "R2", "R3", "R4", "R5", "R6"]
# buttonColumnList = ["C1", "C2", "C3"]
#
# print(len(buttonRowList))
# print(len(buttonColumnList))
#
# for i in range(0, len(buttonRowList)):
#     for j in range(0, len(buttonColumnList)):
#         button = tkinter.Button(mainWindow, text ="{}, {}".format(buttonRowList[i], buttonColumnList[j]))
#         button.grid(row=i, column=j, sticky='new')
#
# mainWindow.mainloop()

# test 8 - generating buttons with loop in tkinter (with grid)
# multiple rows and columns with range for more flexibility
#
# buttonList = [["C", "CE"], ["7", "8", "9", "+"], ["4", "5", "6", "-"], ["1", "2", "3", "*"], ["0", "=", "/"]]
# for i in buttonList:
#     print(i)
# print("")
#
# for i in buttonList:
#     print(*i)

# test 9 - generating buttons with loop in tkinter (with grid)
# multiple rows and columns with range for more flexibility
#
# buttonList = [["C", "CE"], ["7", "8", "9", "+"], ["4", "5", "6", "-"], ["1", "2", "3", "*"], ["0", "=", "/"]]
# for list in buttonList:
#     for number in list:
#         print(number)

# test 10 - generating buttons with loop in tkinter (with grid)
# figuring out how to retrieve xth sub list, and from it another element
#
# buttonList = [["C", "CE"], ["7", "8", "9", "+"], ["4", "5", "6", "-"], ["1", "2", "3", "*"], ["0", "=", "/"]]
# for i in buttonList:
#     print(i)
#
# print("")
# print(buttonList[1])
# print(buttonList[3])
# print(buttonList[3][2])

# test 11 - generating buttons with loop in tkinter (with grid)
# figuring out how to retrieve xth sub list, and from it another element
#
# buttonList = [["C", "CE"], ["7", "8", "9", "+"], ["4", "5", "6", "-"], ["1", "2", "3", "*"], ["0", "=", "/"]]
# for i in buttonList:
#     print(i)
#
# print("")
# print(buttonList[1])
# print(buttonList[3])
# print(buttonList[3][2])
#
# print("")
# print("")
# print(len(buttonList))
# print("")
# for i in range(0, len(buttonList)):
#     print(i)
#
# for i in range(0, len(buttonList)):
#     for j in range (0, len(buttonList[i])):
#         print(i, j)


# test 12 - generating buttons with loop in tkinter (with grid)
# generating buttons based on a list - the "pythonic" solution 1.0
# try:
#     import tkinter
# except ImportError:  # Python 2
#     import Tkinter as tkinter
#
# mainWindow = tkinter.Tk()
#
# mainWindow.title("tkinter button loop test 12")
# mainWindow.geometry('250x250+8+400')
# mainWindow['padx'] = 10
#
# buttonList = [["C", "CE"],
#               ["7", "8", "9", "+"],
#               ["4", "5", "6", "-"],
#               ["1", "2", "3", "*"],
#               ["0", "=", "/"]]
#
# for i in range(0, len(buttonList)):
#     for j in range (0, len(buttonList[i])):
#         print(i, j)
#
# for i in range(0, len(buttonList)):
#     for j in range(0, len(buttonList[i])):
#         button = tkinter.Button(mainWindow, text ="{}".format(buttonList[i][j]))
#         button.grid(row=i+1, column=j+1, sticky='new')
#
# mainWindow.mainloop()

# test 13 - generating buttons with loop in tkinter (with grid)
# generating buttons based on a list - the "pythonic" solution 2.0
#
#
# try:
#     import tkinter
# except ImportError:  # Python 2
#     import Tkinter as tkinter
#
# mainWindow = tkinter.Tk()
#
# mainWindow.title("tkinter button loop test 13")
# mainWindow.geometry('250x250+8+400')
# mainWindow['padx'] = 10
#
# buttonList = [["C", "CE"],
#               ["7", "8", "9", "+"],
#               ["4", "5", "6", "-"],
#               ["1", "2", "3", "*"],
#               ["0", "=", "/"]]
#
# columnSpanList = [[1, 1],
#               [1, 1, 1, 1],
#               [1, 1, 1, 1],
#               [1, 1, 1, 1],
#               [1, 1, 1]]
#
# for i in range(0, len(buttonList)):
#     for j in range(0, len(buttonList[i])):
#         button = tkinter.Button(mainWindow, text="{}".format(buttonList[i][j]))
#         button.grid(row=i+1, column=j+1, sticky='new', columnspan=columnSpanList[i][j])
#
# mainWindow.mainloop()

# test 14 - generating buttons with loop in tkinter (with grid)
# generating buttons based on a list - the "pythonic" solution 3.0
# generating automatic column span adaption
#

try:
    import tkinter
except ImportError:  # Python 2
    import Tkinter as tkinter

mainWindow = tkinter.Tk()

mainWindow.title("tkinter button loop test 14")
mainWindow.geometry('250x250+8+400')
mainWindow['padx'] = 10

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
        button = tkinter.Button(mainWindow, text="{}".format(buttonList[i][j]))
        button.grid(row=i+1, column=j+columnSpanList[i][j-1], sticky='new', columnspan=columnSpanList[i][j])  # adapting

mainWindow.mainloop()

# Further steps
# double space for certain butten
# min width and height