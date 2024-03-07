from django.http import HttpResponse


def Login(request):
    return HttpResponse("Hello, world. You're at the user login")
def Logout(request):
    return HttpResponse("Hello, world. You're at the user logout")
