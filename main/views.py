from django.views import generic


class IndexPage(generic.TemplateView):
    template_name = "main/main_index.html"


class GitPage(generic.TemplateView):
    template_name = "main/git.html"
