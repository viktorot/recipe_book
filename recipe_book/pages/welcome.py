from django.views.generic import TemplateView

class WelcomePage(TemplateView):
    template_name = 'welcome.html'