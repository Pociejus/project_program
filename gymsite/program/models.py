from datetime import datetime
from django.contrib.auth.models import User
from django.db import models
from PIL import Image


class Exercise(models.Model):
    name = models.CharField(max_length=100)
    muscle_group = models.CharField('muscle', max_length=50)
    comment = models.CharField(max_length=200, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to="exercize_pics")
    sets = models.DecimalField(decimal_places=0, max_digits=2)
    reps = models.DecimalField(decimal_places=0, max_digits=2)

    def __str__(self):
        return f'{self.muscle_group} {self.name}'

    def save(self, *args, **kwargs):  # mazinam nuotraukas jei per dideles
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Strech(models.Model):
    name = models.CharField(max_length=100)
    muscle_group = models.CharField('muscle', max_length=50)
    comment = models.CharField(max_length=200, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to="strech_pics")
    sets = models.DecimalField(decimal_places=0, max_digits=2)
    reps = models.DecimalField(decimal_places=0, max_digits=2)

    def __str__(self):
        return f'{self.muscle_group} {self.name}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Program(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)  # Ryšys su vartotoju
    days = models.ManyToManyField('ProgramDay', related_name='program_days',
                                  blank=True)  # Many-to-many ryšys su ProgramDay
    date_created = models.DateField(null=True, blank=True, default=datetime.now)

    class Meta:
        ordering = ['date_created', 'user']

    def __str__(self):
        return f'{self.user} {self.date_created}'


class ProgramDay(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  # one to many
    program = models.ForeignKey(Program, on_delete=models.CASCADE)  # one to many
    day_number = models.DecimalField(blank=True, null=True, decimal_places=0, max_digits=1)
    exercise = models.ManyToManyField(Exercise, blank=True)
    strech = models.ManyToManyField(Strech, blank=True)

    class Meta:
        ordering = ['day_number']

    def __str__(self):
        return f'{self.user} {self.day_number}'


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True, null=True, help_text='pvz +3706...')
    weight = models.DecimalField(blank=True, null=True, decimal_places=1, max_digits=4)
    height = models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=4, help_text='pvz 1.68')
    birth = models.DateField(null=True, blank=True)
    joined = models.DateField(null=False, blank=False, default=datetime.now)
    info = models.TextField(blank=True, null=True, max_length=1000, help_text='svarbi informacija')

    class Meta:
        ordering = ['user']

    def __str__(self):
        full_name = f'{self.user.first_name} {self.user.last_name}'
        return f'{full_name} {self.phone}'
