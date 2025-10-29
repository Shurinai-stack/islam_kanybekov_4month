from django.shortcuts import render,HttpResponse

def test_view(request):
    return HttpResponse("Криштиану Роналду Душ Сантос Авейру")

def view_html(request):
    return render(request, "base.html")