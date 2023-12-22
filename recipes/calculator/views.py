from django.http import HttpResponse
from django.shortcuts import render, reverse

import os
from django.urls import reverse


DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def recept_view(request, recipe_name):

    # Используем recipe_id для выбора рецепта из DATA
    selected_recipe = DATA.get(recipe_name)

    if selected_recipe:
        servings = int(request.GET.get('servings', 1))  # Получаем количество порций, по умолчанию 1
        adjusted_recipe = {ingredient: amount * servings for ingredient, amount in selected_recipe.items()}
        context = {'recipe': adjusted_recipe, 'recipe_name': recipe_name, 'servings': servings}
    else:
        context = {'recipe': None}

    return render(request, 'calculator/index.html', context)


# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
