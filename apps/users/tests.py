from django.test import TestCase
from django.http import HttpResponse
# Create your tests here.
# 测试

from django.core.mail import send_mail


def sendmail():# SMTP
    send_mail(
        'Subject here',
        'Here is the message.',
        'from@example.com',
        ['to@example.com'],
        fail_silently=False,
        html_message='asdfasda'
    )

def test(request):
    sendmail()
    return HttpResponse('aaaa')
