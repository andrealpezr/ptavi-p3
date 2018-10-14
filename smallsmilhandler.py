#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 20:54:26 2018

@author: andrea
"""
import sys
from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):
    def __init__(self):  # método para inicializar atributos
        self.lista = []  # lista vacía que se rellenará
        self.dicc = {'root-layout': ['width', 'height', 'background-color'],
            'region': ['id', 'top', 'bottom', 'left', 'right'], 'img': ['src', 
            'region', 'begin', 'dur'], 'audio': ['src', 'begin', 'dur'],
            'textstream': ['src', 'region']}  # creo un diccionario

    def startElement(self, name, attrs):
        dict = {}
        if name in self.dicc:
            dict['name'] = name
            for atributo in self.dicc[name]:
                dict[atributo] = attrs.get(atributo, "")
            self.lista.append(dict)

    def get_tags(self):
        return(self.lista)


if __name__ == "__main__":
    parser = make_parser()  # Creo parser
    cHandler = SmallSMILHandler()  # Creo manejador
    parser.setContentHandler(cHandler)  # Le paso el parser al manejador
    parser.parse(open('karaoke.smil'))
    print(cHandler.get_tags())
