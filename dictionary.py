names={
    'name':'Luther',
    'age':25,
    1:100,
    'name':'Maria',
    'name2':'Maria'
}
# print(names)
# print(names['age'])
# print(names.values())
names.update({'age':30})
names[1]=200
names['experience']=10
print(names)
names.pop('age')
print(names)
# print('The keys are:')
# for key in names.keys():
#     print(key)
# print('The values are:')
# for value in names.values():
#     print(value)