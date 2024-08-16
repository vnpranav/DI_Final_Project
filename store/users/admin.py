from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'email', 'is_staff', 'is_active', 'bio', 'birth_date']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('bio', 'birth_date')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
