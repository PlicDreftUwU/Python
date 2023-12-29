from genericpath import exists
import requests
import argparse
from os import path #Nos ayuda a trabajar con rutas dentro del SO para verificar
#existencia de archivos
parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', help='Indica el archivo a subir')
parser = parser.parse_args()
def main():
    if parser.file:
        if path.exists(parser.file):
            archive = open(parser.file,'rb')#Abrimos en formato binario
            headers = {'User' : 'Google'}
            petition = requests.post(
                url='https://curso--python-0-prueba-pentest1.000webhostapp.com/index.php',files={'uploaded_file':archive},headers=headers)
            if parser.file in petition.text:
                print('Upload')
            else:
                print('No upload')
        else:
            print('File dont exists')
    else:
        print('File not found')

if __name__ == '__main__':
    main()