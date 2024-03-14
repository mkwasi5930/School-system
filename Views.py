from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import StudentForm
from .models import Student

@login_required
def student_detail(request):
    student = request.user.student
    return render(request, 'student_detail.html', {'student': student})

@login_required
def edit_student(request):
    student = request.user.student
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_detail')
    else:
        form = StudentForm(instance=student)
    return render(request, 'edit_student.html', {'form': form})
 
