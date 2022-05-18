from django.contrib import admin
from django.contrib.auth.models import User

# Register your models here.

from .models import Employee, Mobile, Circle, Ssa

admin.site.site_header = "EZ MNP feedback portal - Admin"

# Re-register UserAdmin
admin.site.unregister(User)   # as we are reusing the same
admin.site.register(User)


admin.site.register(Mobile)

admin.site.register(Circle)
admin.site.register(Ssa)
# admin.site.register(Employee)
