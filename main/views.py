from django.shortcuts import render

def index(request):
    data = {
        'title': 'Главная страница',
        'values': ['some', 'hello', 'life'],
        'me': {
            'car': 'BMW',
            'age': 21,
            'hobby': 'chess'
        }
    }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')