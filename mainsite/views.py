from django.contrib.auth import login
from django.db.models import query
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from django.contrib.messages.api import error
import requests as rqt
import json
from .models import Favorite
from .models import User
from .models import Movie

# Create your views here.
def index(request):
    return render(request, 'mainsite/index.html', )

def register(request):
    if(request.method == "POST"):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user)
            return redirect("/")

        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

            return render(request = request,
                          template_name = "mainsite/register.html",
                          context={"form":form})


    form = UserCreationForm
    return render(request=request,
                template_name="mainsite/register.html",
                context={"form":form})

def logout_request(request):
    logout(request)
    messages.info(request, "Logged Out successfully!")
    return redirect("mainsite")


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                messages.success(request, f"New account created: {username}")
                return render(request=request,
                            template_name='mainsite/user.html',
                            context= {"username": username})
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")


    form = AuthenticationForm()
    return render(request = request,
                template_name="mainsite/login.html",
                context={"form":form})

#def filtered(ans):
    m = []
    j=0
    for i in range(len(ans)):
        if ans[i]["backdrop_path"]==None:
            continue
        m.append({})
        m[j]["movie_id"]=ans[i]["id"]
        m[j]["movie_image"]=ans[i]["backdrop_path"]
        m[j]["movie_name"]=ans[i]["title"]
        m[j]["movie_date"]=ans[i]["release_date"][0:4]
        m[j]["movie_rating"]=ans[i]["vote_average"]
        j+=1
    return m



#def user(request):
    act = rqt.get("https://api.themoviedb.org/3/search/movie?api_key=4be8a61c04069692ec71d744ddc0b88f&query=${query}")
    if act.status_code!=200:
        return HttpResponse("Request Failed!")
    ans = json.loads(act.text)['results']
    m = list(filtered(ans))
    fav=[]
    #fav = [i.movie_id for i in obj]
    return render(request, 'mainsite/user.html', {"content":m,
                                                "clear":False,
                                                "val":"",
                                                "fav":fav})

#def sent(request):
    query = request.GET['query']
    if query == "":
        return redirect('/')
    result = json.loads(rqt.get("https://api.themoviedb.org/3/search/movie?api_key=4be8a61c04069692ec71d744ddc0b88f&query="+query).text)['results']
    l = list(filtered(result))
    fav = []
    return render(request,
                'mainsite/user.html',
                {"content": l,
                "clear":True,
                "val":query,
                "fav":fav})
