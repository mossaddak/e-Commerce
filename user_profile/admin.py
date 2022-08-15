from django.contrib import admin
from .models import User, Account_type, Follow, Address

# Register your models here.
admin.site.register(User)
admin.site.register(Account_type)
admin.site.register(Follow)
admin.site.register(Address)
 