from django.shortcuts import render, redirect
from django.contrib import messages
from module_1.models import *
from module_1.forms import * 
from django.contrib.auth.hashers import PBKDF2PasswordHasher, Argon2PasswordHasher, CryptPasswordHasher
from base64 import encode
from django.db.models import Q

# Create your views here.
def signup(request):
    if 's_user' in request.session:
        return redirect('module_1:index')

    # ĐĂNG KÝ
    form_signup = FormSignup()
    if request.POST.get('btnSignUp'):
        form_signup = FormSignup(request.POST, User)
        if form_signup.is_valid() and form_signup.cleaned_data['password'] == form_signup.cleaned_data['password_confirm']:
            hasher = Argon2PasswordHasher() # salt: 8 bytes
            request.POST.__mutable = True
            post = form_signup.save(commit=False)
            post.email = form_signup.cleaned_data['email']
            post.password = hasher.encode(form_signup.cleaned_data['password'], '12345678')
            post.save()
            messages.success(request, 'Account created !')
        else:
            messages.error(request, 'Not valid !')
    
    return render(request, 'module_1/signup.html', {
        'form_signup' : form_signup,
    }) 


def login(request):
    if 's_user' in request.session:
        return redirect('module_1:index')

    # ĐĂNG NHẬP
    if request.POST.get('btnLogin'):
        email = request.POST.get('email')
        password = request.POST.get('password')
        hasher = Argon2PasswordHasher()
        encoded = hasher.encode(password, '12345678')

        user = User.objects.filter(email=email, password=encoded)
        if user.count() > 0:
            # Tạo session
            request.session['s_user'] = user.values()[0]
            return redirect('module_1:index')
        else:
            messages.error(request, 'Not valid !')
    
    return render(request, 'module_1/login.html', {
    }) 
    

def index(request):
    if 's_user' not in request.session:
        return redirect('module_1:login')
    
    list_of_rifles = Rifle.objects.filter()
    
    return render(request, 'module_1/template1.html', {
        'list_of_rifles' : list_of_rifles,
    })    

def create_rifle(request):
    if 's_user' not in request.session:
        return redirect('module_1:login')
    
    frm_create_rifle = FormCreateRifle()
    if request.POST.get('btncreaterifle'):
        frm_create_rifle = FormCreateRifle(request.POST, Rifle)
        if frm_create_rifle.is_valid():
            post = frm_create_rifle.save(commit=False)
            post.name = frm_create_rifle.cleaned_data['name']
            post.place_of_origin = frm_create_rifle.cleaned_data['place_of_origin']
            post.save()
            messages.success(request, 'Data created !')
        else:
            messages.error(request, 'Not valid !')

    
    return render(request, 'module_1/create_rifle.html', {
        'frm_create_rifle' : frm_create_rifle,
    })
    

def create_author_and_book(request):
    if 's_user' not in request.session:
        return redirect('module_1:login')
    
    # Create author
    formauthor = FormAuthor()
    if request.POST.get('btncreateauthor'):
        formauthor = FormAuthor(request.POST)
        if formauthor.is_valid():
            # Save info to DB
            request.POST.__mutable = True
            post = formauthor.save(commit=False)
            post.save()
            messages.success(request, 'Data created !')
        else:
            print(formauthor.errors.as_data())
            messages.error(request, str(formauthor.errors.as_data()))
        return redirect('module_1:create_author_and_book')

    # Create book
    formbook = FormBook()
    if request.POST.get('btncreatebook'):
        formbook = FormBook(request.POST)
        if formbook.is_valid():
            # Save info to DB
            request.POST.__mutable = True
            post = formbook.save(commit=False)
            post.save()
            messages.success(request, 'Data created !')
        else:
            print(formbook.errors.as_data())
            messages.error(request, str(formbook.errors.as_data()))
        return redirect('module_1:create_author_and_book')

    
    return render(request, 'module_1/create_author_and_book.html', {
        'formauthor' : formauthor,
        'formbook' : formbook,
    })


def view_book(request):
    if 's_user' not in request.session:
        return redirect('module_1:login')
    
    list_of_books = Book.objects.filter()
    
    
    list_author = Author.objects.all()
    if request.POST.get('btnfilterbook'):
        author_id = request.POST.get('author_id')
        if author_id != '0':
            q = ((Q(author=author_id)))
            list_of_books = Book.objects.filter(q)
        elif author_id == '0':
            list_of_books = Book.objects.filter()
    
    return render(request, 'module_1/view_book.html', {
        'list_of_books' : list_of_books,
        'list_author' : list_author,
    })    

    