from django.contrib import admin
from .models import User, Team, Activity, Workout, Leaderboard
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        (None, {'fields': ('team',)}),
    )
    list_display = ('username', 'email', 'team', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email')

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('user', 'type', 'duration', 'distance', 'created_at')
    search_fields = ('user__username', 'type')

@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'created_at')
    search_fields = ('user__username', 'name')

@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    list_display = ('team', 'points', 'updated_at')
    search_fields = ('team__name',)
