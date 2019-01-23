from django.shortcuts import render
from preinscripcion.forms import nuevoInscritoForm
# Create your views here.

def index(request):
    form = nuevoInscritoForm()
    if request.method == 'POST':
        form = nuevoInscritoForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
        else:
            print('Error en formulario')

    return render(request,'preinscripcion/index.html',{'form':form})
