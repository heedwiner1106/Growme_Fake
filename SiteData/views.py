import random, json
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import (
  TemplateView,
  FormView,
  CreateView,
  UpdateView,
  DeleteView,
  DetailView,
  ListView,
  View
)

from SiteData.forms import SiteCreateForm
from .models import SiteData
import time

# Create your views here.
class SiteListView(TemplateView):
  """danh sách site"""

  template_name = 'pages/list-site.html'

  def get_context_data(self, **kwargs):
    list_site = super().get_context_data(**kwargs)
    list_site['list_site'] = []
    return list_site
  
  def post(self, request):
    list_site = {}
    param_action = request.POST.get('action')
    if param_action == 'load_site':
      # param = json.loads(request.POST.get('params'))
      # print('param: ', param)
      # param_type = param.get('type', -1) or -1
      # param_cms = param.get('cms', -1) or -1
      # param_owner = param.get('owner', -1) or -1
      # param_manager = param.get('manager', -1) or -1

      # print(param_type)
      data = super().get_context_data()
      # data['type'] = param_type
      # data['cms'] = param_cms
      # data['owner'] = param_owner
      # data['manager'] = param_manager
      data['list_site'] = SiteData.objects.all()
      data['abcd'] = 'asadjakdj'
      return render(request, 'pages/sites.html', data)


class SiteCreateView(CreateView):
  form_class = SiteCreateForm
  template_name = 'pages/create.html'

  # success_url: reverse_lazy('Site:list_sites')
  success_message = 'success'
  def get_form(self, form_class = None):
    form = super().get_form(form_class)
    return form

  def get_success_url(self):
        return reverse_lazy('Site:list_sites')