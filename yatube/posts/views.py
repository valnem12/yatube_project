from django.http import HttpResponse


def index(request):
    return HttpResponse('Landing Page Test')

def group(request, slug):
    return HttpResponse(f'Blog Test {slug}')    
