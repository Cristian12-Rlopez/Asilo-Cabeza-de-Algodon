from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Interno

# Vista pública para usuarios generales (Landing Page)
def inicio(request):
    return render(request, 'inicio.html')

# Vista del portal de usuarios
def panel_usuario(request):
    return render(request, 'panel_usuario.html')

# Nueva vista del dashboard protegida con login
@login_required
def dashboard_view(request):
    return render(request, 'core/dashboard.html', {
        'usuario': request.user
    })

@login_required
def expedientes_view(request):
    # Consultamos todos los expedientes ordenados por fecha de creación
    internos = Interno.objects.all().order_by('-fecha_creacion')
    return render(request, 'core/expedientes.html', {
        'usuario': request.user,
        'internos': internos
    })