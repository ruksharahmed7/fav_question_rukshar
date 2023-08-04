from django.contrib import admin
from .models import Question, ReadQuestion, FavoriteQuestion
# Register your models here.
admin.site.register(Question)
admin.site.register(ReadQuestion)
admin.site.register(FavoriteQuestion)
