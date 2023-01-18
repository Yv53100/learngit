from django.shortcuts import render

from app01.models import UserInfo


# Create your views here.
def users(request):
    user_name = "XXX"
    return render(request, "page.html", {"name": user_name})


def login(request):
    user_name = ""
    if request.method == "GET":
        return render(request, "loginpage.html")
    elif request.method == "POST":
        account = request.POST.get("username")
        password = request.POST.get("passwordText")
        datalist = UserInfo.objects.all()
        account_flag = 0
        for obj in datalist:
            if account == obj.account:
                account_flag = 1
                correct_password = obj.password
                user_name = obj.user_name
                break
        if account_flag:
            if password == correct_password:
                return render(request, "page.html", {"name": user_name})
            return render(request, "loginpage.html", {"error_tip": "您提供的用户名或者密码有误"})
