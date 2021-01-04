from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms
from django.forms import inlineformset_factory
from django.contrib import admin
from ..auth.auth_manager import get_user
from ..utils.context_utils import get_base_context
from ..models import *

class OAuthLoginRequiredMixin(LoginRequiredMixin):

  def dispatch(self, request, *args, **kwargs):
    user = get_user(request)

    if not user['is_authenticated']:
      return self.handle_no_permission()

    return super(LoginRequiredMixin, self).dispatch(
        request, *args, **kwargs)

class RecipeForm(forms.ModelForm):
  class Meta:
    model = Recipe
    exclude = []

# class IngredientForm(forms.ModelForm):
#   class Meta:
#     model = Ingredient
#     exclude = []

# class IngredientInline(admin.TabularInline):
#   model = Ingredient
#   form = IngredientForm

# class RecipeAdmin(admin.ModelAdmin):
#   model = Recipe
#   form = RecipeForm
#   inlines = [IngredientInline,]

#class CreateRecipePage(OAuthLoginRequiredMixin, TemplateView):
class CreateRecipePage(View):
  template_name = 'create_recipe.html'
  login_url = '/signin'

  def get(self, request, *args, **kwargs):
    context = get_base_context(self.request)

    recipe = Recipe.objects.get(pk=1)
    ing_formset = inlineformset_factory(Recipe, Ingredient, fields=['name',])

    formset = ing_formset(instance=recipe)

    context['recipe'] = {
      'title': 'Titlarino',
      'form': formset
    }

    return render(request, self.template_name, context)

  def post(self, request, *args, **kwargs):
    context = get_base_context(self.request)

    recipe = Recipe.objects.get(pk=1)
    form_factory = inlineformset_factory(Recipe, Ingredient, fields=['name',])

    form = form_factory(request.POST, instance=recipe)
    if (form.is_valid()):
      form.save()

    # TODO handle not-valid case

    context['recipe'] = {
      'title': 'Titlarino',
      'form': form
    }    

    return render(request, self.template_name, context)