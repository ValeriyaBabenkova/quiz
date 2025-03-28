from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название команды')
    password = models.TextField(verbose_name='Пароль')

    class Meta:
        verbose_name = 'Команда'
        verbose_name_plural = 'Команды'

    def __str__(self):
        return self.name

class Auth(models.Model):
    pass

class Theme(models.Model):
    theme = models.CharField(max_length=100, verbose_name='Тема игры')

    class Meta:
        verbose_name = 'Тема игры'
        verbose_name_plural = 'Темы игр'

    def __str__(self):
        return self.theme

class GamesList(models.Model):
    name_game = models.TextField(max_length=100, verbose_name='Название игры')
    theme = models.ForeignKey(Theme, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='Тема игры')
    image = models.ImageField(upload_to='images', verbose_name='Картинка', blank=True, null=True)

    class Meta:
        verbose_name = 'Список игр'
        verbose_name_plural = 'Списки игр'

    def __str__(self):
        return self.name_game

class Tours(models.Model):
    num_tour = models.CharField(max_length=100,verbose_name='Номер тура')

    class Meta:
        verbose_name = 'Номер тура'
        verbose_name_plural = 'Номера туров'

    def __str__(self):
        return self.num_tour


class QuestionNum(models.Model):
    num_tour = models.ForeignKey(Tours,on_delete=models.CASCADE, verbose_name='Номер тура')
    num_question = models.CharField(max_length=100,verbose_name='Номер вопроса')

    class Meta:
        verbose_name = 'Номер вопроса'
        verbose_name_plural = 'Номера вопросов'

    def __str__(self):
        return self.num_question


class Questions (models.Model):
    name_game = models.ForeignKey(GamesList, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='Название игры')
    num_tour = models.CharField(max_length=256, verbose_name='Номер тура', blank=True, null=True)
    num_question = models.CharField(max_length=256, verbose_name='Номер вопроса', blank=True, null=True)
    text = models.CharField(max_length=256, verbose_name='Текст вопроса', blank=True, null=True)
    ans = models.CharField(max_length=256, verbose_name='Ответ', blank=True, null=True)

    class Meta:
        verbose_name = 'Вопросы игры'
        verbose_name_plural = 'Вопросы игры'

    def __str__(self):
        return f"Игра {self.name_game}. Вопрос {self.num_question} тура {self.num_tour}"

class Answers (models.Model):
    team = models.ForeignKey(Users, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='Название команды', related_name='team')
    answer_team = models.CharField (max_length=256, verbose_name='Ответ команды', blank=True, null=True)
    answer_right = models.ForeignKey(Questions, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='Правильный ответ', related_name='answer_right')

    class Meta:
        verbose_name = 'Проверка ответов'
        verbose_name_plural = 'Проверка ответов'

    def __str__(self):
        return self.answer_team
