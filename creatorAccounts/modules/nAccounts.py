# -*- coding: utf-8 -*-
"""
Created on Sun May 23 14:56:31 2021

@author: c-est
"""

def nAccounts():
   while True:
       users = input('Ingrese el numero de cuentas que desea crear:')
       try:
           users = int(users)
           return users
       except ValueError:
           print ("La entrada es incorrecta: escribe un numero entero")
