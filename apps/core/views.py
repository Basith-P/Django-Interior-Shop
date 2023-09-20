from django.shortcuts import render


def frontpage(request):
    return render(request, 'core/front_page.html')


def contact(request):
    return render(request, 'core/contact.html')
