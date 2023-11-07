from django.contrib import admin
from loginmodule.models import *

# Register your models here.
admin.site.register(AuthGroup)
admin.site.register(AuthGroupPermissions)
admin.site.register(AuthPermission)
admin.site.register(AuthUser)
admin.site.register(AuthUserGroups)
admin.site.register(AuthUserUserPermissions)
admin.site.register(DjangoAdminLog)
admin.site.register(DjangoContentType)
admin.site.register(DjangoMigrations)
admin.site.register(DjangoSession)
admin.site.register(Users)
admin.site.register(Booking)
admin.site.register(Payment)
admin.site.register(Package)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Issues)
admin.site.register(Contactus)
admin.site.register(Feedback)

