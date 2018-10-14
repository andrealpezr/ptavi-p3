#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 20:54:26 2018

@author: andrea
"""

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):
    def __init__(self):  # Método para inicializar atributos
        self.lista = []  # Lista vacía que se rellenará
        # Creo un diccionario
        self.dicc = {'root-layout': ['width', 'height', 'background-color'],
                     'region': ['id', 'top', 'bottom', 'left', 'right'],
                     'img': ['src', 'region', 'begin', 'dur'],
                     'audio': ['src', 'begin', 'dur'],
                     'textstream': ['src', 'region']}

    def startElement(self, name, attrs):  # Método cuando se abre etiqueta
        dict = {}
        if name in self.dicc:
            for atrib in self.dicc[name]:  # Itera todos los elementos
                dict[atrib] = attrs.get(atrib, "")
            self.lista.append([name, dict])  # Añade al final de la lista

    def get_tags(self):
        return self.lista  # Devuelve una lista con las etiquetas encontradas


if __name__ == "__main__":
    parser = make_parser()  # Creo parser
    cHandler = SmallSMILHandler()  # Creo manejador
    parser.setContentHandler(cHandler)  # Le paso el parser al manejador
    parser.parse(open('karaoke.smil'))
    print(cHandler.get_tags())
