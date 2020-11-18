from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    mobile_no = models.CharField(max_length=10)
    goo_uid = models.CharField(max_length=150)

class SplitGroup(models.Model):
    date_created = models.DateField(auto_now_add=True)
    grp_name = models.CharField(max_length=150)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)

class CharterdOfAccounts(models.Model):
    acc_name = models.CharField(max_length=255)
    place = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    mobile_no = models.CharField(max_length=10)
    acc_status = models.IntegerField()
    acc_type = models.IntegerField()
    acc_script = models.IntegerField()
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.email


class SplitGroup(models.Model):
    date_created = models.DateField(auto_now_add=True)
    grp_name = models.ForeignKey(CharterdOfAccounts,on_delete=models.CASCADE)
    cus = models.CharField(max_length=150)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)

class JournalEntry(models.Model):
    date_created = models.DateField(blank=True)
    acc_name = models.ForeignKey(CharterdOfAccounts,on_delete=models.CASCADE)
    debit = models.IntegerField()
    credit = models.IntegerField()
    desc = models.CharField(max_length=150)
    to_acc = models.CharField(max_length=150)
    acc_type = models.IntegerField()
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)

class TradeDetails(models.Model):
    date_created = models.DateField(blank=True)
    acc_name = models.ForeignKey(CharterdOfAccounts,on_delete=models.CASCADE)
    debit_amount = models.IntegerField()
    credit_amount = models.IntegerField()
    desc = models.CharField(max_length=150)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)

class AmountSet(models.Model):
    date_created = models.DateField(auto_now_add=True,blank=True)
    acc_name = models.ForeignKey(CharterdOfAccounts,on_delete=models.CASCADE)
    debit = models.IntegerField()
    credit = models.IntegerField()
    set_type = models.IntegerField()
    tot = models.IntegerField()
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    
