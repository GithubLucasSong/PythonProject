from django.shortcuts import render, HttpResponse


# Create your views here.

def index(request):
    return render(request, 'index.html')


def calc(request):
    x1 = request.GET.get('x1')
    x2 = request.GET.get('x2')
    x3 = int(x1) + int(x2)
    return HttpResponse(x3)


def upload(request):
    if request.method == 'POST':
        f1 = request.FILES.get('f1')
        with open(f1.name, 'wb') as f:
            for i in f1:
                f.write(i)
        return HttpResponse('上传成功')
    return render(request, 'upload.html')
