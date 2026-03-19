from django.shortcuts import render
from .Vuelos_BFS import buscar_solucion_BFS

def index(request):
    resultado = None

    conexiones = {
        'Jiloyork': {'Celaya', 'CDMX', 'Queretaro'},
        'Sonora': {'Zacatecas', 'Sinaloa'},
        'Guanajuato': {'Aguascalientes'},
        'Oaxaca': {'Queretaro', 'Tamaulipas'},
        'Sinaloa': {'Celaya', 'Sonora', 'Jiloyork'},
        'Queretaro': {'Monterrey'},
        'Celaya': {'Jiloyork', 'Sinaloa'},
        'Zacatecas': {'Sonora', 'Monterrey', 'Queretaro'},
        'Monterrey': {'Zacatecas', 'Sinaloa'},
        'Tamaulipas': {'Queretaro', 'CDMX', 'Aguascalientes', 'Guanajuato'},
        'CDMX': {'Tamaulipas', 'Zacatecas', 'Sinaloa', 'Jiloyork', 'Oaxaca'},
        'Aguascalientes': {'Guanajuato', 'Tamaulipas', 'Oaxaca', 'Zacatecas'},
    }

    estados = sorted(conexiones.keys())

    if request.method == 'POST':
        estado_inicial = request.POST.get('inicio')
        estado_final = request.POST.get('fin')

        nodo_solucion = buscar_solucion_BFS(conexiones, estado_inicial, estado_final)

        if nodo_solucion:
            camino = []
            nodo = nodo_solucion
            while nodo.get_padre() != None:
                camino.append(nodo.get_datos())
                nodo = nodo.get_padre()
            camino.append(estado_inicial)
            camino.reverse()
            resultado = camino
        else:
            resultado = ["No hay ruta disponible"]

    return render(request, 'index.html', {
        'resultado': resultado,
        'estados': estados
    })