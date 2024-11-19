# # views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from .models import Student
from .forms import StudentForm  # assuming we have a form created for Student model
from django.urls import reverse
from .forms import StudentForm
from .serializers import StudentSerializer
from rest_framework.parsers import JSONParser
from django.db.models import Min,Max,Avg

# List all students
# def student_list(request):  #get api
#     students = Student.objects.all()
#     #fetch students whose age is greater than 18
#     student_over_18 = Student.objects.filter(age__gt=18)
#     #fetch student whose age is less than 20
#     student_under_20 = Student.objects.filter(age__lt = 20)
#     #get the student with the minimum age
#     yougest_student = Student.objects.all().aggregate(min_age = Min('age'))
#     #get the student with the maximum age
#     oldest_student = Student.objects.all().aggregate(max_age = Max('age'))
#     #get the average age of all the students
#     average_age = Student.objects.all().aggregate(average_age = Avg('age'))
#     #count the total number of students in the database 
#     total_students = Student.objects.count()
#     #order the students age in the ascending order
#     students_order_by_age = Student.objects.all().order_by('age')
#     #oreder the students age in descending order
#     student_order_by_desc = Student.objects.all().order_by('-age')
#     #fetch distict ages of student 
#     distinct_ages = Student.objects.values('age').distinct()
#     #perform muiltiple aggregate functions
#     # aggregates = Student.objects.aggregate(
#     #     min_age = Min('age'),
#     #     max_age = Max('age'),
#     #     average_age = Avg('age'),
#     # )
#     context = {
#         'students': students,
#         'student_over_18': student_over_18,
#         'student_under_20':student_under_20,
#         'yougest_student': yougest_student,
#         'oldest_student':oldest_student,
#         'average_age':average_age,
#         'total_students':total_students,
#         'students_order_by_age':students_order_by_age,
#         'student_order_by_desc':student_order_by_desc,
#         'distinct_ages':distinct_ages
#     }
#     return render(request, 'student_list.html',context)


# #create api

# def StudentCreate(request):
#     if request.method == 'POST':
#         form = StudentForm(request.POST)
#         if form.is_valid():
#             form.save()    
#         return redirect('student_list')
#     else:
#         form = StudentForm()
#     return render(request,'student_form.html',{'form':form})


# #update
# def student_update(request,id):
#     student = get_object_or_404(Student,id = id)
#     if request.method == 'POST':
#         form = StudentForm(request.POST,instance = student)
#         if form.is_valid():
#             form.save()
#         redirect('student_list')
#     else:
#         form = StudentForm(instance = student)
#     return render(request,'student_form.html',{'form':form})

# def student_delete(request,id=id):
#     student = get_object_or_404(Student,id=id)
#     if request.method == 'POST':
#         student.delete()
#         return redirect('student_list')
#     return render(request,'student_delete.html',{'student':student})


#class based views
#Listview
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

class student_list(ListView):
    model = Student
    template_name = 'student_list.html'
    context_object_name = 'students'
    
#create api 

class StudentCreate(CreateView):
    model = Student 
    form_class = StudentForm 
    template_name = "student_form.html"
    success_url = reverse_lazy('student_list')
    
class StudentUpdate(UpdateView):
    model = Student 
    form_class = StudentForm 
    template_name = 'student_form.html'
    success_url = reverse_lazy('student_list')
    
class StudentDelete(DeleteView):
    model = Student 
    template_name = 'student_delete.html'
    success_url = reverse_lazy('student_list')
    
