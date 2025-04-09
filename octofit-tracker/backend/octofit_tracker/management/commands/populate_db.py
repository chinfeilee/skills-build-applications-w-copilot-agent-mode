from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

# Ensure the Command class is properly defined and accessible
class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Add test data
        users = [
            User(email='john.doe@example.com', name='John Doe', age=25),
            User(email='jane.smith@example.com', name='Jane Smith', age=30),
            User(email='thundergod@mhigh.edu', name='Thunder God', age=35),
            User(email='metalgeek@mhigh.edu', name='Metal Geek', age=28),
            User(email='zerocool@mhigh.edu', name='Zero Cool', age=22),
            User(email='crashoverride@hmhigh.edu', name='Crash Override', age=27),
            User(email='sleeptoken@mhigh.edu', name='Sleep Token', age=29),
        ]
        User.objects.bulk_create(users)

        teams = [
            Team(name='Team Alpha', members=['john.doe@example.com', 'jane.smith@example.com']),
            Team(name='Blue Team', members=['thundergod@mhigh.edu', 'metalgeek@mhigh.edu']),
            Team(name='Gold Team', members=['zerocool@mhigh.edu', 'crashoverride@hmhigh.edu', 'sleeptoken@mhigh.edu']),
        ]
        Team.objects.bulk_create(teams)

        activities = [
            Activity(user='john.doe@example.com', activity_type='Running', duration=30),
            Activity(user='jane.smith@example.com', activity_type='Cycling', duration=45),
            Activity(user='thundergod@mhigh.edu', activity_type='Cycling', duration=60),
            Activity(user='metalgeek@mhigh.edu', activity_type='Crossfit', duration=120),
            Activity(user='zerocool@mhigh.edu', activity_type='Running', duration=90),
            Activity(user='crashoverride@hmhigh.edu', activity_type='Strength', duration=30),
            Activity(user='sleeptoken@mhigh.edu', activity_type='Swimming', duration=75),
        ]
        Activity.objects.bulk_create(activities)

        leaderboard = [
            Leaderboard(user='john.doe@example.com', score=100),
            Leaderboard(user='jane.smith@example.com', score=150),
            Leaderboard(user='thundergod@mhigh.edu', score=200),
            Leaderboard(user='metalgeek@mhigh.edu', score=180),
            Leaderboard(user='zerocool@mhigh.edu', score=170),
            Leaderboard(user='crashoverride@hmhigh.edu', score=160),
            Leaderboard(user='sleeptoken@mhigh.edu', score=140),
        ]
        Leaderboard.objects.bulk_create(leaderboard)

        workouts = [
            Workout(name='Morning Yoga', description='A relaxing yoga session to start the day'),
            Workout(name='HIIT', description='High-intensity interval training for fat loss'),
            Workout(name='Cycling Training', description='Training for a road cycling event'),
            Workout(name='Crossfit', description='Training for a crossfit competition'),
            Workout(name='Running Training', description='Training for a marathon'),
            Workout(name='Strength Training', description='Training for strength'),
            Workout(name='Swimming Training', description='Training for a swimming competition'),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Database populated with test data'))
