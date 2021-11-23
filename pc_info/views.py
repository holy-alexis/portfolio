from django.http import HttpResponse
from pc_info.pc_info import Get_PC_Info
from django.views import generic


class IndexPage(generic.TemplateView):
    template_name = "pc_info/pc_info_index.html"


class Receive(generic.View):
    def get(self, request):
        return HttpResponse(Get_PC_Info())
