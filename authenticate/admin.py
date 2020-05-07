from django.contrib import admin
# Import the UserProfile model individually.
from .models import UserProfile

# Import the UserProfile model with Category and Page.
# If you choose this option, you'll want to modify the import statement you've already got to include UserProfile.
# from .models import Category, Page, UserProfile
# Register your models here.
admin.site.register(UserProfile)