from django.contrib import admin
from .models import UserProfile, MainCategory, SiteSettings, Content
# Register your models here.

admin.site.site_title = 'Django News'
admin.site.site_header = 'Django News'

admin.site.register(UserProfile)
admin.site.register(MainCategory)
admin.site.register(SiteSettings)
admin.site.register(Content)
