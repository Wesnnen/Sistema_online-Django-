# Generated by Django 4.2.5 on 2023-09-15 23:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataInicio', models.DateTimeField()),
                ('dataTermino', models.DateTimeField()),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cadastro.curso')),
            ],
        ),
    ]
