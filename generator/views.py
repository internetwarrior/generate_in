from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes, authentication_classes

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication


from .serializers import InvoiceSerializer,PaymentSerializer, ReceiptSerializer
from .models import Invoice,PaymentInformation,Receipt
from rest_framework import status


@api_view(['GET', 'POST'])

@permission_classes([IsAuthenticated])
def invoice(request):
    if request.method == 'POST':
        serializer = InvoiceSerializer(data=request.data, context={'request': request})
   
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # Return the validation errors with a 400 Bad Request status
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    invoices = Invoice.objects.filter(user=request.user)
    invoices.order_by('-created')
    serializer = InvoiceSerializer(invoices, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)




@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_receipt(request, pk):
    try:
        receipt = Receipt.objects.get(pk=pk)
    except Receipt.DoesNotExist:
        return Response({"error": "Receipt not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = ReceiptSerializer(receipt)
    return Response(serializer.data, status=status.HTTP_200_OK)




@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_config(request):
    config = PaymentInformation.objects.get()
    serializer =PaymentSerializer(config, many=False)
    return Response(serializer.data)





def react_app(request):
    return render(request, 'index.html')



@api_view(['PATCH'])
def update_receipt(request, pk):
    try:
        receipt = Receipt.objects.get(pk=pk)
    except Receipt.DoesNotExist:
        return Response({"error": "Receipt not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = ReceiptSerializer(receipt, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
