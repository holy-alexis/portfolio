from django.views import generic
from towns.models import People, Town


class IndexPage(generic.TemplateView):
    template_name = 'towns/towns_index.html'


class SearchPage(generic.TemplateView):
    template_name = 'towns/search_page.html'


def get_ids(ids, str_to_search):
    if " " in str_to_search:
        p = People.objects.filter(name__contains=str_to_search.split(" ")[0]) or People.objects.filter(surname__contains=str_to_search.split(" ")[1])
    else:
        p = People.objects.filter(name__contains=str_to_search) or People.objects.filter(surname__contains=str_to_search)
    for people in p:
        if people.pk in ids:
            continue
        ids.append(people.pk)
    return ids


class SearchByPeople(generic.ListView):
    template_name = 'towns/result.html'
    context_object_name = 'peoples_list'

    def get_queryset(self):
        ids = []
        ids = get_ids(ids, self.kwargs["str_to_search"])
        str_to_search = self.kwargs["str_to_search"].title()
        ids = get_ids(ids, str_to_search)
        peoples = []
        for id in ids:
            people = People.objects.get(pk=id)
            peoples.append(people)
        return peoples


class TownsList(generic.TemplateView):
    template_name = 'towns/towns.html'


class SearchByTown(generic.ListView):
    template_name = 'towns/result.html'
    context_object_name = 'peoples_list'

    def get_queryset(self):
        town = Town.objects.filter(town_name=self.kwargs["str_to_search"])
        peoples_list = []
        if len(town) == 0:
            return []
        for i in town[0].people_set.all():
            peoples_list.append(i)
        return peoples_list


class PersonView(generic.DetailView):
    model = People
    template_name = 'towns/person.html'
