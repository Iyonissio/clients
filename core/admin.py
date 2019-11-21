from django.contrib import admin
from .models import Client , ID , Saldo , Produto

class ClientAdmin(admin.ModelAdmin):
    fields = ['nome','ultimo_nome','idade','salario','foto','doc_id']
    list_filter = ['nome','ultimo_nome','idade','salario']
    list_display = ['nome','ultimo_nome','idade','salario']
    search_fields = ['ultimo_nome','idade']

class SaldoAdmin(admin.ModelAdmin):
    fields = ['saldo_numero','client','total','produtos']
    list_filter = ['saldo_numero','client','total']
    list_display = ['saldo_numero','client','total']
    search_fields = ['saldo_numero','client','total']

admin.site.register(Client,ClientAdmin)
admin.site.register(ID)
admin.site.register(Saldo , SaldoAdmin)
admin.site.register(Produto)
