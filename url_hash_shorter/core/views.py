# -*- coding: utf-8 -*-
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.http import require_http_methods

from core.models import URL


def index(request, template_name='index.html'):
    context = {
        'urls': URL.objects.order_by('-pk'),
        'menu': 'index',
    }
    return render(request, template_name, context=context)


@require_http_methods(['POST', ])
def create_url(request):
    try:
        URL.objects.get(source_url=request.POST['url'])
    except URL.DoesNotExist:
        url = URL.objects.create(source_url=request.POST['url'])
        messages.success(request, 'Спасибо, ваша ссылка успешно создана: <a href="{}">перейти</a>.'.format(url.get_absolute_url()))
    return redirect('core:index')


@require_http_methods(['GET', ])
def remove_url(request, url_pk):
    url = URL.objects.get(pk=url_pk)
    slug = url.short_slug
    source_url = url.source_url
    url.delete()
    messages.error(request, 'Спасибо, ссылка <a href="{href}">{source}</a> успешно удалена'.format(href=slug, source=source_url))
    return redirect('core:links')


def links(request, template_name='links.html'):
    context = {
        'urls': URL.objects.order_by('-pk'),
        'menu': 'links',
    }
    return render(request, template_name, context=context)


def url_redirect(request, slug):
    url = get_object_or_404(URL, short_slug=slug)
    url.views += 1
    url.save()
    return HttpResponseRedirect(url.source_url)
