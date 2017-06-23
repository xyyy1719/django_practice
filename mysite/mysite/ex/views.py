from django.shortcuts import render
from django.http import Http404

def custom_proc(request):
    return {
        'app': 'Ex',
        'user': request.user,
        'ip_address': request.META['REMOTE_ADDR']
    }

def run_ex(request, ex_no):
    if ex_no == '1':
        person = {'name': 'qi.chen', 'age': 36}
        return render(request, 'ex/ex1.html', {'person': person})
    elif ex_no == '2':
        return render(request, 'ex/ex2.html', {'items': ['apple', 'banana', 'orange']})
    elif ex_no == '3':
        return render(request, 'ex/ex3.html', {'person': Person('qi.chen', 36)})
    elif ex_no == '4':
        person = Person('qi.chen', 36)
        return render(request, 'ex/ex4.html', {'person': person})
    else:
        raise Http404()
    
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def say_hello(self):
        return "Hello, my name is {}".format(self.name)
    