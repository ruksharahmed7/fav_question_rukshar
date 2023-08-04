# views.py

from django.core.paginator import Paginator
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import FavoriteQuestion, ReadQuestion, Question

#home page view that shows a table with columns User, count of FavoriteQuestion, count of ReadQuestion
def user_question_counts(request):
    users = User.objects.all()

    #With this pagination technique, the page shows 100 users/page
    paginator = Paginator(users, 100)  # Show 100 users per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    user_counts = []

    for user in page_obj:
        #for each user, count its total no. of FavoriteQuestion and ReadQuestion
        favorite_count = FavoriteQuestion.objects.filter(user=user).count()
        read_count = ReadQuestion.objects.filter(user=user).count()
        user_counts.append({'user': user, 'favorite_count': favorite_count, 'read_count': read_count})

    return render(request, 'question/user_question_counts.html', {'user_counts': user_counts, 'page_obj': page_obj})


def user_profile(request, user_id):
    user = User.objects.get(pk=user_id)

    # Get the query parameter 'status' from the URL
    status = request.GET.get('status', 'all')

    if status == 'read':
        questions = ReadQuestion.objects.filter(user=user)
    elif status == 'unread':
        questions = FavoriteQuestion.objects.exclude(user=user)
    elif status == 'favorite':
        questions = FavoriteQuestion.objects.filter(user=user)
    elif status == 'unfavorite':
        questions = ReadQuestion.objects.exclude(user=user)
    else:
        questions = Question.objects.all()  # 'all' status, no filtering

    # Paginate the questions
    paginator = Paginator(questions, 100)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'question/user_profile.html', {
        'user': user,
        'status': status,
        'page_obj': page_obj
    })