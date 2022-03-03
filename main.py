import functions as f
import literales as l

def main():
    rep = 1
    f.cabecera()

    while rep == 1:
        nombre = input(l.NOM)
        apellido = input(l.APELLIDO)
        edad = int(input(l.EDAD))
        tecnologia = f.opcion()
        identificador = (nombre[:2].upper() + "-" + apellido[-2:].upper() + "-" + str(edad))

        f.introducir(identificador, nombre, apellido, edad, tecnologia)

        rep = int(input(l.REPETIR))

if __name__ == '__main__':
    main()