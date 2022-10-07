from django.contrib import admin
from .models import CustomUser
from .forms import CustomUserForm

# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'gender', 'national_code', 'birthday_date')
    readonly_fields = ('first_name', 'last_name',)
    search_fields = ['username', 'full_name']
    ordering = ('-ceremony_datetime',)
    form = CustomUserForm

    def first_name(self, obj):
        return obj.get_first_and_last_name()['first_name']

    def last_name(self, obj):
        return obj.get_first_and_last_name()['last_name']

admin.site.register(CustomUser, CustomUserAdmin)
