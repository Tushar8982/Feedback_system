from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import Feedback
from .serializers import FeedbackSerializer
from .tasks import send_feedback_email_task

class FeedbackListCreateView(generics.ListCreateAPIView):
    queryset = Feedback.objects.all().order_by('-created_at')
    serializer_class = FeedbackSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        feedback = serializer.save(user=self.request.user if self.request.user.is_authenticated else None)
        send_feedback_email_task.delay(feedback.id)

class FeedbackDetailView(generics.RetrieveAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [permissions.IsAuthenticated]

class ProtectedHelloView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        return Response({"message": f"Hello, {request.user.username}!"})
