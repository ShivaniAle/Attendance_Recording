from django.http import HttpResponseForbidden
from datetime import datetime

class HODTimeOfDayRestrictionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = request.user

        # Check if the user is authenticated and is an HOD
        if user.is_authenticated and user.user_type == '1':
            now = datetime.now()
            allowed_start_time = 12
              # 9 AM
            allowed_end_time = 17  # 5 PM

            if not allowed_start_time <= now.hour < allowed_end_time:
                return HttpResponseForbidden("Access allowed only between 12 PM and 5 PM for HOD users.")

        response = self.get_response(request)
        return response
