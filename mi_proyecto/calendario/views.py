from django.shortcuts import render
import datetime
# Create your views here.
def calendario(request, fecha):
    # Separamos la cadena "31-2-2020" por los guiones
    partes = fecha.split('-')
    
    mi_dia = partes[0]
    num_mes = int(partes[1])
    mi_ano = partes[2]

    # Mapeo del número de mes a texto
    meses = {
        1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril",
        5: "Mayo", 6: "Junio", 7: "Julio", 8: "Agosto",
        9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"
    }
    
    mi_mes = meses.get(num_mes, partes[1])

    # Validamos si la fecha es real en el calendario
    try:
        datetime.date(int(mi_ano), num_mes, int(mi_dia))
        mensaje = " La fecha es válida"
    except ValueError:
        mensaje = "atención: La fecha introducida no existe"

    return render(request, 'calendario/fecha.html', {
        'dia': mi_dia, 
        'mes': mi_mes, 
        'ano': mi_ano, 
        'mensaje': mensaje
    })