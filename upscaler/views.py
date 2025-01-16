from django.http import FileResponse
from django.shortcuts import render
from .forms import ImageForm
from .upscale import upscale
from django.views import generic
from main.settings import MEDIA_URL


class UpscalerIndexPage(generic.TemplateView):
    template_name = "upscaler/upscaler_index.html"

    def get(self, request):
        form = ImageForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            upscale(f'{img_obj.image}')  # without '/' cause MEDIA_URL already has it
            return FileResponse(img_obj.image.open(), as_attachment=True)
        return render(request, self.template_name, {'form': form})
