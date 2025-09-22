from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404, HttpResponseBadRequest

def index(request):
    
    context={
        'title':'index page',
        'content':'my index page'
    }
    
    return render(request,"FirstApp/index.html",context)


#Function-based View...재사용성, 호환성 떨어짐 >> Class-based 뷰 활용하기
def api(request):
    if request.method == "GET":
        data = {
            'name' : "kim",
            'age' : 20,
        }
        return JsonResponse(data)
    
    elif request.method == "POST":
        return HttpResponse('')
    
    else:
        #return HttpResponse('Wrong method')
        #raise Http404()
        raise HttpResponseBadRequest()
    
