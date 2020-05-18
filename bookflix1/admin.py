from django.contrib import admin
from .models import Usuario, Tarjeta,Perfil, Comentario, Calificacion, Editorial, Autor,Genero,Novedad,Precio,Libro,Capitulo
# Register your models here.

class AutorAdmin(admin.ModelAdmin):
    search_fields=("id","nombre","nacimiento",)

class LibroAdmin (admin.ModelAdmin):
    autocomplete_fields=("autor",)
    list_display=("titulo","trailer","autor")
    search_fields=("titulo","autor_id__nombre",)
   
class TarjetaAdmin(admin.ModelAdmin):
    search_fields=("num",)

class UsuarioAdmin(admin.ModelAdmin):
    autocomplete_fields=("tarjeta",)
    list_display=("user", "dni")
    search_fields=("user_id__username","dni",)

admin.site.register(Usuario,UsuarioAdmin)
admin.site.register(Tarjeta,TarjetaAdmin)
admin.site.register(Perfil)
admin.site.register(Capitulo)
admin.site.register(Comentario)
admin.site.register(Calificacion)
admin.site.register(Editorial)
admin.site.register(Autor,AutorAdmin)
admin.site.register(Genero)
admin.site.register(Novedad)
admin.site.register(Precio)
admin.site.register(Libro,LibroAdmin)
