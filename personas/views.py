from xml.parsers.expat import model

from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views import View
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
# from .forms import SecureLoginForm, User
from django.views.generic import CreateView, DeleteView, ListView, TemplateView, DetailView, UpdateView
from django.contrib import messages

from personas.models import Persona
from .forms import PersonaForm, NotaForm 
from .models import Nota
# from .forms import SecureSignupForm


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'personas/dashboard.html'


class PersonaCreateView(LoginRequiredMixin, CreateView): 
    model = Persona
    form_class = PersonaForm
    template_name = 'personas/persona_form.html'
    success_url = reverse_lazy('persona_crear')

    def form_valid(self, form):
        form.instance.foto = self.request.FILES.get('foto')
        messages.success(self.request, "Persona creada correctamente.")
        return super().form_valid(form)


class PersonaDetailView(LoginRequiredMixin, DetailView):
    model = Persona
    template_name = 'personas/persona_detail.html'
    context_object_name = 'persona'

    # def get(self, request, pk):
    #     persona = Persona.objects.get(pk=pk)
    #     return render(request, 'personas/persona_detail.html', {'persona': persona})

class PersonaDeleteView(LoginRequiredMixin, DeleteView):
    model = Persona
    template_name = 'personas/persona_confirm_delete.html'
    success_url = reverse_lazy('persona_listar')

    # def delete(self, request, *args, **kwargs):
    #     messages.success(self.request, "Persona eliminada correctamente.")
    #     return super().delete(request, *args, **kwargs)

class PersonaListView(LoginRequiredMixin, ListView):
    permission_required = 'app.change_persona'
    model = Persona
    template_name = 'personas/persona_list.html'
    context_object_name = 'personas'
    success_url = reverse_lazy('persona_listar')
    
    def get_queryset(self):
        return Persona.objects.filter(activo=True).order_by('apellido', 'nombre')
    
class InactivoPersonaListView(LoginRequiredMixin, ListView):
    model = Persona
    template_name = 'personas/persona_list.html'
    context_object_name = 'personas'
    success_url = reverse_lazy('persona_listar')
    
    def get_queryset(self):
        return Persona.objects.filter(activo=False).order_by('apellido', 'nombre')
    

class PersonaUpdateView(LoginRequiredMixin, UpdateView):
    model = Persona
    form_class = PersonaForm
    template_name = 'personas/persona_form.html'
    success_url = reverse_lazy('persona_listar')

    def form_valid(self, form):
        messages.success(self.request, "Persona Actualizada correctamente.")
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titul'] = 'Editar Persona'
        context['boton'] = 'Actualizar'
        return context
    

class NotaCreateView(LoginRequiredMixin, CreateView):
    model = Nota
    form_class = NotaForm
    template_name = 'notas/nota_form.html'

    def form_valid(self, form):
        id = self.kwargs['pk']
        form.instance.persona = Persona.objects.get(pk=id)
        form.instance.autor = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('persona_detalle', kwargs={'pk': self.kwargs['pk']})


def mi_error_404(request, exception):
    return render(request, '404.html', status=404)