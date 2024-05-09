from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from .forms import*
from .models import*

# def login_view(request):
#     if request.method == 'POST':
#         # Handle form submission
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         remember_me = request.POST.get('remember_me')  # Check if remember me checkbox is checked
        
#         # Perform authentication (replace this with your authentication logic)
#         # If authentication is successful, store login date and time in session
#         if username == 'example' and password == 'password':
#             request.session['login_datetime'] = timezone.now()
#             messages.success(request, 'Login successful!')
            
#             # Redirect user to dashboard or any other page
#             return redirect('dashboard')
#         else:
#             messages.error(request, 'Invalid username or password.')
    
#     return render(request, 'login.html')




# def dashboard_view(request):
#     login_datetime = request.session.get('login_datetime')  # Retrieve login date and time from session
#     if login_datetime:
#         # Display login date and time in dashboard
#         login_datetime_str = login_datetime.strftime('%Y-%m-%d %H:%M:%S')
#         context = {'login_datetime': login_datetime_str}
#     else:
#         context = {'login_datetime': 'N/A'}
    
#     return render(request, 'dashboard.html', context)

def home(request):
    context={}
    context['form']=UserForm
    return render(request, 'home.html' , context)

def register(request):
    name=request.POST.get('Name')
    email=request.POST.get('Email')
    number=request.POST.get('Number')
    password=request.POST.get('Password')
    con_password=request.POST.get('Con_Password')
    RegistrationModel.objects.create(
        Name=name,
        Email=email,
        Number= number,
        Password=password,
        Con_Password=con_password    
        )
    msg="Registration Successfully Done"
    return render(request, 'login.html', {'key':msg}) 

def display(request):
    data=RegistrationModel.objects.all()
    
    return render(request, 'login.html', {'key1': data})