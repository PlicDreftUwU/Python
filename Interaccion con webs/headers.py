import requests #peticiones a web
import argparse

parser = argparse.ArgumentParser(description='Detector de cabeceras') #Detectar argumentos por medio de la consola
parser.add_argument('-t','--target',help='Objetivo') #Se almacena la informacion del objetivo
parser = parser.parse_args()

def main():
    if parser.target:
        try:
            url = requests.get(url=parser.target)
            contenido = dict(url.headers)
            for n in contenido:
                print(n + ' : ' + contenido[n])
        except:
            print('No conexion')
    else:
        print('No target')

if __name__ == '__main__':
    main()