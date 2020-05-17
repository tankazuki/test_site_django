from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from config import settings
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from app01.forms import MemoForm, SignUpForm
from app01.models import Memo, Like


class ListMemoView(CreateView):
    model = Memo
    form_class = MemoForm
    template_name = 'app01/index.html'
    success_url = reverse_lazy('app01:index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ListMemoView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['memo_list'] = Memo.objects.all()
        return context


class DetailMemoView(DetailView):
    model = Memo
    template_name = 'app01/detail.html'


class SignUpView(CreateView):
    def post(self, request,  *args, **kwargs):
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            print('password_dubug')
            print(password)
            user = authenticate(username=username, email=email, password=password)
            login(request, user)
            return redirect('/app01/')
        return render(request, 'app01/signup.html', {'form': form})

    def get(self, request, *args, **kwargs):
        form = SignUpForm()
        return render(request, 'app01/signup.html', {'form': form})

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.object = user
        return HttpResponseRedirect(self.get_success_url())


def add_like(request, pk):
    memo = get_object_or_404(Memo, pk=pk)
    user = request.user

    if request.method == 'POST':
        like = Like.objects.create(memo=memo, user=user)
        like.save()
        message = '登録に成功しました'
        response = {
            'count': Like.objects.filter(memo=memo).count(),
            'message': message
        }
        return JsonResponse(response)



