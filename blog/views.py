from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.views import View
from .models import Student, Hobby
from .forms import LoginForm, RegisterForm
from django.contrib.auth.models import User
from .forms import StudentForm

class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', context={"form":form})

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('register')
        
        form = LoginForm()
        return render(request, 'login.html', context={"form":form})
    

class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'register.html', context={"form":form})

    def post(self, request):
        username = request.POST['username']
        fisrt_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            user = User()

            user.username = username
            user.first_name = fisrt_name
            user.last_name = last_name
            user.email = email
            user.set_password(password)
            user.save()

            user.set_password(password)
            return redirect('data')

        form = RegisterForm()
        return render(request, 'register.html', context={"form":form})
        
def data(request):
    data = User.objects.all()
    return render(request, 'data_base.html', context={"data":data})

def read_data(request, id):
    data = User.objects.get(id=id)
    return render(request, 'read_data.html', context={"data":data})

def delete_data(request, id):
    data = get_object_or_404(User, id=id)
    data.delete()

    return redirect('data/')

# def profile(request, id):
#     student=Student.objects.get(id=id)
#     hobby=student.hobby.all()
#     return render(request, 'profile.html', context={"student", student})

def profile(request, id):
    student=Student.objects.get(id=id)
    hobby=student.hobby.all()
    return render(request, 'profile.html', context={"student":student})



def update(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('profile', id=student.id)
    else:
        form = StudentForm(instance=student)

    return render(request, 'update.html', context={'student': student, 'form': form})