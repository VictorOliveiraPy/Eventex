from django.conf import settings
from django.contrib import messages
from django.core import mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription


def subscribe(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)


def create(request):
    form = SubscriptionForm(request.POST)
    
    if not form.is_valid():
        return render(request, 'subscriptions/subscription_form.html',  # Errros
                      {'form': form})

    # Send email Success
    _sed_mail('Confirmação de inscrição',
              settings.DEFAULT_FROM_EMAIL,
              form.cleaned_data['email'],
              'subscriptions/subscription_email_txt',
              form.cleaned_data)

    Subscription.objects.create(**form.cleaned_data)

    # Success feedback
    messages.success(request, 'Inscrição realizada com sucesso!')

    return HttpResponseRedirect('/inscricao/')


def new(request):
    return render(request, 'subscriptions/subscription_form.html',
                  {'form': SubscriptionForm()})


def _sed_mail(subject, from_, to, template_name, context):  # auxiliar
    body = render_to_string(template_name, context)
    mail.send_mail(subject, body, from_, [from_, to])
