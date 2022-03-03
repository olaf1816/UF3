import literales as l
import csv

def opcion():
    option = int(input(l.DESPLEGABLE))
    match option:
        case 1:
            return "tecno1"
        case 2:
            return "tecno2"
        case 3:
            return "tecno3"
        case _:
            print (l.ERROR)
            exit()
def cabecera():
    with open('files/base.csv', 'a') as csvfile:
        writeCSV = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writeCSV.writerow(['Identificador','Nombre', 'Apellido', 'Edad', 'Tecnologia'])

def introducir(identificador, nombre, apellido, edad, tecnologia):
    with open('files/base.csv', 'a+') as csvfile:
        writeCSV = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writeCSV.writerow([identificador,nombre, apellido, edad, tecnologia])