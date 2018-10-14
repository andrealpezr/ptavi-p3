#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 20:54:26 2018

@author: andrea
"""
import sys
import json
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from urllib.request import urlretrieve
from smallsmilhandler import SmallSMILHandler


class KaraokeLocal(SmallSMILHandler):

    def __init__(self, fichero):  # Inicializo y construyo la lista
        parser = make_parser()  # Creo parser
        cHandler = SmallSMILHandler()  # Creo manejador
        parser.setContentHandler(cHandler)  # Le paso el parser al manejador
        parser.parse(open(fichero))
        self.lista = cHandler.get_tags()

if __name__ == "__main__":

    if len(sys.argv) != 2:
        sys.exit("Usage: python3 karaoke.py file.smil")
    try:
        obj = KaraokeLocal(sys.argv[1])
    except (ValueError, IndexError, FileNotFoundError):
        sys.exit("Usage: python3 karaoke.py file.smil")
    print(obj)
