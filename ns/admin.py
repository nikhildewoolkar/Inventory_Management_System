from django.contrib import admin
from .models import SignUp,Feedback,UserProfile,newsell,oldsell
# Register your models here.
admin.site.register(SignUp)
admin.site.register(Feedback)
admin.site.register(UserProfile)
admin.site.register(oldsell)
admin.site.register(newsell)