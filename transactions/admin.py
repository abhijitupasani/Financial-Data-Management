from django.contrib import admin
from .models import Account, Transaction, AuditLog

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('account_number', 'account_name', 'user', 'account_type', 'balance', 'created_at', 'updated_at')
    search_fields = ('account_number', 'account_name', 'user__username')

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('transaction_id', 'account', 'user', 'transaction_type', 'amount', 'category', 'status', 'created_at', 'updated_at')
    search_fields = ('transaction_id', 'account__account_number', 'user__username')

@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = ('model_name', 'object_id', 'action', 'changed_by', 'timestamp')
    search_fields = ('model_name', 'action', 'changed_by__username')
    readonly_fields = ('model_name', 'object_id', 'action', 'changed_by', 'changes', 'timestamp')
