from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import ShortenedURL
import logging

logger = logging.getLogger(__name__)


def shorten_url(request):
    if request.method == 'POST':
        long_url = request.POST.get('long_url')
        if long_url:
            try:
                shortened_url = ShortenedURL(long_url=long_url)
                shortened_url.save()
                return render(request, 'cakes/shorten_url.html', {'shortened_url': shortened_url})
            except ValueError as e:
                return render(request, 'cakes/shorten_url.html', {'error': str(e)})
            except Exception as e:
                return render(request, 'cakes/shorten_url.html', {'error': f"Произошла ошибка: {str(e)}"})
    return render(request, 'cakes/shorten_url.html')


def redirect_to_long_url(request, short_url):
    try:
        shortened_url = get_object_or_404(ShortenedURL, short_url=short_url)
        shortened_url.click_count += 1
        shortened_url.save()
        return HttpResponseRedirect(shortened_url.long_url)
    except Exception as e:
        logger.error(f"Ошибка при перенаправлении: {str(e)}")
        return redirect(f"/error/?error={str(e)}")


def error_page(request):
    error_message = request.GET.get('error', 'Произошла неизвестная ошибка.')
    return render(request, 'cakes/error.html', {'error': error_message})
