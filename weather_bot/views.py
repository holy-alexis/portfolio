from django.views import generic


class IndexPage(generic.TemplateView):
    template_name = "weather_bot_index.html"
