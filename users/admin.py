from django.contrib import admin
from .models import User


@admin.register(User)
#model admin 상속받아서 register 등록, 맵핑
class UserAdmin(admin.ModelAdmin) :
    list_display = [
        'username',
        'email',
        'date_joined',
    ]

    list_filter = [
        'date_joined',
    ]

    sortable_by = [
        'username',
        'email',
        'date_joined',
    ]

    