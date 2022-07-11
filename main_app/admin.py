from django.contrib import admin
# import your models here
from .models import Bird, Feeding, Toy, Photo

# Register your models here
admin.site.register(Bird)

admin.site.register(Feeding)

admin.site.register(Toy)
admin.site.register(Photo)
