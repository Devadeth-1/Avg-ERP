#Dashboard named app Here is the code for the dashboard:

from rest_framework.response import Response
from rest_framework.views import APIView

class AdminDashboardView(APIView):
    def get(self, request):
        data = {
            "total_employees": 352,
            "leave_count": 22,
            "new_employees": 32,
            "payouts": 32,
        }
        return Response(data)
