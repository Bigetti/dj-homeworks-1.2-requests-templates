import csv

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings



def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    # Путь к csv-файлу
    csv_file_path = settings.BUS_STATION_CSV

    # Чтение данных из csv-файла
    with open(csv_file_path, encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        stations_data = list(reader)

        # Количество элементов на странице
    items_per_page = 10

    # Создание объекта Paginator
    paginator = Paginator(stations_data, items_per_page)

    # Получение текущей страницы из GET-параметра
    page_number = request.GET.get('page', 1)

    # Получение объекта Page для текущей страницы
    page_obj = paginator.get_page(page_number)

    # Формирование контекста
    context = {
         'bus_stations': paginator.get_page(page_number),
    }
    return render(request, 'stations/index.html', context)
