from django.shortcuts import render

def mPage(request):
    return render(request,"navigation_app/index.html")

def Spage(request):
    return render(request,"navigation_app/index.html")

def showData(request):
    d = {'author' : 'Rahim', 'age' : 20, 'lst' : [1,2,3],
    'courses' : 
        [
            {
                'id' : 1,
                'name':'python',
                'fee' : 10000,
            },
            {
                'id' : 2,
                'name':'django courses',
                'fee' : 100000,
            },
            {
                'id' : 3,
                'name':'development courses',
                'fee' : 100000,
            }
            
        ]}
    return render(request,"navigation_app/backendtoFront.html",d)