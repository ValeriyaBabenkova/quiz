from django.contrib import admin
from .models import Users, GamesList, Theme, Questions, Answers, Tours, QuestionNum
# Register your models here.
admin.site.register(Users)
admin.site.register(GamesList)
admin.site.register(Theme)
admin.site.register(Tours)
admin.site.register(QuestionNum)
admin.site.register(Questions)
admin.site.register(Answers)