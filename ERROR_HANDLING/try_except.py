
# try:
#     f = open('testfile.txt')
#     # var= bad_var
# except FileNotFoundError as e:
#     print(e)
# except Exception as e:
#     print(e)

# else:
#     print(f.read())
#     f.close()
# finally:
#     print('Execute Finally...')
try:
    number = float(input('Enter a number:'))
    result = 10/number

except ValueError as e:
    print(e)

except ZeroDivisionError as e:
    print(e)

else:
    print('The number is:', result)

finally:
    print('Finally the code is finished.')