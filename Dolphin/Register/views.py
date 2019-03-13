from django.shortcuts import render
from .forms import regist_form
from .models import user_info

def home(request):
    return render(request, 'home.html')


def add(request):
    form = regist_form()
    if request.POST:
        f = regist_form(request.POST)
        if f.is_valid():
            if 'submit' in request.POST:
                user = user_info()
                user.id_card = request.POST['id_card']
                user.user_name = request.POST['user_name']
                user.phone_number = request.POST['phone_number']
                try:
                    user.save(force_insert=True)
                    return render(request, 'result.html', {'form': '注册成功'})
                except Exception as e:
                    raise e
            else:
                return render(request, 'result2.html',
                              {'form': '注册失败，已存在用户'})
    return render(request, 'post.html', {'form': form})