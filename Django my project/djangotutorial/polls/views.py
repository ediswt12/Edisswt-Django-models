from django.http import HttpResponse


def index(request):
    return HttpResponse("Edile xanım yeni seyler oyrenmeye calisir")
