from django.contrib import admin
from .models import UserProfile,HobbiesAndInterests,MusicEducation,ProfilePhotos #EmplyementHistory

admin.site.register(UserProfile)
admin.site.register(HobbiesAndInterests)
admin.site.register(MusicEducation)
#admin.site.register(EmplyementHistory)
admin.site.register(ProfilePhotos)