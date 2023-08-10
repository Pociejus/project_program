from django.db.models.signals import post_save  # signalas (būna įvairių)
from django.contrib.auth.models import User     # siuntėjas
from django.dispatch import receiver            # priėmėjas (dekoratorius)
from .models import UserProfile

# Sukūrus vartotoją automatiškai sukuriamas ir profilis.
@receiver(post_save, sender=User) # išviečiama kai sukuriamas User
def create_profile(sender, instance, created, **kwargs): # instance yra ką tik sukurtas User objektas. Sender-User klasė
    # created yra True(sukurtas) arba False(i6saugotas)
    if created:
        UserProfile.objects.create(user=instance)  # kuria UserProfile nauja ir susieja su User sukurtu
        print('KWARGS: ', kwargs)


# Pakoregavus vartotoją, išsaugomas ir profilis
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.userprofile.save()