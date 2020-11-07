from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(CharterdOfAccounts)
admin.site.register(JournalEntry)
admin.site.register(TradeDetails)