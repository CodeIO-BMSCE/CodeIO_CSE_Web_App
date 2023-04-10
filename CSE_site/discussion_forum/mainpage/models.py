from django.views.generic import TemplateView

# Create your models here.

class Profile(TemplateView):
    model = TemplateView
    template_name = "registration\profile.html"
