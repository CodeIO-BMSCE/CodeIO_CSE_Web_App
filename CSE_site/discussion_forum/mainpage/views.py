from django.views.generic import TemplateView
from django.views.generic.edit import DeleteView
# Create your views here.

class HomePageView(TemplateView):
    template_name = "discussion_forum/home.html"

    
