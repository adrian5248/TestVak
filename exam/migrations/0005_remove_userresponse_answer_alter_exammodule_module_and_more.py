# Generated by Django 5.0.2 on 2024-06-13 18:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0004_module_alter_exam_modules_alter_exammodule_module_and_more'),
        ('library', '0004_alter_question_question_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userresponse',
            name='answer',
        ),
        migrations.AlterField(
            model_name='exammodule',
            name='module',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.module', verbose_name='Modulo'),
        ),
        migrations.RemoveField(
            model_name='question',
            name='module',
        ),
        migrations.RemoveField(
            model_name='userresponse',
            name='question',
        ),
        migrations.AlterField(
            model_name='breakdown',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.question', verbose_name='Pregunta'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='modules',
            field=models.ManyToManyField(through='exam.ExamModule', to='library.module', verbose_name='Módulos'),
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.DeleteModel(
            name='Module',
        ),
        migrations.DeleteModel(
            name='UserResponse',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
