from django.shortcuts import render
from .models import *


def main_view(request):
    # request -> Запрос, который приходит от браузера
    # request.method -> Указывает каким методом был отправлен запрос(GET, POST)
    # print(request.method)  # GET

    # books = Book.objects.all()  # Возвращает все записи из таблицы Book(QuerySet)
    # print(books)
    # books = Book.objects.filter(name='Алхимик')  # Возвращает записи из таблицы Book по условию name='Алхимик'(QuerySet)
    # print(books)
    # books = Book.objects.get(id=1)  # Возвращает только одну запись из таблицы Book по условию id=1(Object)
    #                                 # (Ошибка, если их несколько)
    # print(books)

    books = Book.objects.filter(is_popular=True)  # Возвращает все книги с is_popular=True
    authors = Author.objects.all()

    # for i in range(len(books)):
    #     books[i].name = books[i].name.upper()

    context = {
        'books': books,
        'word': 'HELLO!!!',
        'authors': authors
    }
    # context -> dict. Данные, которые отправляем от вью в темплейт
    return render(request, 'main_template.html', context=context)
    # render -> Функция Django, которая прорисовывает темлейт
    # render(<request>, '<template_name>', context=<context>)


# 1) Создать вью, в которых выгрузить список всех жанров
# 2) Создать вью, в которых выгрузить список всех авторов
# 3) Создать к ним темплейты, и провести url
