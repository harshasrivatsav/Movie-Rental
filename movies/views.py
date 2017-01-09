from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login
from .forms import UserForm
from .models import MovieInfo
from django.views import View
from django.contrib.auth import logout
from django.db.models import Q


def index(request):
    all_movies = MovieInfo.objects.all()
    return render(request, 'movies/index.html', {'all_movies': all_movies})

def detail(request, movie_id):
    movie = get_object_or_404(MovieInfo, pk=movie_id)
    return render(request, 'movies/detail.html', {'movie': movie})

class UserFormView(View):
    form_class = UserForm
    template_name = 'movies/register.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']

            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('movies:index')
        else:
            return render(request, self.template_name, {'form': form})


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('movies:index')
        else:
            return render(request, 'movies/login.html', {'error_message': 'Invalid login! Please try again'})
    return render(request, 'movies/login.html')


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'movies/login.html', context)


def search(request):
    all_movies = MovieInfo.objects.all()
    query = request.GET.get('q')
    all_movies = all_movies.filter(Q(Name__icontains=query) |
                                   Q(Cast__icontains=query) |
                                   Q(Director__icontains=query)|
                                   Q(Genre__icontains=query)|
                                   Q(Year__icontains=query) )
    return render(request, 'movies/index.html', {'all_movies': all_movies})


def payment(request):
    return render(request, 'movies/payment.html')


def success(request):
    return render(request, 'movies/success.html')


def news(request):
    return render(request, 'movies/news.html')



def newmovies(request):
    return render(request, 'movies/newmovies.html')



