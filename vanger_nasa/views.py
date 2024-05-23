from django.shortcuts import render
from django.views.generic import TemplateView

from slider.models import Slide


class HomePageView(TemplateView):
    template_name = 'vanger_nasa/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['slides'] = Slide.objects.all()
        return context
# def get_index(request):
#     context = {}
#     slides = Slide.objects.all()
#     context = {'slides': slides}
#     return render(request, 'vanger_nasa/index.html', context)