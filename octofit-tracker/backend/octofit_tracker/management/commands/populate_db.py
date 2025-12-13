from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

from octofit_tracker import models as app_models

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Eliminar datos existentes
        User = get_user_model()
        User.objects.all().delete()
        app_models.Team.objects.all().delete()
        app_models.Activity.objects.all().delete()
        app_models.Leaderboard.objects.all().delete()
        app_models.Workout.objects.all().delete()

        # Crear equipos
        marvel = app_models.Team.objects.create(name='Marvel')
        dc = app_models.Team.objects.create(name='DC')

        # Crear usuarios
        users = [
            User.objects.create_user(username='ironman', email='ironman@marvel.com', password='pass', team=marvel),
            User.objects.create_user(username='spiderman', email='spiderman@marvel.com', password='pass', team=marvel),
            User.objects.create_user(username='batman', email='batman@dc.com', password='pass', team=dc),
            User.objects.create_user(username='superman', email='superman@dc.com', password='pass', team=dc),
        ]

        # Crear actividades
        activities = [
            app_models.Activity.objects.create(user=users[0], type='run', duration=30, distance=5),
            app_models.Activity.objects.create(user=users[1], type='cycle', duration=45, distance=20),
            app_models.Activity.objects.create(user=users[2], type='swim', duration=60, distance=2),
            app_models.Activity.objects.create(user=users[3], type='run', duration=25, distance=4),
        ]

        # Crear workouts
        workouts = [
            app_models.Workout.objects.create(user=users[0], name='Chest Day', description='Bench press, push-ups'),
            app_models.Workout.objects.create(user=users[1], name='Leg Day', description='Squats, lunges'),
            app_models.Workout.objects.create(user=users[2], name='Cardio', description='Running, cycling'),
            app_models.Workout.objects.create(user=users[3], name='Strength', description='Deadlift, pull-ups'),
        ]

        # Crear leaderboard
        app_models.Leaderboard.objects.create(team=marvel, points=100)
        app_models.Leaderboard.objects.create(team=dc, points=90)

        self.stdout.write(self.style.SUCCESS('La base de datos octofit_db ha sido poblada con datos de prueba.'))
