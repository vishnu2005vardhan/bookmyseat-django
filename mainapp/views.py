from .forms import StudentForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Student

@login_required(login_url='/login/')
def student_list(request):
    students = Student.objects.filter(user=request.user)
    return render(request, 'mainapp/student_list.html', {
        'students': students
    })


@login_required(login_url='/login/')
def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)

        if form.is_valid():
            student = form.save(commit=False)
            student.user = request.user
            student.save()
            return redirect('/')

    else:
        form = StudentForm()

    return render(request, 'mainapp/add_student.html', {
        'form': form
    })



@login_required(login_url='/login/')
def edit_student(request, id):
    student = Student.objects.get(id=id, user=request.user)

    if request.method == "POST":
        name = request.POST.get('name')
        age = request.POST.get('age')
        course = request.POST.get('course')

        # ✅ SAFETY CHECK
        if not name:
            return render(request, 'mainapp/edit_student.html', {
                'student': student,
                'error': 'Name cannot be empty'
            })

        student.name = name
        student.age = age
        student.course = course
        student.save()

        return redirect('/')

    return render(request, 'mainapp/edit_student.html', {
        'student': student
    })

@login_required(login_url='/login/')
def delete_student(request, id):
    student = Student.objects.get(id=id, user=request.user)
    student.delete()
    return redirect('/')


from django.contrib.auth.models import User
from django.shortcuts import render, redirect
def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # 🔐 SAFETY CHECK (this MUST run before create_user)
        if User.objects.filter(username=username).exists():
            return render(request, 'mainapp/signup.html', {
                'error': 'Username already exists'
            })

        user = User.objects.create_user(
            username=username,
            password=password
        )
        user.save()

        return redirect('/login/')

    return render(request, 'mainapp/signup.html')

    


from django.contrib.auth import authenticate, login
def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'mainapp/login.html', {
                'error': 'Invalid credentials'
            })

    return render(request, 'mainapp/login.html')
from django.contrib.auth import logout

def user_logout(request):
    logout(request)
    return redirect('/login/')
from django.contrib.auth import logout

