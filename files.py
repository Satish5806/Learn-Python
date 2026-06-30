import os

# if os.path.exists('D:\LEARN PYTHON\classes.py'):
#     file=open('D:\LEARN PYTHON\class.py', "a")
#     file.write(' #This is written with files.py')
#     file.close()

if os.path.exists('D:\LEARN PYTHON\classes.py'):
    file=open('D:\LEARN PYTHON\classes.py', "r")
    print(file.read())

else:
    open('D:\LEARN PYTHON\classes.py','x')
    file=open('D:\LEARN PYTHON\classes.py', "a")
    file.write(' #This is the new file created.')
    file=open('D:\LEARN PYTHON\classes.py', "r")
    print(file.read())

