import json

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import JsonResponse, HttpResponse


from .models import CustomUser
from .forms import LoginForm


class MainView(View):

    def get(self, request):
        return render(request, 'base.html')


class LoginView(View):

    def get(self, request):
        context = {'form': LoginForm}
        return render(request, 'login.html', context)

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['email'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('profile')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')


class SignUpView(View):

    def post(self, request):
        data = json.loads(request.body)
        try:
            user = CustomUser.objects.get(telegram_user_id=data['telegram_user_id'])
            response = {
                'message': 'Вы уже зарегистрированы',
                'email': user.email
            }
            return JsonResponse(response, status=400, safe=False)
        except CustomUser.DoesNotExist:
            CustomUser.objects.create_user(**data)
        return JsonResponse({'message': 'Вы успешно зарегистрировались'}, status=201, safe=False)


class UserInfo(LoginRequiredMixin, View):
    def get(self, request):
        context = {
            'user': request.user
        }
        return render(request, 'profile.html', context)


