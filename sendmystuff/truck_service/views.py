from django.shortcuts import render, redirect

from .models import FormOne, FormTwo


def home(request):
    return render(request, 'front/home.html')


def src_dst(request):
    if request.method == "POST":
        # src = request.POST.get('src_city', '')
        # dst = request.POST.get('drop_city', '')
        # tmp = City.objects.filter(city_name=src)
        # if tmp == None or tmp == '':
        #     return render(request, 'front/home.html')
        #
        # tmp = City.objects.filter(city_name=dst)
        # if tmp == None or tmp == '':
        #     return render(request, 'front/home.html')
        #
        # request.session['src'] = src
        # request.session['dst'] = dst
        pass
        return redirect("/form_one")
    elif request.method == "GET":
        return render(request, 'front/home.html')
    else:
        return render(request, 'front/home.html')


def form_one(request):
    if request.method == "POST":
        # weight = request.POST.get('material_weight', '')
        # length = request.POST.get('material_length', '')
        # width = request.POST.get('material_width', '')
        # height = request.POST.get('material_height', '')
        # date = request.POST.get('date', '')
        #
        # content = FormOne(weight=weight, length=length, width=width, height=height, date=date)
        # content.save()
        return redirect('/form_two')
    return render(request, "front/form.html")


def form_test(request):
    if request.method == "POST":
        pass
        return redirect("/form_two")
    return render(request, "front/form2.html")


    #     print("test")
    #     name = request.POST.get('name', '')
    #     email = request.POST.get('email', '')
    #     phone = request.POST.get('phone', '')
    #     otp = request.POST.get('otp', '')
    #
    #     if otp == None or otp == '':
    #         pass
    #
    #     content = FormTwo(name=name, email=email, phone=phone, otp=otp)
    #     content.save()
    #     return redirect('/form2')
    # return render(request, "front/form2.html")

