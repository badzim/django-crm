from django.shortcuts import render, redirect;
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, CreateRecordForm
from .models import Record

# Create your views here.
def home(request):
    # Check to see if logging in
    if request.user.is_authenticated:
        # Filtrer les enregistrements par utilisateur connecté
        record = Record.objects.filter(created_by=request.user)
    else:
        record = Record.objects.none()

    
    if request.method == 'POST':
        username1 = request.POST['username1']
        password1 = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username1, password=password1)
        if user is not None:
            login(request, user)
            messages.success(request, "You Have Been Logged In!")
            return redirect('home')
        else:
            messages.success(request, "There Was An Error Logging in")
            return redirect('home')
    return render(request, 'home.html', {'records':record})

def login_user(request):
    pass

def logout_user(request):
    logout(request)
    messages.success(request, "You Have Been Logged Out ...")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, "You Have Successfully Registered, Welcome !")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})
    return render(request, 'register.html', {'form': form})


def customer_record(request, pk):
    if request.user.is_authenticated:
        # Look Up Records
        customer_record = Record.objects.get(id=pk)
        if (customer_record.created_by == request.user):
            return render(request, 'record.html', {'customer_record':customer_record})
        else:
            messages.success(request, "You Are Not Allowed To View This Record")
            return redirect('home')   
            
    else:
        messages.success(request, "You Need To Be Authenticated To View This Record")
        return redirect('home')        
    
def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        if (delete_it.created_by == request.user):
            delete_it.delete()
            messages.success(request, "Record Deleted Successfully !")
        else:
            messages.success(request, "You Are Not Allowed To Delete This Record")
            return redirect('home')   
    else:
        messages.success(request, "You Need To Be Logged In To Do This Action !")
    return redirect('home')


def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        if (current_record.created_by == request.user):
            form = CreateRecordForm(request.POST or None, instance=current_record)
            if (request.method == 'POST'):
                if form.is_valid():
                    form.save()
                    messages.success(request, "Record Updated Successfully !")
                    return redirect('home')
            else:
                return render(request, 'update_record.html', {'form':form})
        else:
            messages.success(request, "You Are Not Allowed To Update This Record")
            return redirect('home')   
    else:
        messages.success(request, "You Need To Be Logged In To Do This Action !")
    return redirect('home')


def add_record(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CreateRecordForm(request.POST)
            if form.is_valid():
                record = form.save()
                record.created_by = request.user
                record.save()
                messages.success(request, "Record Added Successfully !")
                return redirect('home')
            else:
                messages.success(request, "Form Invalid !") 


        else:
            form = CreateRecordForm()
            return render(request, 'add_record.html', {'form':form})
    else:
        messages.success(request, "You Need To Be Logged In To Do This Action !")
    return redirect('home')