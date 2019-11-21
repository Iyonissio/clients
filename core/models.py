from django.db import models



class ID(models.Model):
    numero = models.CharField(max_length=50)

    def __str__(self):
        return self.numero


class Client(models.Model):
    nome = models.CharField(max_length=70)
    ultimo_nome = models.CharField(max_length=70)
    idade = models.IntegerField()
    salario = models.DecimalField(max_digits=7,decimal_places=2)
    email = models.EmailField(null=True,blank=True)
    foto = models.ImageField(null=True,blank=True , upload_to='clients')
    data_nascimento = models.DateField(null=True, blank=True)
    doc_id = models.OneToOneField(ID , null=True ,on_delete=models.CASCADE)

    def get_fullname(self):
        return self.nome+' '+self.ultimo_nome

    def __str__(self):
        return self.get_fullname()

class Produto(models.Model):
    descrisao = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=7, decimal_places=2)
    taxas = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.descrisao

class Saldo(models.Model):
    saldo_numero = models.CharField(max_length=10)
    client =models.ForeignKey(Client,on_delete=False)
    data = models.DateField(auto_now_add=True)
    total = models.DecimalField(max_digits=7,decimal_places=2)
    produtos = models.ManyToManyField(Produto , null=True, blank=True)

    def __str__(self):
        return self.saldo_numero