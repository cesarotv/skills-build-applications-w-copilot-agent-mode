from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Borrar datos existentes
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Crear equipos
        marvel = Team.objects.create(name="Marvel", description="Marvel superheroes")
        dc = Team.objects.create(name="DC", description="DC superheroes")

        # Crear usuarios
        tony = User.objects.create(name="Tony Stark", email="tony@stark.com", team=marvel)
        steve = User.objects.create(name="Steve Rogers", email="steve@rogers.com", team=marvel)
        bruce = User.objects.create(name="Bruce Wayne", email="bruce@wayne.com", team=dc)
        diana = User.objects.create(name="Diana Prince", email="diana@prince.com", team=dc)

        # Crear workouts
        pushups = Workout.objects.create(name="Pushups", description="Upper body", difficulty="Easy")
        running = Workout.objects.create(name="Running", description="Cardio", difficulty="Medium")
        yoga = Workout.objects.create(name="Yoga", description="Flexibility", difficulty="Easy")

        # Crear actividades
        Activity.objects.create(user=tony, type="Running", duration=30, date=timezone.now())
        Activity.objects.create(user=steve, type="Pushups", duration=20, date=timezone.now())
        Activity.objects.create(user=bruce, type="Yoga", duration=40, date=timezone.now())
        Activity.objects.create(user=diana, type="Running", duration=25, date=timezone.now())

        # Crear leaderboard
        Leaderboard.objects.create(user=tony, score=120, rank=1)
        Leaderboard.objects.create(user=steve, score=110, rank=2)
        Leaderboard.objects.create(user=bruce, score=105, rank=3)
        Leaderboard.objects.create(user=diana, score=100, rank=4)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully!'))
