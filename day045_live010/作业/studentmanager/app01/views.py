from django.shortcuts import render, redirect, HttpResponse
from app01 import models


# Create your views here.
def index(request):
    return render(request, 'index.html')


def class_list(request):
    if request.method == 'POST':
        pass
    else:
        class_all = models.Class.objects.all()
        return render(request, 'class_list.html', {'class_all': class_all})


def class_add(request):
    if request.method == 'POST':
        class_name = request.POST.get('class_name')
        # 判断返回的数据是否为空
        if not class_name:
            return render(request, 'class_add.html', {'error': '班级名字不能为空'})
        else:
            models.Class.objects.create(name=class_name)
            return redirect('/class_list/')

    return render(request, 'class_add.html')


def class_del(request):
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        pk = request.GET.get('pk')
        models.Class.objects.filter(pk=pk).delete()
        return redirect('/class_list/')


def class_edit(request):
    pk = request.GET.get('pk')
    class_obj = models.Class.objects.get(pk=pk)
    if request.method == 'POST':
        class_name = request.POST.get('class_name')
        class_obj.name = class_name
        class_obj.save()
        return redirect('/class_list/')
    elif request.method == 'GET':
        return render(request, 'class_edit.html', {'class_obj': class_obj})


def student_list(request):
    if request.method == 'GET':
        student_all = models.Student.objects.all()
        return render(request, 'student_list.html', {'student_all': student_all})
    elif request.method == 'POST':
        pass


def student_add(request):
    class_all = models.Class.objects.all()
    if request.method == 'GET':
        return render(request, 'student_add.html', {'class_all': class_all})

    elif request.method == 'POST':
        # 通过获得的class的id去class表中查到相对应的那条class对象，class_obj为对象类型
        student_name = request.POST.get('student_name')
        classs_pk = request.POST.get('class_all')
        class_obj = models.Class.objects.get(pk=classs_pk)
        if not student_name:
            return render(request, 'student_add.html', {'class_all': class_all, 'error': '学生名字不能为空'})
        else:
            models.Student.objects.create(name=student_name, classs=class_obj)
            return redirect('/student_list/')


def student_del(request):
    pk = request.GET.get('pk')
    models.Student.objects.get(pk=pk).delete()
    return redirect('/student_list/')


def student_edit(request):
    class_all = models.Class.objects.all()
    pk = request.GET.get('pk')
    if request.method == 'GET':
        student_obj = models.Student.objects.get(pk=pk)
        return render(request, 'student_edit.html', {'class_all': class_all, 'student_obj': student_obj})
    elif request.method == 'POST':
        student_name = request.POST.get('student_name')
        student_class = request.POST.get('class_all')
        student_obj = models.Student.objects.get(pk=pk)
        student_obj.name = student_name
        student_obj.classs_id = student_class
        student_obj.save()
        return redirect('/student_list/')

def teacher_list(request):
    teacher_all = models.Teacher.objects.all()
    if request.method == 'GET':
        return render(request,'teacher_list.html',{'teacher_all':teacher_all})

    elif request.method == 'POST':
        pass



def teacher_add(request):
    class_all = models.Class.objects.all()
    if request.method == 'GET':
        return render(request, 'teacher_add.html', {'class_all': class_all})
    elif request.method == 'POST':
        subject_name = request.POST.get('subject_name')
        teacher_name = request.POST.get('teacher_name')
        class_id = request.POST.getlist('class_all')
        teacher_obj = models.Teacher.objects.create(name=teacher_name,subject=subject_name)
        teacher_obj.classs.set(class_id)
        return redirect('/teacher_list/')



def teacher_del(request):
    if request.method == 'GET':
        pk = request.GET.get('pk')
        models.Teacher.objects.get(pk=pk).delete()
        return redirect('/teacher_list/')
    elif request.method == 'POST':
        pass

def teacher_edit(request):
    pk = request.GET.get('pk')
    teacher_obj = models.Teacher.objects.get(pk=pk)
    class_all = models.Class.objects.all()
    if request.method == 'GET':
        return render(request,'teacher_edit.html',{'class_all':class_all,'teacher_obj':teacher_obj})
    elif request.method == 'POST':
        teacher_obj.name = request.POST.get('teacher_name')
        teacher_obj.subject = request.POST.get('subject_name')
        teacher_obj.save()
        teacher_obj.classs.set(request.POST.getlist('class_all'))
        return redirect('/teacher_list/')
