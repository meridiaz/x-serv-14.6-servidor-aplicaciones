#!/usr/bin/python3

"""
webApp class
 Root for hierarchy of classes implementing web applications

 Copyright Jesus M. Gonzalez-Barahona and Gregorio Robles (2009-2015)
 jgb @ gsyc.es
 TSAI, SAT and SARO subjects (Universidad Rey Juan Carlos)
 October 2009 - February 2015
"""

import socket
import webapp

class holaApp(webapp.webApp):
    def process(self, parsedRequest):
        return ("200 OK", "<html><body><h1>Hola mundo</h1></body></html>")

if __name__ == "__main__":
    testWebApp_hola = holaApp("localhost", 1234)
