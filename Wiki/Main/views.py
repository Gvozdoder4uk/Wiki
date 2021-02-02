from django.shortcuts import render


# Create your views here.


def index(request):
    if request.user_agent.is_mobile:
        is_mobile = True
    else:
        is_mobile = False
    context = {'is_mobile': is_mobile}
    return render(request, template_name="Main_Templates/main.html", context=context)
