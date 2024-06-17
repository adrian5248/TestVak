from django.db import models
from django.contrib.auth.models import User
from career.models import Career
from library.models import Module, Question


class Stage(models.Model):
    stage = models.IntegerField(
        verbose_name = "Etapa"
        )
    application_date = models.DateTimeField(
        verbose_name = "Fecha de aplicación")

    @property
    def year(self):
        return self.application_date.year
    
    @property
    def month(self):
        months = ['enero', 'febrero',
                'marzo', 'abril','mayo','junio',
                'julio','agosto','septiembre', 'octubre',
                'noviembre', 'diciembre']
        return months[self.application_date.month -1]


    def __str__(self):
        return f"{self.stage} - { self.month } { self.year}"

    class Meta:
        verbose_name = "Etapa"
        verbose_name_plural = "Etapas"

class Exam(models.Model):
    user = models.OneToOneField(
            User,
            on_delete = models.CASCADE,
            verbose_name = 'Usuario'
        )
    stage = models.ForeignKey(
            Stage,
            on_delete = models.CASCADE,
            verbose_name = 'Etapa'
        )
    career = models.ForeignKey(
            Career,
            on_delete = models.CASCADE,
            verbose_name = 'Carrera'
            )
    modules = models.ManyToManyField(
        Module,
        through='ExamModule',
        verbose_name= 'Módulos'
    )
    score = models.FloatField(
        verbose_name = 'Calificacion',
        default = 0.0
        )
    created = models.DateTimeField(
        verbose_name = "Fecha de creación",
        auto_now_add = True)
    updated = models.DateTimeField(
        verbose_name = 'Fecha de actualizacion',
        auto_now=True)
    
    def set_modules(self):
        for module in Module.objects.all():
            self.modules.add(module)

    def set_questions(self):
        for module in self.modules.all():
            for question in Question.objects.filter(module=module):
                Breakdown.objects.create(
                exam = self,
                question = question,
                correct = question.correct,
            )

    def __str__(self):
        return f"{self.user} - {self.career}: {self.score}"
    
    class Meta:
        verbose_name = "examen"
        verbose_name = "examenes"

class ExamModule(models.Model):
    exam = models.ForeignKey(
            Exam,
            on_delete = models.CASCADE,
            verbose_name ="Examen"
        )
    module = models.ForeignKey(
            Module,
            on_delete = models.CASCADE,
            verbose_name = 'Modulo'
        )
    active = models.BooleanField(
            verbose_name = "Activo",
            default = True
        )
    score = models.FloatField(
            verbose_name ="Calificación",
            default = 0.0
        )
    
    def __str__(self):
        return f"{self.module} - { self.score }"
    
class Breakdown(models.Model):
    exam = models.ForeignKey(
                Exam,
                on_delete = models.CASCADE,
                verbose_name = "Examen"
            )
    question = models.ForeignKey(
        Question,
        on_delete = models.CASCADE,
        verbose_name = "Pregunta"
    )
    answer = models.CharField(
        verbose_name = "Respuesta",
        max_length = 5,
        default = '-'
    )
    correct = models.CharField(
        verbose_name = "Respuesta correcta",
        max_length = 5,
        default = '-'
    )
