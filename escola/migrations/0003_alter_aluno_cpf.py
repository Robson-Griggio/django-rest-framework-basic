# Generated by Django 4.0.4 on 2022-05-25 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0002_alter_aluno_data_nascimento_alter_aluno_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='cpf',
            field=models.CharField(max_length=11, unique=True),
        ),
    ]
