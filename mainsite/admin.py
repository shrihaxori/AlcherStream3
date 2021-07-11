from django.contrib import admin

from .models import Favorite
from .models import User
from .models import Movie

# Register your models here.

admin.site.register(Favorite)