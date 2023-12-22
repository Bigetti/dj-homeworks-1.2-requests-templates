"""recipes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from django.urls import path
from calculator.views import recept_view


urlpatterns = [
    # здесь зарегистрируйте вашу view-функцию
    path('recept/<str:recipe_name>/', recept_view, name='recept_view'),
    path('<str:recipe_name>/', recept_view, name='recept_view'),
    path('', recept_view, name='recept_view_short'),
    # Раскомментируйте код, чтобы данные урлы
    # обрабатывались Django

]
