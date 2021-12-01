from django.shortcuts import render
from . import forms
from django.db.models import Q
from django.views.generic import TemplateView, ListView
from django.shortcuts import render,redirect
from formapp.models import NewForm
from .forms import ContentForm
from django.contrib import messages

class AddView(TemplateView):
    template_name = 'add.html'

class HomeView(TemplateView):
    template_name = 'home.html'

def show(request):
    students = NewForm.objects.all()
    phone = students[len(students)-1].phone
    fname = students[len(students)-1].first_name
    sname = students[len(students)-1].last_name
    email = students[len(students)-1].email
    addr = students[len(students)-1].address
    zipcode = students[len(students)-1].zipcode
    print("Forgot")
    return render(request,"profile.html",{'phone':phone, 'fname':fname, 'sname':sname, 'email':email, 'addr':addr, 'zipcode':zipcode})

def search_show(request):
    students = NewForm.objects.all()
    return render(request,"profile.html",{'student':students})

def post(request ):                                                                                             
    post_list = Post.objects.order_by('id')
    form = ContentForm()
    return render(request, 'posts/success.html',
        {'post': post_list,
        'form':form},
    )                                                                                                           
def content_get(request):
    if request.method == 'POST':
        form=ContentForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

def get_question(request):
    form = forms.ContentForm()

    if request.method == 'POST':
        form = forms.ContentForm(request.POST)
        if form.is_valid():
            saved_instance = form.save(commit=True)
            
    else:
        form = forms.ContentForm()

    return render(request, 'success.html', { 'form': ContentForm(instance=saved_instance) })

class SearchResultsView(ListView):
     model = NewForm
     template_name = 'search_results.html'

     def get_queryset(self): # new
         query = self.request.GET.get('q')
         object_list = NewForm.objects.filter(
             Q(first_name__icontains=query) | Q(last_name__icontains=query) 
         )
         print("Object", object_list.last())
         return object_list.last()

def my_form(request):
    saved_instance = None
    if request.method == "POST":
        form = ContentForm(request.POST)
        if form.is_valid():
            saved_instance = form.save(commit=True)
            messages.success(request, 'Student Added!')
    else:
        form = ContentForm()
    return render(request, 'add.html', {'form':  ContentForm(instance=saved_instance)})
