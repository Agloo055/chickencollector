from django.shortcuts import render
from .models import Chicken

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
    return render(request, 'chickens/detail.html', {'chicken': chicken})