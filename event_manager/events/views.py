import logging
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Event
from .forms import CategoryForm

logger = logging.getLogger(__name__)

def categories(request):
    """ 
    Show a list of categories.
    /events/categories
    Templates have to live in templates/<APP_NAME>
    """
    categories = Category.objects.all()
    logger.warning(categories)

    return render(request, 
                  "events/category_list.html", {
                    "categories": categories,
                  })


def category_detail(request, pk):
    """ 
    Show a detail page for category
    /events/category/9
    """
    category = get_object_or_404(Category, pk=pk)

    return render(request, 
                  "events/category_detail.html", {
                    "category": category
                  })


def category_create(request):
    """Create new Category with POST data.
    
    events/category/create

    if called via GET: show Form
    if called via POST: try insert Data
    """
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save()
            return redirect("events:categories")
        logger.warning("Wrong Form data added.")
    else:
        form = CategoryForm()
      
    return render(request, 
                  "events/category_create.html", {
                    "form": form
                  })
      

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
