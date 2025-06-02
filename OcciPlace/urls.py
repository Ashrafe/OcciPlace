"""
URL configuration for OcciPlace project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views  # <-- ajouter en haut, pour importer votre vue home

urlpatterns = [
    path('admin/', admin.site.urls),
]



urlpatterns = [
    # ... vos autres urls ici ...
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),       # Gestion utilisateurs
    path('products/', include('products.urls')),       # Catalogue produits
    path('orders/', include('orders.urls')),           # Commandes
    path('wishlist/', include('wishlist.urls')),       # Wishlist
    path('notifications/', include('notifications.urls')), # Notifications
    path('loyalty/', include('loyalty.urls')),         # Fidélité
    
    path('', views.home, name='home'),   # Page d'accueil du site (URL racine)

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)