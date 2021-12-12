from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserModel

class LeagueAdvisorAdmin(UserAdmin):
        fieldsets = UserAdmin.fieldsets
        UserAdmin.list_display = list(UserAdmin.list_display)
        REQUIRED_FIELDS = ["email"]

admin.site.register(UserModel)


