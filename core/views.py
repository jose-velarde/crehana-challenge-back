from django.views.generic import TemplateView


class AppsView(TemplateView):
    template_name = 'apps.html'

    def get_context_data(self, *args, **kwargs):
        context = super(AppsView, self).get_context_data(*args, **kwargs)
        context['apps'] = 'Gryffindor'
        return context
