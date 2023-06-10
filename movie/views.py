from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

from django.shortcuts import redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from .models import Movie, MovieLinks, Rating


# User Regsiter Function
# def register_request(request):
# 	if request.method == "POST":
# 		form = NewUserForm(request.POST)
# 		if form.is_valid():
# 			user = form.save()
# 			login(request, user)
# 			messages.success(request, "Registration successful." )
# 			return redirect("homepage")
# 		messages.error(request, "Unsuccessful registration. Invalid information.")
# 	form = NewUserForm()
# 	return render (request=request, template_name="movie/register.html", context={"register_form":form})


# User Login Function
# def login_request(request):
# 	if request.method == "POST":
# 		form = AuthenticationForm(request, data=request.POST)
# 		if form.is_valid():
# 			username = form.cleaned_data.get('username')
# 			password = form.cleaned_data.get('password')
# 			user = authenticate(username=username, password=password)
# 			if user is not None:
# 				login(request, user)
# 				messages.info(request, f"You are now logged in as {username}.")
# 				return redirect("homepage")
# 			else:
# 				messages.error(request,"Invalid username or password.")
# 		else:
# 			messages.error(request,"Invalid username or password.")
# 	form = AuthenticationForm()
# 	return render(request=request, template_name="main/login.html", context={"login_form":form})


# User Logout Function
# def logout_request(request):
# 	logout(request)
# 	messages.info(request, "You have successfully logged out.") 
# 	return redirect("homepage")



# Show all Movies at Home
class HomeView(ListView):
    model = Movie
    template_name = 'movie/home.html'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['top_rated'] = Movie.objects.filter(status='TR')
        context['most_watched'] = Movie.objects.filter(status='MW')
        context['recently_added'] = Movie.objects.filter(status='RA')
        return context


# Show all Movie
class MovieList(ListView):
    model = Movie
    paginate_by = 4


#  Movie details View 
class MovieDetail(DetailView):
    model = Movie
    paginate_by = 4

    def get_context_data(self, **kwargs ):
        context = super(MovieDetail, self).get_context_data(**kwargs)
        context['links'] = MovieLinks.objects.filter(movie=self.get_object())
        # Order_by('created')[0:3]
        context['related_movies'] = Movie.objects.filter(category=self.get_object().category)
        return context


# Movies Reviews    
class MovieComment(CreateView):
    model = Rating
    
    def get_context_data(self, **kwargs ):
        movie_id = self.get_object().id
        return movie_id
    
    def post(self, request, *args, **kwargs):
        movie_id = kwargs['pk']
        rate = request.POST.get('rate')
        comment = request.POST.get('comment')
        movie = get_object_or_404(Movie, id=movie_id)
        Rating.objects.create(movie=movie, rate=rate, comment=comment)
        return redirect('movie-detail', pk=movie_id)
    
    
# Movies by Category list View
class MovieCategory(ListView):
    model = Movie
    paginate_by = 4
    
    def get_queryset(self):
        self.category = self.kwargs['category']
        return Movie.objects.filter(category=self.category)
        
    def get_context_data(self, **kwargs):
        context = super(MovieCategory, self).get_context_data(**kwargs)
        context['movie_category'] = self.category
        return context


# Movie by Language list View
class MovieLanguage(ListView):
    model = Movie
    
    def get_queryset(self):
        self.language = self.kwargs['lang']
        return Movie.objects.filter(language=self.language)
        
    def get_context_data(self, **kwargs):
        context = super(MovieLanguage, self).get_context_data(**kwargs)
        context['movie_language'] = self.language
        return context


# Movies by Searching list View
class MovieSearch(ListView):
    model = Movie
    
    def get_queryset(self):
        query = self.request.GET.get('query')
        if query:
            object_list = Movie.objects.filter(title__icontains=query)
        else:
            object_list = self.model.objects.none()
        return object_list
        
        