from django.contrib import admin
from .models import *
#Register your models here. to work with it in admin panel


admin.site.register(Question)
admin.site.register(information)

# admin.site.register(storyData)

# another way to register (class base)
class storyDataAdmin(admin.ModelAdmin):
    fieldsets=[
    ('title',         {'fields':['title']}),
    ('content',       {'fields':['story','author']}),
    ('image',         {'fields':['image']}),
    ('likes',         {'fields':['likes']})


    ]
    # you can customize panel in here
    list_display=['title','date']
    search_fields=['title']
    # for more information search customize admin panel django

admin.site.register(storyData,storyDataAdmin)

