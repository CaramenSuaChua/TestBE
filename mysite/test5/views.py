from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Person
import math
import logging

logger = logging.getLogger(__name__)

def calculate_distance(p1, p2):
    """Tính khoảng cách Euclidean giữa 2 người"""
    return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)

class TopFurthestPeopleView(APIView):
    def get(self, request):
        try:
            people = list(Person.objects.all())
            if not people:
                return Response({"error": "No data available"}, status=400)

            distances = []
            for person in people:
                # Tính khoảng cách đến người gần nhất
                min_distance = min(
                    calculate_distance(person, other)
                    for other in people if other.id != person.id
                )
                distances.append((person.id, min_distance))

            # Sắp xếp theo khoảng cách lớn nhất
            distances.sort(key=lambda x: x[1], reverse=True)

            # Lấy 10% người xa nhất
            top_10_percent_count = int(len(distances) * 0.1)
            top_people_ids = [person[0] for person in distances[:top_10_percent_count]]

            top_people = Person.objects.filter(id__in=top_people_ids).values('id', 'name', 'x', 'y')

            return Response({"top_10_percent_people": list(top_people)})

        except Exception as e:
            logger.error(f"Error processing request: {str(e)}")
            return Response({"error": "Internal Server Error"}, status=500)
