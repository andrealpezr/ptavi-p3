#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 20:54:26 2018

@author: andrea
"""
import sys
import json
from xml.sax import make_parser
from urllib.request import urlretrieve
from smallsmilhandler import SmallSMILHandler


class KaraokeLocal(SmallSMILHandler):

    def __init__(self, fichero):
        # Inicializo y construyo la lista
        parser = make_parser()  # Creo parser
        cHandler = SmallSMILHandler()  # Creo manejador
        parser.setContentHandler(cHandler)  # Le paso el parser al manejador
        parser.parse(open(fichero))
        self.lista = cHandler.get_tags()

    def __str__(self):
        """ Método para crear la lista de etiquetas """
        linea = " "
        for elem in self.lista:
            linea = linea + elem[0]
            atributos = elem[1].items()
            for nombre, valor in atributos:
                if valor != '':
                    linea = linea + '\t' + nombre + '=' + '"' + valor + '"'
            print(linea)

    def to_json(self, fich, fich_json=None):
        # Creamos un fichero en formato json
        fich_json = json.dumps(self.lista)
        if fich_json is None:
            fich_json = fich.split('.')[0] + '.json'
            json.dump(self.lista, open(fich_json, 'w'))

    def do_local(self):
        # Recorre la lista y descarga recursos remotos
        for diccs in self.lista:
            atrib = diccs[1]
            for atributos, posi in atrib.items():
                    if atributos == "src" and posi[0:7] == "http://":
                        atrib_Nuevo = posi.split('/')[-1]
                        urlretrieve(posi, atrib_Nuevo)
                        print("Descargando %s ..." % posi)

if __name__ == "__main__":

    if len(sys.argv) != 2:
        sys.exit("Usage: python3 karaoke.py file.smil")
    try:
        obj = open(sys.argv[1])
    except (ValueError, IndexError, FileNotFoundError):
        sys.exit("Usage: python3 karaoke.py file.smil")

    fichero = sys.argv[1]
    fich_json = sys.argv[1].replace(".smil", ".json")
    obj = KaraokeLocal(fichero)
    obj.__init__(fichero)
    obj.__str__()
    obj.to_json(fich_json)
    obj.do_local()
    obj.to_json(fich_json, 'local.json')
    obj.__str__()
