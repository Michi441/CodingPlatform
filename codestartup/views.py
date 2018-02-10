from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import PlaceForm
from .models import Place



# Create your views here.

def home(request):
    places = Place.objects.all
    return render(request, 'home.html', {'places': places})

def place_detail(request, id):

    try:
        place = Place.objects.get(id=id)
    except Place.DoesNotExist:
        return redirect('/')


    return render(request, 'place_detail.html', {'place': place})

def edit_place(request, id):
    try:
        place = Place.objects.get(id=id, user=request.user)
        error = ""
        if request.method == 'POST':
            placeform = PlaceForm(request.POST, request.FILES, instance=place)
            if placeform.is_valid():
                place.save()
                return redirect('/')
            else:
                error = "Data is invalid!"

        return render(request, 'edit_place.html', {'place': place, 'error': error})
    except Place.DoesNotExist:
        return redirect('/')




def library(request):
    return render(request, 'library.html', {})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
        else:
            Error = 'Something went wrong!'

    return render(request, 'login.html', {})


## CREATE A NEW PLACE
def create(request):
    error = ''
    if request.method == 'POST':
        place_form = PlaceForm(request.POST, request.FILES)
        if place_form.is_valid():
            place = place_form.save(commit=False)
            place.user = request.user
            place.save()
            return redirect('/')
        else:
            print(place_form.errors)
            error = 'Data is invalid!'

    place_form = PlaceForm()
    return render(request, 'create.html', {'place_form': place_form, 'error': error})
