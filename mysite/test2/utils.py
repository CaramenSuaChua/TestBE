import base64
import os
from django.conf import settings

def get_file_content(file_path):
    """ Đọc file và trả về nội dung Base64 """
    try:
        if not os.path.exists(file_path):
            return None
        with open(file_path, "rb") as file:
            return base64.b64encode(file.read()).decode("utf-8")
    except Exception as e:
        return None
