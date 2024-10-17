from django.shortcuts import render
from .models import *


def main_view(request):
    books = Book.objects.filter(is_popular=True)
    authors = Author.objects.all()

    context = {
        'books': books,
        'word': 'HELLO!!!',
        'authors': authors
    }

    return render(request, 'main_template.html', context=context)


def book_detail_view(request, book_id):
    from django.core.exceptions import ObjectDoesNotExist
    try:
        book_object = Book.objects.get(id=book_id)
        context = {
            'book': book_object
        }
        return render(request, 'book_detail.html', context=context)
    except ObjectDoesNotExist:
        context = {}
        return render(request, 'book_detail.html', context=context)


def book_create_view(request):
    if request.method == 'GET':
        # GET -> Вернуть "бланк" html
        authors = Author.objects.all()
        genres = Genre.objects.all()
        context = {
            'authors': authors,
            'genres': genres
        }
        return render(request, 'book_create.html', context=context)
    elif request.method == 'POST':
        name = request.POST.get('book_name')

        author = request.POST.get('book_author')
        author = Author.objects.get(id=author)
        # Находим автора в SQL по принятому id

        genre = request.POST.get('book_genre')
        genre = Genre.objects.get(id=genre)
        # Находим жанра в SQL по принятому id

        year = int(request.POST.get('book_year'))

        is_popular = request.POST.get('book_is_popular')
        if is_popular == 'on':
            is_popular = True
        else:
            is_popular = False

        book = Book(
            name=name,
            author=author,
            genre=genre,
            year=year,
            is_popular=is_popular
        )  # Создаем книгу в виде объекта
        book.save()  # Сохраняет объект в базе данных

        context = {
            'book': book
        }
        return render(request, 'book_detail.html', context=context)


def book_delete_view(request, book_id):
    if request.method == 'POST':
        from django.shortcuts import redirect
        book = Book.objects.get(id=book_id)
        book.delete()  # delete() -> Удаляет объект из Базы Данных
        return redirect(main_view)
        # redirect(main_view) -> Перенаправляет на main_view


def book_update_view(request, book_id):
    if request.method == 'GET':
        book = Book.objects.get(id=book_id)
        authors = Author.objects.all()
        genres = Genre.objects.all()
        context = {
            'book': book,
            'authors': authors,
            'genres': genres
        }
        return render(request, 'book_update.html', context=context)
    elif request.method == 'POST':
        name = request.POST.get('book_name')

        author = request.POST.get('book_author')
        author = Author.objects.get(id=author)

        genre = request.POST.get('book_genre')
        genre = Genre.objects.get(id=genre)

        year = int(request.POST.get('book_year'))

        is_popular = request.POST.get('book_is_popular')
        if is_popular == 'on':
            is_popular = True
        else:
            is_popular = False

        book = Book.objects.get(id=book_id)
        book.name = name  # Обновляем имя
        book.author = author  # Обновляем автора
        book.genre = genre  # Обновляем жанр
        book.year = year  # Обновляем год
        book.is_popular = is_popular  # Обновляем популярность
        book.save()

        from django.shortcuts import redirect
        return redirect(book_detail_view, book_id=book_id)


# Создать 3 новых вью
# 1) author_detail_view(+ темплейт)
# 2) author_update_view(+ темплейт)
# 3) author_delete_view(Формочка с кнопкой удаления, должна быть
#    на темплейте для author_detail_view)
