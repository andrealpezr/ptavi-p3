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
        # Recorro diccionario añadiendo un string y '\n'
        stri = ""
        for diccs in self.lista:
            stri += str(diccs['name'])
            for atributo in diccs:
                if diccs[atributo] != "" and atributo != 'name':
                    stri += '\t' + atributo + '="' + diccs[atributo] + '"'
            stri += '\n'
        return(stri)   

    def to_json(self, fich, fich_json=None):
        # Creamos un fichero en formato json
        fich_json = json.dumps(self.lista)
        if fich_json is None:
            fich_json = fich.split('.')[0] + '.json'
        json.dump(self.lista, open(fich_json, 'w'))

    def do_local(self):
        # Recorre la lista y descarga recursos remotos
        for diccs in self.lista:
            for atributos in diccs:
                    if diccs[atributos][0:7] == "http://":
                        atrib_Antes = diccs[atributos]
                        atrib_Nuevo = diccs[atributos].split('/')[-1]
                        urlretrieve(atrib_Antes, atrib_Nuevo)
                        diccs[atributos] = atrib_Nuevo


if __name__ == "__main__":

    if len(sys.argv) != 2:
        sys.exit("Usage: python3 karaoke.py file.smil")
    try:
        obj = KaraokeLocal(sys.argv[1])
    except (ValueError, IndexError, FileNotFoundError):
        sys.exit("Usage: python3 karaoke.py file.smil")

    print(obj) 
    obj.to_json(sys.argv[1])
    obj.do_local()
    obj.to_json(sys.argv[1], 'local.json')
    print(obj)

