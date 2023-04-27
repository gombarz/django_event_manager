import logging
from django.http import HttpRequest, HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from .models import Category, Event
from .forms import CategoryForm, EventForm

logger = logging.getLogger(__name__)

class UserIsOwnerOrAdmin(UserPassesTestMixin):

    def test_func(self) -> bool:
        # if returns True, Permission is fine. 
        # Otherwise will result in a 403 Forbidden Error
        return (self.get_object().author == self.request.user or 
                self.request.user.is_superuser)

class EventDeleteView(SuccessMessageMixin, 
                      UserIsOwnerOrAdmin, 
                      DeleteView):
    """
    generic template for confirmation page: event_confirm_delete.html
    """
    model = Event
    success_url = reverse_lazy("events:events")
    success_message = "Event was successfully deleted"


class EventUpdateView(SuccessMessageMixin, 
                      UserIsOwnerOrAdmin, 
                      UpdateView):
    model = Event
    form_class = EventForm
    success_message = "Event was successfully updated"
    

class EventCreateView(CreateView):
    model = Event
    form_class = EventForm
    # template_name = "some_other_template.html"
    # success_url = "https://amazon.com"

    def form_valid(self, form) -> HttpResponse:
        # set the author field to the current 
        # authenticated user (self.request.user)
        form.instance.author = self.request.user
        return super().form_valid(form)    


class EventDetailView(DetailView):
    model = Event

class EventListView(ListView):
    """will show all events in a list

    /events
    generic template name: event_list.html
    generic context name: object_list

    """
    model = Event
    queryset = Event.objects.select_related("category", "author").all()
    # queryset = Event.objects.prefetch_related("category", "author").all()


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
            return redirect(reverse("events:category_detail", args=(category.pk,)))
        logger.warning("Wrong Form data added.")
    else:
        form = CategoryForm()
      
    return render(request, 
                  "events/category_create.html", {
                    "form": form,
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
