names=['Anika','Monika','Maria','Sofia']
names_2d=[
    [22,5,7,'Enjal'],
    ['Muna','Bharat','Stellas']
        ]

# for names_1 in names_2d:
#     for name in names_1:
#         print(name)
# print(names_2d[1])
names_5d=[
    [
        [
            [
              [
                22,5,7,'Enjal'  
              ],
              [
                 'Muna','Bharat','Stellas' 
              ]  
            ]
        ]
    ]
]
# print(names_5d[0][0][0][0][-1])
for names_4 in names_5d:
    for names_3 in names_4:
        for names_2 in names_3:
            for names_1 in names_2:
                for names in names_1:
                    print(names)