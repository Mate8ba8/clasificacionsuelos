import matplotlib.pyplot as plt
import matplotlib.path as mpath
import numpy as np
from matplotlib.ticker import FuncFormatter
from matplotlib.ticker import MultipleLocator
from matplotlib.ticker import Formatter
from prettytable import PrettyTable

from .Granulometria import *
from .CartaPlasticidad import *
from .Valoresdeentrada import*

tam_200 = pasa_tamiz200
tam_4 = pasa_tamiz4

Limite_plastico = Limite_liquido - Indice_plasticidad
Cu=4
Cc=2

if tam_200 < 50: 
      print("mundo de los suelos gruesos")
      if tam_4 < 50:
        print("El suelo es una grava")
        if tam_200 > 12:
          if Limite_plastico > 7:
            print("GRAVA ARCILLOSA (GC)")
          else:
            if Indice_plasticidad < 4:
              print("GRAVA LIMOSA (GM)")
            else: 
              print("GRAVA LIMOSA- GRAVA ARCILLOSA (GM-GC)")
        else: 
          if tam_200 > 5: 
            if Limite_plastico < 0.73*(Limite_liquido-20):
              if (Cu > 4) and (1<Cc<3):
                print("GW-GM")
              else:
                print("GP-GM")
            else:
              if (Cu > 4) and (1<Cc<3):
                print("GW-GC")
              else:
                print("GP-GC")
          else:
            if (Cu>4) and (1<Cc<3):
              print("GW")
            else:
              print("GP")
            
      
      else: 
        print("El suelo es arena")
        if tam_200 > 12:
          if Limite_plastico > 7:
            print("SC")
          else:
            if Indice_plasticidad < 4:
              print("SM")
            else:
              print("SM-SC")
        else:
          if tam_200 > 5:
            if Limite_plastico < 0.73*(Limite_liquido-20):
              if (Cu > 6) and (1<Cc<3):
                print("SW-SM")
              else:
                print("SP-SM")
            else:
              if (Cu > 6) and (1<Cc<3):
                print("SW-SC")
              else:
                print("SP-SC")
          else: 
            if (Cu>6) and (1<Cc<3):
              print("SW")
            else:
              print("SP")

else: clasificacion()


