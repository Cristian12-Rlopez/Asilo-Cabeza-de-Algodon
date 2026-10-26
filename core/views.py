from django.shortcuts import render
from django.contrib.auth.decorators import login_required

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