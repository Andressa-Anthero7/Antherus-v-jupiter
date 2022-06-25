from django.contrib import admin
from .models import Formulario, Perfil, Produto, CadastroClientes

# Register your models here.


admin.site.register(Formulario)
admin.site.register(Perfil)
admin.site.register(Produto)
admin.site.register(CadastroClientes)


