from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import AccountCreationForm, AccountChangeForm
from .models import Account

class CustomUserAdmin(UserAdmin):
    add_form = AccountCreationForm
    form = AccountChangeForm
    model = Account
    list_display = ['email', 'username' ]

    # fieldsets = UserAdmin.fieldsets + (
    #     ('personal_info', {'fields': ('age','phone_number')}),
    # )

admin.site.register(Account, CustomUserAdmin)