from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from ..views import initialize_context

class OAuthLoginRequiredMixin(LoginRequiredMixin):

  def dispatch(self, request, *args, **kwargs):
    user = request.session.get('user', {'is_authenticated': False})

    if not user['is_authenticated']:
      return self.handle_no_permission()

    return super(LoginRequiredMixin, self).dispatch(
        request, *args, **kwargs)

class WelcomePage(OAuthLoginRequiredMixin, TemplateView):
  template_name = 'welcome.html'
  login_url = '/signin'

  def get_context_data(self, **kwargs):
    return initialize_context(self.request)