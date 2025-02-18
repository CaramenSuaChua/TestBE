from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Person
from django.db.models import Avg
import logging

logger = logging.getLogger(__name__)

class TopAgeDifferenceView(APIView):
    def get(self, request):
        try:
            avg_age = Person.objects.aggregate(avg_age=Avg('age'))['avg_age']
            if avg_age is None:
                return Response({"error": "No data available"}, status=400)

            people = Person.objects.all()
            people_age_diff = [(person.id, abs(person.age - avg_age)) for person in people]

            # Sắp xếp theo độ chênh lệch lớn nhất
            people_age_diff.sort(key=lambda x: x[1], reverse=True)

            # Lấy 20% dân số có độ chênh lệch lớn nhất
            top_20_percent_count = int(len(people_age_diff) * 0.2)
            top_people_ids = [person[0] for person in people_age_diff[:top_20_percent_count]]

            top_people = Person.objects.filter(id__in=top_people_ids).values('id', 'name', 'age')

            return Response({"top_20_percent_people": list(top_people)})

        except Exception as e:
            logger.error(f"Error processing request: {str(e)}")
            return Response({"error": "Internal Server Error"}, status=500)
