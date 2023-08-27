from django.shortcuts import render ,HttpResponse
from django.views import View
from .froms import LoginForm
from django.contrib.auth import login , logout , authenticate
from django.contrib.auth.models import AnonymousUser

# Create your views here.
class LoginView(View):
    from_class = LoginForm

    def post(self , req , *args,**kwargs):
        form = self.from_class(data = req.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(req , username = username , password = password)
            if user is not None :
                login(req , user)
                return HttpResponse("""
                                    <h1 style=' position: absolute;
                                                top: 50%;
                                                left: 50%;
                                                transform: translate(-50%, -50%);'
                                    >
                                        you're in 🌴VALHALA🌴
                                    </h1>""") 
            else:
                print('🔴 sth wrong')
                return HttpResponse("""
                                    <h1 style=' position: absolute;
                                                top: 50%;
                                                left: 50%;
                                                transform: translate(-50%, -50%);'
                                    >
                                        YOU SHALL NOT PASS 🧙‍♂️
                                    </h1>
                                    """)
        else:
            return HttpResponse("form is not valid ")
    

    def get(self , req , *args,**kwargs):
        form = self.from_class()
        context = {"form":form}
        return render(req, "login.html", context )
    

class LogoutView(View):
    def get(self , req , *args,**kwargs):
        user = req.user
        if isinstance(user , AnonymousUser ):
            return HttpResponse("you must login first")
        else:
            logout(req)
            return HttpResponse("you successfully logged out")
    
    
class ProtectedView(View):
    def get(self , req , *args,**kwargs):
        return HttpResponse("protected view")