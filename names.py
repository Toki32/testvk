import openpyxl

def zakup(name):
    names=[]
    wb = openpyxl.load_workbook(filename = r'C:\Users\sasmir28\Desktop\kukla\Книга1.xlsx')
    sheet = wb['Лист1']
    a = ''
    #vals = [v[0].value for v in sheet.range('B2:B4')]
    if name == 'ruk':
        a = sheet['A2':'A947']

        for kek in a:
            for lol in kek:
                try:
                    splitName = lol.value.split(' ')[0] + ' ' + lol.value.split(' ')[1]

                    # print(names.append(lol.value))
                    names.append(splitName)
                except AttributeError:
                    pass
    elif name == 'zak':
        a = sheet['B2':'B316']
        for kek in a:
            for lol in kek:
                names.append(lol.value)

    return(names)



