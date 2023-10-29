from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from .models import Chicken, Snack
from .forms import LayingForm

# chickens = [
#     {'name': "Sage", 'breed': 'Olive Egger', 'description': 'Grey with Beard', 'age': 3},
#     {'name': "Sclepi", 'breed': 'Golden Lace', 'description': 'Black and Golden', 'age': 3},
# ]

# Create your views here.
def home(request):
    return render(request, 'chickens/home.html')

def about(request):
    return render(request, 'chickens/about.html')

def chickens_index(request):
    chickens = Chicken.objects.all()
    return render(request, 'chickens/index.html', {
        'chickens': chickens
    })

def chickens_detail(request, pk):
    chicken = Chicken.objects.get(id=pk)

    laying_form = LayingForm
    return render(request, 'chickens/detail.html', {
        'chicken': chicken,
        'laying_form': laying_form
    })

def add_laying(request, pk):
    form = LayingForm(request.POST)

    if form.is_valid():
        new_laying = form.save(commit=False)
        new_laying.chicken_id = pk
        new_laying.save()
    
    return redirect('detail', pk = pk)

# class based views
class ChickenCreate(CreateView):
    model = Chicken
    fields = ['name', 'breed', 'description', 'age']

class ChickenUpdate(UpdateView):
    model = Chicken

    fields = ['breed', 'description', 'age']

class ChickenDelete(DeleteView):
    model = Chicken
    success_url = '/chickens'

class SnackList(ListView):
    model = Snack

class SnackDetail(DetailView):
    model = Snack

class SnackCreate(CreateView):
    model = Snack
    fields = '__all__'

class SnackUpdate(UpdateView):
    model = Snack
    fields = ['name', 'amount']

class SnackDelete(DeleteView):
    model = Snack
    success_url = '/snacks'