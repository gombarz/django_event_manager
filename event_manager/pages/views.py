from django.views.generic.base import TemplateView
from events.models import Event, Category
from event_manager.services import ServiceAPI


class HomePageView(TemplateView):
    """this is the homepage of our project."""
    template_name = "pages/index.html"

    def get_context_data(self, **kwargs) -> dict:
        """intercept context data and add new context
        by ourselves. 
        returns the context dict
        """
        context = super().get_context_data(**kwargs)
        context["events"] = Event.objects.all()[:5]
        context["categories"] = Category.objects.all()[:5]
        return context
