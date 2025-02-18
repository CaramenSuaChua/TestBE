from rest_framework.response import Response
from rest_framework.views import APIView
from .models import HtmlFile
from .utils import get_file_content
import logging

logger = logging.getLogger(__name__)

class RetrieveHtmlFile(APIView):
    def post(self, request):
        try:
            # Lấy dữ liệu từ request
            data = request.data
            system = data.get("system")
            environment = data.get("environment")
            machine_number = data.get("machine_number")
            machine_level = data.get("machine_level")

            # Tìm file phù hợp
            file_entry = HtmlFile.objects.filter(
                system=system,
                environment=environment,
                machine_number=machine_number,
                machine_level=machine_level 
            ).first()

            if not file_entry:
                return Response({"success": False, "message": "File not found"}, status=404)

            # Lấy nội dung file
            file_content = get_file_content(file_entry.file_path)
            if not file_content:
                return Response({"success": False, "message": "File could not be read"}, status=500)

            return Response({
                "success": True,
                "filename": file_entry.filename,
                "content": file_content
            })

        except Exception as e:
            logger.error(f"Error retrieving HTML file: {str(e)}")
            return Response({"success": False, "message": "Internal server error"}, status=500)
