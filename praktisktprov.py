#Author: Lucas Curry
#Date: 2024-09-25

userinput = input('Ange gångertabeller du vill se, mellanslag mellan varje siffra: ')

if (userinput == ''):
    print('Inget värde anget, stänger ner programmet.')
else:
    number_list = userinput.split()
    
    for i in range(len(number_list)):
        temp_var = int(number_list[i])
        print(f'{temp_var*1}\n{temp_var*2}\n{temp_var*3}\n{temp_var*4}\n{temp_var*5}\n{temp_var*6}\n{temp_var*7}\n{temp_var*8}\n{temp_var*9}\n{temp_var*10}\n')
    print('Beräkningar klara, stänger ner programmet')