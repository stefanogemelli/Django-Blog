from django.http import HttpResponse

def ShowIndex():
    return HttpResponse("index")

def EditUser():
    return HttpResponse("edit_user")