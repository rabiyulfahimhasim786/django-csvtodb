from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
#polls models
from .models import Film, Genre
import csv
#others

def index(request):
    return HttpResponse("Hello, world !")


dot = '.'
def run(request):
    with open(dot+'/media/csv/pixar.csv') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

        #Film.objects.all().delete()
        #Genre.objects.all().delete()

        for row in reader:
            print(row)

            genre, _ = Genre.objects.get_or_create(name=row[0])

            film = Film(title=row[1],
                        year=row[2],
                        filmurl = row[3],
                        genre=genre)
            film.save()
    #return render('base.html')
    return HttpResponse("Hello, world !")

def indexhtml(request):
    filmes = Film.objects.all()
    return render(request, 'films.html', { 'filmes': filmes })