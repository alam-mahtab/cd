from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from .models import Schedule, Highlight, Schedule2, Schedule3, User_Data
from django.contrib import messages
from django.contrib.auth.models import User, auth





# Create your views here.
def film_festival(request):
    # higli1 = Highlight()
    # higli1.image = "1.jpg"
    # higli1.work = "Comedy"
    # higli1.worktype = "Finding Success "
    # higli1.description = " Grow Your Social Following"

    # higli2 = Highlight()
    # higli2.image = ""
    # higli2.work = "Comedy"
    # higli2.worktype = " Success "
    # higli2.description = " Social Following"

    # higli3 = Highlight()
    # higli3.image = "1.jpg"
    # higli3.work = "Thrill"
    # higli3.worktype = "Finding Work "
    # higli3.description = "Your Social Following"

    # higli4 = Highlight()
    # higli4.image = ""
    # higli4.work = "Comedy"
    # higli4.worktype = "Finding Success "
    # higli4.description = " Grow Your Social Following"

    # higli5 = Highlight()
    # higli5.image = "1.jpg"
    # higli5.work = "Comedy"
    # higli5.worktype = "Finding Success "
    # higli5.description = " Grow Your Social Following"

    # higli6 = Highlight()
    # higli6.image = ""
    # higli6.work = "Comedy"
    # higli6.worktype = "Finding Success "
    # higli6.desc = " Grow Your Social Following"

    # high =[higli1, higli2, higli3, higli4, higli5, higli6]
    high = Highlight.objects.all()

    About = "This is the about content"
    return render(request, 'film-festival.html', {'About':About, 'high' : high})

def signup_submission(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    dateofbirth = request.POST['dateofbirth']
    CD_Id = request.POST['CD_Id']
    #username = request.POST['username']
    phone = request.POST['phone']
    email = request.POST['email']
    password = request.POST['password']
    confirm_password =request.POST['confirm_password']


    if password == confirm_password:
        if User_Data.objects.filter(email=email).exists():
            messages.info(request, 'This Email id s already exists')
            #print('email exists')
        elif User_Data.objects.filter(CD_Id=CD_Id).exists():
            messages.info(request, 'This ID is already taken')
            #print('This ID is already taken')
        else:
            user_data = User_Data(password=password,email=email,first_name=first_name,last_name=last_name,dateofbirth=dateofbirth,CD_Id=CD_Id,phone=phone)
            user_data.save();
            return render(request, 'sign_in.html')
    else:
        messages.info(request, 'Password not matching')
        print('password not matching')


def signup(request):
    # if request.method == 'POST':
    #     first_name = request.POST['first_name']
    #     last_name = request.POST['last_name']
    #     dateofbirth = request.POST['dateofbirth']
    #     username = request.POST['username']
    #     phone = request.POST['phone']
    #     email = request.POST['email']
    #     password = request.POST['password']
    #     confirm_password =request.POST['confirm_password']

    #     if password == confirm_password :
    #         if User.objects.filter(username=username).exists():
    #             print('username taken')
    #             return redirect('signup')
    #         elif User.objects.filter(email=email).exists():
    #             print('email already registered')
    #             return redirect('signup')
    #         else:
    #             #user = User_Data.objects.create_user(request.POST)
    #             user = User(password=password,email=email,first_name=first_name,last_name=last_name,dateofbirth=dateofbirth,username=username,phone=phone)
    #             user.save();
    #             print('user created')
    #             return redirect('/')
    #     else:
    #         print("Password not matching")
    #         return redirect('signup')

    # else:
    return render(request, 'sign_up.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        #user_data = User_Data.objects.all()
        user_data = authenticate(request, email=email, password=password)
        if user_data is not None:
            login(request, user_data)
            print('authentication done')
            return render(request, 'film-festival.html')
            #return HttpResponse()
        else:
            print('invalid')
            
            messages.info(request, 'Invalid Credential')
            return render(request,'schedule')
            #return HttpResponse()
    else:
        return render(request, 'sign_in.html')

def forgetpassword(request):
    return render(request, 'forget-password.html')
def schedule(request):
    # sch1 = Schedule()
    # sch1.img = '1.jpg'
    # sch1.type = 'Film'
    # sch1.title = 'Find Success There'
    # sch1.desc = 'GrowYour Social'

    # sch2 = Schedule()
    # sch2.img = ''
    # sch2.type = 'Writer'
    # sch2.title = ' Success There'
    # sch2.desc = 'Your Social'

    # sch3 = Schedule()
    # sch3.img = ''
    # sch3.type = 'Director'
    # sch3.title = 'Find There'
    # sch3.desc = 'Grow Social'

    # sch4 = Schedule()
    # sch4.img = ''
    # sch4.type = 'lightman'
    # sch4.title = 'Find Success '
    # sch4.desc = 'Grow Your '

    # sch5 = Schedule()
    # sch5.img = ''
    # sch5.type = 'Film'
    # sch5.title = 'Find Success There'
    # sch5.desc = 'GrowYour Social'

    # sch6 = Schedule()
    # sch6.img = ''
    # sch6.type = 'Music'
    # sch6.title = 'Find Success There'
    # sch6.desc = 'GrowYour Social'

    # sch7 = Schedule()
    # sch7.img = '1.jpg'
    # sch7.type = 'Film Director'
    # sch7.title = 'Find Success There'
    # sch7.desc = 'GrowYour Social'

    # sch8 = Schedule()
    # sch8.img = ''
    # sch8.type = 'Writer'
    # sch8.title = ' Success There'
    # sch8.desc = 'Your Social'

    # sch9 = Schedule()
    # sch9.img = '1.jpg'
    # sch9.type = 'Director'
    # sch9.title = 'Find There'
    # sch9.desc = 'Grow Social'

    # sch10 = Schedule()
    # sch10.img = ''
    # sch10.type = 'lightman'
    # sch10.title = 'Find Success '
    # sch10.desc = 'Grow Your '

    # sch11 = Schedule()
    # sch11.img = ''
    # sch11.type = 'Film'
    # sch11.title = 'Find Success There'
    # sch11.desc = 'GrowYour Social'

    # sch12 = Schedule()
    # sch12.img = ''
    # sch12.type = 'Music'
    # sch12.title = 'Find Success There'
    # sch12.desc = 'GrowYour Social'

    # sch13 = Schedule()
    # sch13.img = '1.jpg'
    # sch13.type = 'Business'
    # sch13.title = 'Find Success There'
    # sch13.desc = 'GrowYour Social'

    # sch14 = Schedule()
    # sch14.img = ''
    # sch14.type = 'Writer'
    # sch14.title = ' Success There'
    # sch14.desc = 'Your Social'

    # sch15 = Schedule()
    # sch15.img = '1.jpg'
    # sch15.type = 'Director'
    # sch15.title = 'Find There'
    # sch15.desc = 'Grow Social'

    # sch16 = Schedule()
    # sch16.img = ''
    # sch16.type = 'Business'
    # sch16.title = 'Find Success '
    # sch16.desc = 'Grow Your '

    # sch17 = Schedule()
    # sch17.img = '1.jpg'
    # sch17.type = 'Film'
    # sch17.title = 'Find Success There'
    # sch17.desc = 'GrowYour Social'

    # sch18 = Schedule()
    # sch18.img = ''
    # sch18.type = 'Music'
    # sch18.title = 'Find Success There'
    # sch18.desc = 'GrowYour Social'

    # schs = [sch1,sch2,sch3,sch4,sch5,sch6]  # Schedule Day 1
    # schds = [sch7,sch8,sch9,sch10,sch11,sch12]  # Schedule Day 2
    # schdes = [sch13,sch14,sch15,sch16,sch17,sch18]  # Schedule Day 3
    schs = Schedule.objects.all()
    schds = Schedule2.objects.all()
    schdes = Schedule3.objects.all()

    return render(request, 'schedule.html', {'schs' : schs, 'schds' : schds, 'schdes' : schdes})
