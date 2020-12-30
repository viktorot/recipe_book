def get_user(request):
    return request.session.get('user', {'is_authenticated': False})

def store_user(request, user):
  request.session['user'] = {
    'is_authenticated': True,
    'name': user['displayName'],
    'email': user['mail'] if (user['mail'] != None) else user['userPrincipalName'],
  }