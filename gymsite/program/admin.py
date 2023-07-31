from django.contrib import admin
from .models import Exercise, Strech, Program, UserProfile, ProgramDay


class ExerciseAdmin(admin.ModelAdmin):
    search_fields = ['name']


class StrechAdmin(admin.ModelAdmin):
    search_fields = ['name']


class ExerciseInline(admin.TabularInline):
    model = ProgramDay.exercise.through  # inline forma bus susieta su vidine lentele, kuri saugo ManyToMany ryšį tarp
    # ProgramDay ir Exercise modelių. Ši lentelė yra prieinama per through atributą,automatiškai sugeneruoto Django

    fk_name = 'programday'   # foreign key vardas excercize modelyje ryšiui
    autocomplete_fields = ('exercise',)  # leidzia pasirinkti is saraso, bet reikalauja search_fields atributo admin klasėse


class StrechInline(admin.TabularInline):
    model = ProgramDay.strech.through
    fk_name = 'programday'
    autocomplete_fields = ('strech',)


class ProgramDayAdmin(admin.ModelAdmin):
    filter_horizontal = ('exercise', 'strech',)  # pasirinkimui patogiam
    inlines = [ExerciseInline, StrechInline]  # papildomos grafos redagavimiui iš PrgoramDay tiesiai


admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(Strech, StrechAdmin)
admin.site.register(Program)
admin.site.register(UserProfile)
admin.site.register(ProgramDay, ProgramDayAdmin)