from django.contrib import admin
from .models import CreateBlog,Comment,Memoire,Personnel,Contact

# Register your models here.
    
class BlogAdmin(admin.ModelAdmin):
    list_display=('title','intro','slug','date_created')

class CommentAdmin(admin.ModelAdmin):
    list_display =('body','email','date_added')
        
class MemoireAdmin(admin.ModelAdmin):
    display=['title',]
    
class PersonnelAdmin(admin.ModelAdmin):
    list_display=['nom','poste']
    
class ContactAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'tel', 'objet')

admin.site.register(CreateBlog,BlogAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Personnel,PersonnelAdmin)
admin.site.register(Memoire,MemoireAdmin)
admin.site.register(Contact,ContactAdmin)
