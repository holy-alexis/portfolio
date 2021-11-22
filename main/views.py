from django.views import generic


class IndexPage(generic.TemplateView):
    template_name = "main_index.html"


class GitPage(generic.TemplateView):
    template_name = "git.html"
