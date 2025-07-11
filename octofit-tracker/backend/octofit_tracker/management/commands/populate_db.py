from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate octofit_db with test data for users, teams, activities, leaderboard, and workouts.'

    def handle(self, *args, **options):
        # Users
        User.objects.all().delete()
        users = [
            User(username='alice', email='alice@merington.edu', age=16, team='Merington Tigers'),
            User(username='bob', email='bob@merington.edu', age=17, team='Merington Tigers'),
            User(username='carol', email='carol@merington.edu', age=16, team='Merington Panthers'),
        ]
        for user in users:
            user.save()

        # Teams
        Team.objects.all().delete()
        teams = [
            Team(name='Merington Tigers', members=['alice', 'bob']),
            Team(name='Merington Panthers', members=['carol']),
        ]
        for team in teams:
            team.save()

        # Activities
        Activity.objects.all().delete()
        activities = [
            Activity(user='alice', type='run', duration=30, calories=200),
            Activity(user='bob', type='cycle', duration=45, calories=350),
            Activity(user='carol', type='swim', duration=60, calories=400),
        ]
        for activity in activities:
            activity.save()

        # Leaderboard
        Leaderboard.objects.all().delete()
        leaderboard_entries = [
            Leaderboard(user='alice', points=1200),
            Leaderboard(user='bob', points=1100),
            Leaderboard(user='carol', points=1300),
        ]
        for entry in leaderboard_entries:
            entry.save()

        # Workouts
        Workout.objects.all().delete()
        workouts = [
            Workout(name='Morning Cardio', description='30 min run + 15 min cycle'),
            Workout(name='Swim Session', description='60 min swim'),
        ]
        for workout in workouts:
            workout.save()

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
