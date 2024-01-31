from django.shortcuts import render


def index(request):
    data = {'title': 'Гдавная страница',
            "values": ['hi', 'world', 'cars'],
            'car': {'car': 'bmw',
                    'model': 'x7',
                    'power': '540ph'}
            }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')


def contact(request):
    return render(request, 'main/contact.html')
