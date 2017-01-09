from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from carton.cart import Cart
from movies.models import MovieInfo



def add(request, movie_id):
    cart = Cart(request.session)
    movie = get_object_or_404(MovieInfo, pk=movie_id)
    cart.add(movie, price=movie.Price)
    return render(request, 'movies/added_to_cart.html', {'movie': movie})


def remove(request, movie_id):
    cart = Cart(request.session)
    movie = get_object_or_404(MovieInfo, pk=movie_id)
    cart.remove(movie)
    return render(request, 'shopping/show-cart.html')


def show(request):
    return render(request, 'shopping/show-cart.html')
