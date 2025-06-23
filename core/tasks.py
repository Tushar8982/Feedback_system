from celery import shared_task
from django.core.mail import send_mail
from .models import Feedback
from django.conf import settings

@shared_task
def send_feedback_email_task(feedback_id):
    try:
        feedback = Feedback.objects.get(id=feedback_id)
        subject = f"New Feedback from {feedback.name}"
        message = f"Message: {feedback.message}\nEmail: {feedback.email}"
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
        )
    except Feedback.DoesNotExist:
        pass
