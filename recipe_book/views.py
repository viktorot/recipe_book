from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .auth.oauth_utils import get_sign_in_flow, get_token_from_code, remove_user_and_token
from .auth import auth_manager
from . import user_helper
from .utils.context_utils import get_base_context

def home(request):
  context = get_base_context(request)
  return render(request, 'home.html', context)

def sign_in(request):
  # Get the sign-in flow
  flow = get_sign_in_flow()
  # Save the expected flow so we can use it in the callback
  request.session['auth_flow'] = flow
  # Redirect to the Azure sign-in page
  return HttpResponseRedirect(flow['auth_uri'])

def sign_out(request):
  # Clear out the user and token
  remove_user_and_token(request)

  return HttpResponseRedirect(reverse('home'))

def callback(request):
  # Make the token request
  result = get_token_from_code(request)

  #Get the user's profile
  user = user_helper.get_user(result['access_token'])

  # Store user
  auth_manager.store_user(request, user)
  return HttpResponseRedirect(reverse('home'))