from rest_framework import serializers
from .models import Invoice, Receipt, PaymentInformation

class ReceiptSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField(source='get_status_display', read_only=True)
    class Meta:
        model = Receipt
        fields = ['id', 'status_update','status', 'cash_rate', 'created', 'invoice', 'total_cash', 'payment_date', 'sub_agent', 'completed_act', 'agent_report', 'swift']
        read_only_fields = ['created', 'invoice', 'total_cash', 'payment_date', 'sub_agent', 'completed_act', 'agent_report', 'swift']
    def get_status(self, obj):
        # Return the display value of the status field
        return dict(Receipt.STATUS_CHOICES).get(obj.status)
    status_update = serializers.ChoiceField(choices=Receipt.STATUS_CHOICES, write_only=True)
    def update(self, instance, validated_data):
        # Check if 'status_update' is in the validated_data
        status_update = validated_data.pop('status_update', None)
        if status_update:
            # Update the instance's status
            instance.status = status_update
        
        # Proceed with the default update method
        return super().update(instance, validated_data)

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentInformation
        fields ='__all__'




class InvoiceSerializer(serializers.ModelSerializer):
    
    receipt= ReceiptSerializer(read_only=True)
    class Meta:
        model = Invoice
        #fields = '__all__'
        exclude =['user']
        
    def create(self, validated_data):
        # Create the Invoice
        invoice = super().create(validated_data)
        # Create a Receipt associated with the Invoice
        Receipt.objects.create(invoice=invoice)
        return invoice
