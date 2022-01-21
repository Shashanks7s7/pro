from django.contrib import admin
from .models import Blogs, Team
from .models import Messages
# Register your models here.
admin.site.register(Team)
admin.site.register(Messages)
admin.site.register(Blogs)