from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.shortcuts import render
# Create your views here.
def come_view(request):
    return HttpResponse("Welcome to Django Framework.")

#views for date time
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>IT is now %s </body></html>"%now
    return HttpResponse(html)

def showtime(request):
    now = datetime.datetime.now()
    return HttpResponse("Current Date and Time: " + str(now))

def blog_int(request, id):
    return HttpResponse(f"Integer value: {id}")

def blog_slug(request, name):
    return HttpResponse(f"Slug value: {name}")

def blog_string(request, text):
    return HttpResponse(f"String value: {text}")

def demo(request):
    msg="welcome "
    return render(request, 'home.html',{'msg':msg})

def About(request):
    context={
        'author': 'Mehul',
        'post_title': 'learning Django templates',
        'date': datetime.datetime.now()
    }
    return render(request, "About.html",context)

def post(request):
    posts=[
        {'title': "python Framework",'recent':True},
        {'title': "python Django",'recent':True},
        {'title': "templates",'recent':True},
        {'title':"Migration",'recent':True},
        {'title': "posts",'recent':False},
    ]
    return render(request,'post.html',{'posts':posts})

def base(request):
    return render(request,'base.html')



#prog-13
from django.core.mail import send_mail
from django.conf import settings
from .forms import contactForm

def contact(request):
    context={}
    form=contactForm(None)
    if request.method == 'POST':
        address = request.POST.get('address')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        if address and subject and message:
            try:
                send_mail(subject,message,settings.EMAIL_HOST_USER,[address])
                context['result']="Email sent successfully"
            except Exception as e:
                context['result']="Error sending email:{e}"
        else:
            context['result']="All fields are required"
    return render(request,"contact.html",{'form':form,'context':context})


from django.core.mail import send_mail

def base(request):
    send_mail (
    subject="testing purpose mail",
    message="hi this is console email",
    from_email="rocket.jerry2310@gmail.com",
    recipient_list=["rocket.jerry2310@gmail.com"],
    fail_silently=False,
    )
    return render(request,"base.html")

from .forms import RegistrationForm
from .models import Registration
from django.shortcuts import redirect
def registration(request):
    context={}
    form=RegistrationForm(None)
    if request.method == 'POST':
        nm = request.POST.get('name')
        un = request.POST.get('user_name')
        mno = request.POST.get('mobile_no')
        pw=request.POST.get('password')
        repw=request.POST.get('re_password')
        if nm and un and mno and pw and repw:
            dt=Registration(Name=nm,User_name=un,MobileNo=mno,Password=pw,Re_Password=repw)
            dt.save()
            context["result"]="Data saved Successfully"
            return redirect(registration)
        else:
            context["result"]="All fields Are Required"

    return render (request,"registration.html",{'form':form,'context':context})

from django.shortcuts import redirect
from .forms import Login
from .models import Registration

def login(request):
    context = {}
    form = Login(None)
    if request.method == 'POST':
        un = request.POST.get('User_name')
        pw = request.POST.get('Password')

        if un and pw:
            try:
                user = Registration.objects.get(User_name=un, Password=pw)
                context["result"] = "Login Successful"
                return redirect('home')
            except Registration.DoesNotExist:
                context["result"] = "Invalid Username or Password"
        else:
            context["result"] = "All fields are required"

    return render(request, "login.html", {'form': form, 'context': context})

from django.shortcuts import redirect
from .forms import PostForm
from .models import Post

def post(request):
    context = {}
    form = PostForm(None)
    if request.method == 'POST':
        title = request.POST.get('title')
        slug = request.POST.get('slug')
        content = request.POST.get('content')
        author = request.POST.get('author')
        is_published = request.POST.get('is_published')

        if title and slug and content and author and is_published:
            dt = Post(
                title=title,
                slug=slug,
                content=content,
                author=author,
                is_published=True if is_published == 'True' else False
            )
            dt.save()
            context["result"] = "Post saved successfully"
            return redirect(post)
        else:
            context["result"] = "All fields are required"

    return render(request, "post_form.html", {'form': form, 'context': context})

from django.shortcuts import render, redirect
from .forms import CategoryForm
from .models import Category

def category_view(request):
    context = {}
    form = CategoryForm(None)

    if request.method == 'POST':
        nm = request.POST.get('Name')
        des = request.POST.get('Description')

        if nm and des:
            dt = Category(name=nm, description=des)
            dt.save()
            context["result"] = "Category saved successfully"
            return redirect('category')

        else:
            context["result"] = "All fields are required"

    data = Category.objects.all()

    return render(request, "category.html", {'form': form, 'context': context, 'data': data})

def edit_category(request, id):
    context = {}
    obj = Category.objects.filter(id=id).first()

    if request.method == 'POST':
        nm = request.POST.get('Name')
        des = request.POST.get('Description')

        if nm and des and obj:
            obj.name = nm
            obj.description = des
            obj.save()
            context["result"] = "Category updated successfully"
            return redirect('category')
        else:
            context["result"] = "All fields are required"

    form = CategoryForm(initial={'Name': obj.name, 'Description': obj.description}) if obj else CategoryForm(None)
    data = Category.objects.all()

    return render(request, "category.html", {'form': form, 'context': context, 'data': data})

def delete_category(request, id):
    obj = Category.objects.filter(id=id).first()

    if obj:
        obj.delete()

    return redirect('category')

from .forms import FeedbackForm

def feedback(request):
    form = FeedbackForm()
    data = None

    if request.method == "POST":
        form = FeedbackForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            form = FeedbackForm()

    return render(request, "feedback.html", {"form": form, "data": data})