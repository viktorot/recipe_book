from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from ..auth.auth_manager import get_user
from ..utils.context_utils import get_base_context

class OAuthLoginRequiredMixin(LoginRequiredMixin):

  def dispatch(self, request, *args, **kwargs):
    user = get_user(request)

    if not user['is_authenticated']:
      return self.handle_no_permission()

    return super(LoginRequiredMixin, self).dispatch(
        request, *args, **kwargs)

class WelcomePage(OAuthLoginRequiredMixin, TemplateView):
  template_name = 'welcome.html'
  login_url = '/signin'

  def get_context_data(self, **kwargs):
    return get_base_context(self.request)