from django.shortcuts import render

# Create your views here.
import pandas as pd


def index(request):
    if request.method == "POST":
        guess = request.POST["answer"]

    else:
        return render(request, "chinesepracticeapp1/index.html", {})

def readexcel():
    
    df = pd.read_excel('Characters.xlsx')


"""
def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")
"""