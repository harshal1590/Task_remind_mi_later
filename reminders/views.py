from django.http import JsonResponse
from .models import Reminder
import json

def create_reminder(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        date = data.get('date')
        time = data.get('time')
        message = data.get('message')

        reminder = Reminder.objects.create(date=date, time=time, message=message)
        return JsonResponse({'status': 'Reminder saved sucessfully'})
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'})