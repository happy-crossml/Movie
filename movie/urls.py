from django.urls import path
from .views import MovieList, MovieDetail, MovieCategory, MovieLanguage, MovieSearch
from .views import*

app_name = 'movie'


urlpatterns = [
    
    # path("register/", register_request, name="register"),
    # path("login/", login_request, name="login"),
    # path("logout/", logout_request, name= "logout"),
    
    path('' , MovieList.as_view(), name='movie_list'),
    path('category/<str:category>/', MovieCategory.as_view(), name='movie_category'),
    path('language/<str:lang>/', MovieLanguage.as_view(), name='movie_language'),
    path('search/', MovieSearch.as_view(), name='movie_search'),
    path('<slug:slug>/', MovieDetail.as_view(), name='movie_detail'),
    
]    