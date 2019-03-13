from django.shortcuts import render
from Register.forms import regist_form
from Register.models import user_info

def home(request):
    return render(request, 'home.html')


def add(request):
    form = regist_form()
    if request.POST:
        f = regist_form(request.POST)
        if f.is_valid():
            if 'submit' in request.POST:
                user_info = user_info()
                user_info.id_card = request.POST['id_card']
                user_info.user_name = request.POST['username']
                user_info.phone_number = request.POST['phone_number']
                try:
                    user_info.save()
                    return render(request, 'result.html', {'form': '注册成功'})
                except Exception as e:
                    raise e
            else:
                return render(request, 'result2.html',
                              {'form': '注册失败，已存在用户'})
    return render(request, 'post.html', {'form': form})