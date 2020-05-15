from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from app01.forms import MemoForm
from app01.models import Memo


def index(request):
    return HttpResponse('aaaaaaaaaa')


class ListMemoView(CreateView):
    model = Memo
    form_class = MemoForm
    template_name = 'app01/index.html'
    success_url = reverse_lazy('app01:index')

    def form_valid(self, form):
        result = super().form_valid(form)
        messages.success(
            self.request, '保存に成功しました'
        )
        return result

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['memo_list'] = Memo.objects.all()
        return context


class DetailMemoView(DetailView):
    model = Memo
    template_name = 'app01/detail.html'






