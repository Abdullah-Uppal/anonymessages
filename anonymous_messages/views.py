from typing import List

from django.contrib.auth import login
from anonymous_messages.models import AnonymousMessage
from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from django.views.generic import *
from django.urls import reverse_lazy, reverse
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
import uuid

# Create your views here.


class URLCreateView(CreateView):
    model = URL
    form_class = URLCreationForm

    def get_success_url(self) -> str:
        return JsonResponse({
            'message': 'success',
        })

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

@login_required
def home(request):
    form = URLCreationForm()
    if request.is_ajax():
        form = URLCreationForm(request.POST)
        form.instance.user = request.user
        if (form.is_valid()):
            form.save()
            return JsonResponse({
                'message': 'success'
            })
    return render(request, 'home.html', {'form': form})

class URLListView(LoginRequiredMixin, ListView):
  model = URL
  template_name = 'links.html'
  ordering = ['-time_created'] 
  context_object_name = 'urls'

  def get_queryset(self):
      return URL.objects.filter(user=self.request.user)
@login_required
def delete_message(request, id):
    try:
        obj = AnonymousMessage.objects.get(id=id)
        obj.delete()
    except:
        return JsonResponse({'message':'null'})
    return JsonResponse({'message':'deleted'})
@login_required
def delete_link(request, id):
    try:
        obj = URL.objects.get(id=id)
        obj.delete()
    except:
        return JsonResponse({'message':'null'})
    return JsonResponse({'message':'deleted'})

class AnonymousMessageListView(LoginRequiredMixin, ListView):
    model = AnonymousMessage
    template_name = 'messages.html'
    context_object_name = 'messages'

    def get_queryset(self):
        return URL.objects.get(id=self.kwargs.get('id')).anonymousmessage_set.all().order_by('-time_created')

@login_required
def homeview(request):
    return render(request, "home.html", {"form": URLCreationForm()})

@login_required
def newview(request):
    url = request.build_absolute_uri()[:-5]
    id = uuid.uuid4()
    data = {
        "link": url + reverse_lazy("send_message", args=[id]),
    }
    return JsonResponse(data)


class CreateMessageView(CreateView):
    model = AnonymousMessage
    template_name = "sendmessage.html"
    fields = ['message']
    def get_success_url(self) -> str:
        return reverse('message_sent')
    
    def form_valid(self, form):
        form.instance.to = URL.objects.get(url=self.request.build_absolute_uri())
        return super().form_valid(form)

def message_sent(request):
    return render(request, 'message_sent.html')
