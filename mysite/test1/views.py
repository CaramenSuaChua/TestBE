from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Account
from .serializers import AccountSerializer 
from rest_framework.pagination import PageNumberPagination
import logging

# Cấu hình logging
logger = logging.getLogger(__name__) 

# 📌 Lấy danh sách tài khoản có phân trang  
class AccountListCreateView(generics.ListCreateAPIView): 
    queryset = Account.objects.all() 
    serializer_class = AccountSerializer
    pagination_class = PageNumberPagination  # Thêm phân trang 

    def create(self, request, *args, **kwargs): 
        try:
            return super().create(request, *args, **kwargs)  
        except Exception as e: 
            logger.error(f"Error creating account: {str(e)}")
            return Response({"error": "Internal Server Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# 📌 Lấy một tài khoản, cập nhật, xóa
class AccountRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer 

    def retrieve(self, request, *args, **kwargs):
        try:
            return super().retrieve(request, *args, **kwargs)
        except Exception as e:
            logger.error(f"Error fetching account: {str(e)}")
            return Response({"error": "Account not found"}, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, *args, **kwargs):
        try:
            return super().update(request, *args, **kwargs)
        except Exception as e:
            logger.error(f"Error updating account: {str(e)}")
            return Response({"error": "Internal Server Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, *args, **kwargs):
        try:
            return super().delete(request, *args, **kwargs)
        except Exception as e:
            logger.error(f"Error deleting account: {str(e)}")
            return Response({"error": "Internal Server Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
