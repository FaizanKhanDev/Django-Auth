from django.contrib import admin
from .models import (
    User,
    Profile,
    Product
)

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "first_name", "last_name", "email",)



# Register your models here.
admin.site.register(User,UserAdmin)
admin.site.register(Profile)
admin.site.register(Product)
