from django.http import HttpResponse

def odd_or_even(request, num):
    if num % 2 == 0:
        return HttpResponse(f'This number is even')
    else:
        return HttpResponse(f'This number is odd')