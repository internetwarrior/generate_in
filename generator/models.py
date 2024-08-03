from django.db import models
import uuid
from django.contrib.auth.models import User
from django.utils import timezone
from solo.models import SingletonModel

class PaymentInformation(SingletonModel):
    cash_rate = models.IntegerField(default=0)
    payment_information = models.TextField(default='Банк Мира')
    
    def __str__(self):
        return "Настройки"
        
    class Meta:
        verbose_name = "Настройки информации"




class Invoice(models.Model):
    #-----------KEY VALUES------------
    id = models.UUIDField(default=uuid.uuid4,unique=True, primary_key=True,editable=False)
    
    created = models.DateField(auto_now =True )
    
    user = models.ForeignKey(User, on_delete =models.CASCADE)
    
    #---------INVOICE INFO------------
    invoice_number = models.CharField(max_length=20, unique=True)
    
    recipient_detail = models.CharField(max_length=250)
    
    payer_detail = models.CharField(max_length=250)
    
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    
    
    
    def __str__(self):
        return f'Номер Инвойса {self.invoice_number} - {self.recipient_detail}'
    class Meta:
        verbose_name = "Список Инвойсов"
        


class Receipt(models.Model):
    STATUS_CHOICES = [
       
        ('A', 'Ожидание Оплаты'), 
        ('B', 'Ожидание Соглашение'),
        ('C', 'На проверке'),
        ('D', 'Оплачено')
    ]
    
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default ='A')
    cash_rate =models.IntegerField(default=0)
    #--------IMPORTANT PART--------
    created = models.DateField(auto_now=True)
    
    id = models.UUIDField(default=uuid.uuid4,unique=True, primary_key=True,editable=False)
    
    invoice = models.OneToOneField(Invoice, on_delete= models.CASCADE)
    
    #--------GENERAL INFORMATION
    
    
    total_cash = models.IntegerField(null=True, default =0)

    
    payment_date= models.DateField(auto_now=True)
    sub_agent = models.TextField(default='Инфо', blank=True)
    completed_act =models.TextField(default = 'Пусто',blank =True)
    agent_report = models.TextField(default='Пусто',blank=True)
    
    swift = models.FileField(upload_to='swift/', blank =True)
    
    class Meta:
        verbose_name = "Список  дел"    
        
    
        
    