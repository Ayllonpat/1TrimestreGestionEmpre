import csv
from datetime import datetime
from math import sqrt
from collections import namedtuple

#función lee_avistamientos

Avistamiento = namedtuple ('Avistamientos',
                           'fechahora, ciudad, estado, forma, duracion, comentarios, latitud, longitud')

def lee_avistamientos(fichero):
    res=[]

    with open (fichero, encoding= 'utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        for x in lector:
            fecha_hora = x[0]
            fechahora = datetime.strptime(fecha_hora, '%m/%d/%Y %H:%M')
            ciudad = x[1]
            estado = x[2]
            forma = x[3]
            duracion = int(x[4])
            comentarios = x[5]
            latitud = float(x[6])
            longitud = float(x[7])
            tupla = Avistamiento(fecha_hora, ciudad, estado, forma, duracion, comentarios, latitud, longitud)
            res.append(tupla)
    return res

#función duracion_total

def duracion_total(registros):

    res=[]

    return res

    
# función comentario_mas_largo



# función avistamientos_fechas



# función hora_mas_avistamientos