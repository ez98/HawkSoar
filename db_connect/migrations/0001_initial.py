# Generated by Django 4.2 on 2023-04-13 22:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_id', models.CharField(max_length=10)),
                ('event_name', models.CharField(max_length=20)),
                ('event_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Mid', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('A_number', models.CharField(max_length=9)),
                ('Student_Name', models.CharField(max_length=20)),
                ('Student_email', models.EmailField(max_length=254)),
                ('Major', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='TutorsCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tid', models.CharField(blank=True, default='', max_length=10)),
                ('course_id', models.CharField(max_length=10)),
                ('cname', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cwid', models.CharField(max_length=9)),
                ('is_tutor', models.BooleanField(default=False, verbose_name='Is Tutor')),
                ('is_student', models.BooleanField(default=False, verbose_name='Is Student')),
                ('is_mentor', models.BooleanField(default=False, verbose_name='Is Mentor')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=100)),
                ('Tid', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='db_connect.tutorscourse')),
            ],
        ),
        migrations.CreateModel(
            name='Has_Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('A_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Student_number', to='db_connect.student')),
                ('event_date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Edate', to='db_connect.events')),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Eid', to='db_connect.events')),
                ('event_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Ename', to='db_connect.events')),
            ],
        ),
        migrations.CreateModel(
            name='course_registered',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Course_id', models.CharField(max_length=10)),
                ('Course_Name', models.CharField(max_length=20)),
                ('A_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CWID', to='db_connect.student')),
            ],
        ),
        migrations.CreateModel(
            name='Assignments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Assignment_Name', models.CharField(max_length=10)),
                ('Description', models.CharField(max_length=20)),
                ('Attach', models.CharField(max_length=10)),
                ('Subject_Status', models.CharField(max_length=20)),
                ('A_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db_connect.student')),
                ('Tid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Tutor_id', to='db_connect.tutorscourse')),
            ],
        ),
    ]