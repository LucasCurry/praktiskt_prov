#Author: Lucas Curry
#Date: 2024-09-25

userinput = input('Ange gångertabeller du vill se, mellanslag mellan varje siffra: ')

if (userinput == ''):
    print('Inget värde anget, stänger ner programmet.')
else:
    number_list = userinput.split()

    for i in range(len(number_list)):
        temp_var = int(number_list[i])
        for i in range(1,11):
            print(f'{temp_var} * {i} = {temp_var*i}')
        print("")
    print('Beräkningar klara, stänger ner programmet')