from django.db import models
from user.models import User

# As a 'User' I want to be able to add a 'exercise' to my daily 'workout'. A workout can contain multiple exercises. 

class Exercise(models.Model):
    STRENGTH = 'S'
    AEROBIC = 'A'

    EXERCISE_TYPE = (
        (STRENGTH, 'Strength'),
        (AEROBIC, 'Aerobic'),
    )

    name = models.CharField(max_length=128)
    exercise_type = models.CharField(max_length=3, choices=EXERCISE_TYPE)
    weight = models.FloatField(blank=True, null=True)
    repetitions = models.PositiveIntegerField(null=True, blank=True)
    distance = models.FloatField(blank=True, null=True)
    time = models.DurationField(blank=True, null=True)

    def __str__(self):
        return self.name


class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='workout_user')
    date = models.DateField()
    exercise = models.ManyToManyField(
        Exercise,
        null=True,
        blank=True,
        related_name='workout_exercises'
    )

    def __str__(self):
        return self.date
