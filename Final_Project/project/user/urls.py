from django.urls import path, include
from django.conf import settings
from . import views 
from .views import home, profile, aboutus
from django.conf.urls.static import static

urlpatterns = [
		path('', views.index, name ='index'),
        path('home/', home, name='home'),
        path('profile/', profile, name='profile'),
    	path('aboutus/', aboutus, name='aboutus'),
    	# Add new URLs for Art, Write, Music, and Puzzles pages
    	path('art/', views.art_page, name='art_page'),
    	path('write/', views.write_page, name='write_page'),
    	path('music/', views.music_page, name='music_page'),
    	path('puzzles/', views.puzzles_page, name='puzzles_page'),
]

