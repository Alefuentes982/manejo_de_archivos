n = int(input('\nIntroduce un número entero entre 1 y 10: '))
file_name = 'datos.txt-' + str(n) + '.txt'
f = open(file_name, 'w')
for i in range(1, 11):
    f.write(str(n) + ' x ' + str(i) + ' = ' + str(n * i) + '\n')
f.close()

print("\nSe ha creado satisfactoriamente el archivo datos.txt-", n, "correspondiente a la tabla del \n", n) 










