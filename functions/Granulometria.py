from .Valoresdeentrada import *
import matplotlib.pyplot as plt
import matplotlib.path as mpath
import numpy as np
from matplotlib.ticker import FuncFormatter
from matplotlib.ticker import MultipleLocator
from matplotlib.ticker import Formatter
from prettytable import PrettyTable

from .Valoresdeentrada import *


abertura_tamiz4 = 4.75
abertura_tamiz10 = 2
abertura_tamiz20 = 0.850
abertura_tamiz40= 0.425
abertura_tamiz100 = 0.150
abertura_tamiz200 = 0.075

sum_retenido = Cantidad_retenida_Tara + Cantidad_retenida_tam4 + Cantidad_retenida_tam10 + Cantidad_retenida_tam20 + Cantidad_retenida_tam40 + Cantidad_retenida_tam100 + Cantidad_retenida_tam200


por_ret_4 = (100 * Cantidad_retenida_tam4)/ sum_retenido
por_ret_10 = (100 * Cantidad_retenida_tam10)/ sum_retenido
por_ret_20 = (100 * Cantidad_retenida_tam20)/ sum_retenido
por_ret_40 = (100 * Cantidad_retenida_tam40)/ sum_retenido
por_ret_100 = (100 * Cantidad_retenida_tam100)/ sum_retenido
por_ret_200 = (100 * Cantidad_retenida_tam200)/ sum_retenido
por_ret_Tara = (100 * Cantidad_retenida_Tara)/ sum_retenido

sum_por_ret = por_ret_4+por_ret_10+por_ret_20+por_ret_40+por_ret_100+por_ret_200+por_ret_Tara

por_acu_ret_4 = por_ret_4 
por_acu_ret_10 = por_acu_ret_4 + por_ret_10 
por_acu_ret_20 = por_acu_ret_10 + por_ret_20 
por_acu_ret_40 = por_acu_ret_20 + por_ret_40 
por_acu_ret_100 = por_acu_ret_40 + por_ret_100
por_acu_ret_200 = por_acu_ret_100 + por_ret_200
por_acu_ret_Tara = por_acu_ret_200 + por_ret_Tara

pasa_tamiz4 = 100 - por_acu_ret_4
pasa_tamiz10 = 100 - por_acu_ret_10
pasa_tamiz20 = 100 - por_acu_ret_20
pasa_tamiz40 = 100 - por_acu_ret_40
pasa_tamiz100 = 100 - por_acu_ret_100
pasa_tamiz200 = 100 - por_acu_ret_200


      # Crear la tabla
tabla = PrettyTable()
tabla.field_names = ["Tamiz", "Abertura","Retenido (g)","retenido(%)","% Ret.Acum","% Pasa"]
tabla.add_row(["4",abertura_tamiz4,Cantidad_retenida_tam4,por_ret_4,por_acu_ret_4, pasa_tamiz4])
tabla.add_row(["10",abertura_tamiz10,Cantidad_retenida_tam10,por_ret_10,por_acu_ret_10, pasa_tamiz10])
tabla.add_row(["20",abertura_tamiz20,Cantidad_retenida_tam20,por_ret_20,por_acu_ret_20, pasa_tamiz20])
tabla.add_row(["40",abertura_tamiz40,Cantidad_retenida_tam40,por_ret_40,por_acu_ret_40, pasa_tamiz40])
tabla.add_row(["100",abertura_tamiz100,Cantidad_retenida_tam100,por_ret_100,por_acu_ret_100, pasa_tamiz100])
tabla.add_row(["200",abertura_tamiz200,Cantidad_retenida_tam200,por_ret_200,por_acu_ret_200, pasa_tamiz200])
tabla.add_row(["Tara","---",Cantidad_retenida_Tara,por_ret_Tara,por_acu_ret_Tara, "---"])
tabla.add_row(["Total","---",sum_retenido,sum_por_ret, "---","---",])

      # Imprimir la tabla
print(tabla)

      #Se grafica la línea de la granulometría
plt.figure(figsize=(14, 4)) 

    # Se pone en escala logaritmica el eje de las x 
plt.xscale('log')

# En cada eje se marca un limite 
plt.xlim([0.01, 10])
plt.ylim([0, 100])
# Aqui se aplica una función para poder cambiar el formato de representación del eje x 
def log_tick_formatter(val, pos=None):
    return "{:.4f}".format(val)

plt.gca().xaxis.set_major_formatter(FuncFormatter(log_tick_formatter))
 
 # Esta función se utiliza para invertir el eje x
plt.gca().invert_xaxis()

plt.gca().yaxis.set_major_locator(MultipleLocator(10))



# Aqui se utiliza una función para poder poner el sufijo % al eje y 
class PercentageFormatter(Formatter):
    def __call__(self, x, pos=None):
        return f"{x:.0f}%"

plt.gca().yaxis.set_major_formatter(PercentageFormatter())



# grilla log en eje x
plt.grid(True, which="minor", linestyle='-')
 
# grilla normal en eje y
plt.grid(True, linestyle='-')

# Añadir nombre a los ejes
plt.xlabel('Abertura del Tamiz (mm)')
plt.ylabel('Porcentaje que Pasa')

# Agregar un título al gráfico
plt.title('CURVA GRANULOMETRICA DE LOS AGREGADOS')

L_No4 = ([4.75,4.75])
L_No10 = ([2,2]) 
L_No20 = ([0.850,0.850]) 
L_No40 = ([0.425,0.425]) 
L_No100 = ([0.150,0.150])
L_No200 = ([0.075,0.075])  
L_rango = ([0,100])

plt.plot(L_No4, L_rango, color='grey', lw='2', ls='--')
plt.plot(L_No10, L_rango, color='grey', lw='2', ls='--')
plt.plot(L_No20, L_rango, color='grey', lw='2', ls='--') 
plt.plot(L_No40, L_rango, color='grey', lw='2', ls='--')
plt.plot(L_No100, L_rango, color='grey', lw='2', ls='--')
plt.plot(L_No200, L_rango, color='grey', lw='2', ls='--')

# Coordenadas a graficar
x = [abertura_tamiz4, abertura_tamiz10, abertura_tamiz20, abertura_tamiz40, abertura_tamiz100, abertura_tamiz200]
y = [pasa_tamiz4, pasa_tamiz10, pasa_tamiz20, pasa_tamiz40, pasa_tamiz100, pasa_tamiz200]
 
plt.plot(x, y, '-o')
plt.show()


