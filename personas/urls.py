from django.urls import path

from .views import DashboardView, PersonaDetailView, PersonaListView, PersonaCreateView, PersonaDeleteView, InactivoPersonaListView, PersonaUpdateView, NotaCreateView

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('persona/crear/', PersonaCreateView.as_view(), name='persona_crear'),
    path('persona/listar/', PersonaListView.as_view(), name='persona_listar'),  
    path('persona/listar/inactivos/', InactivoPersonaListView.as_view(), name='persona_listar_inactivos'),
    path('persona/<int:pk>/', PersonaDetailView.as_view(), name='persona_detalle'),
    path('persona/<int:pk>/eliminar/', PersonaDeleteView.as_view(), name='persona_eliminar'),
    path('persona/<int:pk>/editar/', PersonaUpdateView.as_view(), name='persona_update'),
    path('persona/<int:pk>/nota/nueva/', NotaCreateView.as_view(), name='nota_create'),
] 
