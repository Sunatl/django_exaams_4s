from django.shortcuts import render
from django.template import loader
from django.views.generic import CreateView,DeleteView,DetailView,UpdateView,ListView
from .models import *
from django.http import HttpResponse
from django.urls import reverse_lazy

def base(request):
    template = loader.get_template("base.html")
    return HttpResponse(template.render())



# Movie

class MovieListView(ListView):
    model = Movie
    template_name = 'list_m.html'
    
class MovieDetailView(DetailView):
    model = Movie
    template_name = 'detail_m.html'
    
class MovieCreateView(CreateView):
    model = Movie
    template_name = 'create_m.html'
    fields = ['name','image','description','vedio','cinema']
    success_url = reverse_lazy('list_m') 
    
    
class MovieUpdateView(UpdateView):
    model = Movie
    template_name = 'update_m.html'
    fields = ['name','image','description','vedio','cinema']
    success_url = reverse_lazy('list_m') 
    
    
class MovieDeleteView(DeleteView):
    model = Movie
    template_name = 'delete_m.html'
    success_url = reverse_lazy('list_m') 



# Order
class OrderListView(ListView):
    model = Order
    template_name = 'list_o.html'
    
class OrderDetailView(DetailView):
    model = Order
    template_name = 'detail_o.html'
    
class OrderCreateView(CreateView):
    model = Order
    template_name = 'create_o.html'
    fields = ['name','user','amount']
    success_url = reverse_lazy('list_o') 
    
    
class OrderUpdateView(UpdateView):
    model = Order
    template_name = 'update_u.html'
    fields = ['name','user','amount']
    success_url = reverse_lazy('list_o') 
    
    
class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'delete_o.html'
    success_url = reverse_lazy('list_o') 
    
    
    
# User
class UserListView(ListView):
    model = User
    template_name = 'list_u.html'
    
class UserDetailView(DetailView):
    model = User
    template_name = 'detail_u.html'
    
class UserCreateView(CreateView):
    model = User
    template_name = 'create_u.html'
    fields = ['fullname','username','email','phone_number']
    success_url = reverse_lazy('list_u') 
    
    
class UserUpdateView(UpdateView):
    model = User
    template_name = 'update_u.html'
    fields = ['fullname','username','email','phone_number']
    success_url = reverse_lazy('list_u') 
    
    
class UserDeleteView(DeleteView):
    model = User
    template_name = 'delete_u.html'
    success_url = reverse_lazy('list_u') 
    
    
    
# Peyment

class PaymentListView(ListView):
    model = Payment
    template_name = 'list_p.html'
    
class PaymentDetailView(DetailView):
    model = Payment
    template_name = 'detail_p.html'
    
class PaymentCreateView(CreateView):
    model = Payment
    template_name = 'create_p.html'
    fields = ['cord','description','price']
    success_url = reverse_lazy('list_p') 
    
    
class PaymentUpdateView(UpdateView):
    model = Payment
    template_name = 'update_p.html'
    fields = ['cord','description','price']
    success_url = reverse_lazy('list_p') 
    
    
class PaymentDeleteView(DeleteView):
    model = Payment
    template_name = 'delete_p.html'
    success_url = reverse_lazy('list_p') 
    
    


# Ciname

class CinemaListView(ListView):
    model = Cinema    
    template_name = 'list_c.html'
    
class CinemaDetailView(DetailView):
    model = Cinema
    template_name = 'detail_c.html'
    
class CinemaCreateView(CreateView):
    model = Cinema
    template_name = 'create_c.html'
    fields = ['name','location','genres']
    success_url = reverse_lazy('list_c') 
    
    
class CinemaUpdateView(UpdateView):
    model = Cinema
    template_name = 'update_c.html'
    fields = ['name','location','genres']
    success_url = reverse_lazy('list_c') 
    
    
class CinemaDeleteView(DeleteView):
    model = Cinema
    template_name = 'delete_c.html'
    success_url = reverse_lazy('list_c') 
    
    
    
# Genre

class GenreListView(ListView):
    model = Genre    
    template_name = 'list_g.html'
    
class GenreDetailView(DetailView):
    model = Genre
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context["answer"] = Cinema.objects.filter(genres = self.kwargs['pk'])
        return context
    template_name = 'detail_g.html'
    
class GenreCreateView(CreateView):
    model = Genre
    template_name = 'create_g.html'
    fields = ['name']
    success_url = reverse_lazy('list_g') 
    
    
class GenreUpdateView(UpdateView):
    model = Genre
    template_name = 'update_g.html'
    fields = ['name']
    success_url = reverse_lazy('list_g') 
    
    
class GenreDeleteView(DeleteView):
    model = Genre
    template_name = 'delete_g.html'
    success_url = reverse_lazy('list_g') 
    
    
    
    