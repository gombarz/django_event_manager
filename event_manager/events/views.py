from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def first_view(request: HttpRequest) -> HttpResponse:
    """
    /events/first

    each view receives a http request and has to respond
    with a HttpResponse.
    """
    print(dir(request))
    print(request.user)
    print(request.method)
    print(request.GET)
    response = HttpResponse("hello world!")
    print("Response: ", response)

    return response
