from django.shortcuts import render, HttpResponse, redirect
from models import Trip
from ..logReg_app .models import User

def index(request):
    if 'user' not in request.session:
        return redirect('/user')
    user = User.objects.get(id = request.session['user'])
    return render(request, 'travels_app/index.html', {'trips': Trip.objects.all(), 'user': user, 'user_trips': user.all_trips.all()})
def add(request):
    if 'user' not in request.session:
        return redirect('/user')
    return render(request, 'travels_app/new.html')
def create(request):
    if 'user' not in request.session:
        return redirect('/user')
    user = User.objects.get(id = request.session['user'])
    trip = Trip.objects.create(traveler = user, destination = request.POST['destination'], start_date = request.POST['start_date'], end_date = request.POST['end_date'], desc = request.POST['desc'])
    trip.all_users.add(user)
    return redirect('/travels')
def show(request, id):
    if 'user' not in request.session:
        return redirect('/user')
    trip = Trip.objects.get(id = id)
    trips = trip.all_users.exclude(id = request.session['user'])
    trips = trips.exclude(id = trip.traveler.id)
    return render(request, 'travels_app/show.html', {'trips': trips, 'trip': trip})
def join(request, id):
    if 'user' not in request.session:
        return redirect('/user')
    user = User.objects.get(id = request.session['user'])
    trip = Trip.objects.get(id = id)
    trip.all_users.add(user)
    trip.save()
    return redirect("/travels")
def logout(request):
    request.session.flush()
    return redirect('/user')
