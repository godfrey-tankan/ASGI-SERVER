from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import *


# Create your views here.
@login_required
def chat_view(request):
    chat_group = get_object_or_404(ChatGroup, group_name='t & t')
    chat_messages = chat_group.chat_messages.all()[:20]
    form = ChatMessageCreateForm()

    if request.method == 'POST':
        form = ChatMessageCreateForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.group = chat_group
            message.author = request.user
            message.save()
            context = {'message':message, 'user':request.user}
            return render(request, 'chat.html', {'context':context})
    return render(request, 'chat.html', {'chat_messages':chat_messages, 'form':form})