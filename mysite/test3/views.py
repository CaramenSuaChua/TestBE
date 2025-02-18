from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Student
from django.db.models import Count, Q
import logging

logger = logging.getLogger(__name__)

class StudentAgeStatisticsView(APIView):
    def get(self, request):
        try:
            avg_age = 20 + (8 / 12)  # 20 năm 8 tháng = 20.6667 năm
            threshold_high = avg_age + 0.5  # Lớn hơn 6 tháng
            threshold_low = avg_age - 0.5   # Nhỏ hơn 6 tháng

            result = Student.objects.values('class_number').annotate(
                older_than_avg=Count('id', filter=Q(age__gt=threshold_high)),
                younger_than_avg=Count('id', filter=Q(age__lt=threshold_low))
            ).order_by('class_number')

            return Response({"data": list(result)})

        except Exception as e:
            logger.error(f"Error calculating student statistics: {str(e)}")
            return Response({"error": "Internal Server Error"}, status=500)
