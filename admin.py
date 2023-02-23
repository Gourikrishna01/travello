from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(User_details)
admin.site.register(PackageDetails)
admin.site.register(Book_Tour)
admin.site.register(Feedback)
admin.site.register(Payment)
admin.site.site_header="travello admin"