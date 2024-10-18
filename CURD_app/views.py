from django.shortcuts import render,redirect
from . forms import Employee_form
from . models import Employee

# Create your views here.
def retrive(request):
    data=Employee.objects.all()
    my_dict={'data':data}
    return render(request,'retrive.html', context=my_dict)
def creating(request):
    form=Employee_form()
    if request.method =='POST':
        form =Employee_form(request.POST)
        if form.is_valid():
            form.save(commit= True)
        return redirect("/")
    return render(request,'Create.html',context={'form':form})
def update(request,id):
    data=Employee.objects.get(id=id)
    if request.method =='POST':
        data = Employee_form(request.POST,instance=data)
        if data.is_valid():
            data.save(commit=True)
        return redirect("/")
    return render(request,'update.html',context={'data':data})
def deleting(request,id):
    data=Employee.objects.get(id=id)
    data.delete()
    return redirect("/")