from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    context = {'title': 'home'}
    return render(request, 'headersapp/home.html', context=context)


def get_headers(request):
    # Extract headers
    headers = request.META

    # Print headers
    # response_text = "\n".join(
    #     f"{key}: {value}" for key, value in headers.items())
    headers_list = [(key, value) for key, value in headers.items()]

    context = {'headers': headers_list, 'title': 'headers'}

    # Return the headers in the HTTP response
    # return HttpResponse(response_text, content_type='text/plain')
    return render(request, 'headersapp/headers.html', context=context)
