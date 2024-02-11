from django.views import generic
import sqlite3
from django.core.paginator import Paginator


class IndexPage(generic.TemplateView):
    template_name = "gold_rates/gold_rates_index.html"


class DatesPage(generic.ListView):
    template_name = "gold_rates/gold_rates_dates.html"
    context_object_name = "data"

    def get_queryset(self):
        with sqlite3.connect("gold.db") as con:
            cur = con.cursor()
            dates = []
            for i in cur.execute("SELECT * FROM dates"):
                dates.append(i[0])
            dates.reverse()
            p = Paginator(dates, 10)
            data = {'dates': [], 'current_page': 0, 'max_page': 0, 'next_page': 0, 'prev_page': 0}

            page = p.page(self.kwargs['page'])
            data['current_page'] = page.number
            data['max_page'] = p.num_pages

            if page.has_next():
                data['next_page'] = page.next_page_number()
            else:
                data['next_page'] = page.number

            if page.has_previous():
                data['prev_page'] = page.previous_page_number()
            else:
                data['prev_page'] = page.number

            data['dates'] = page.object_list

            return data


class RatePage(generic.ListView):
    template_name = "gold_rates/gold_rate.html"
    context_object_name = "rates"

    def get_queryset(self):
        with sqlite3.connect("gold.db") as con:
            cur = con.cursor()
            rates = {"rate": "", "date": ""}
            date = self.kwargs["date"]
            rates["date"] = date
            try:
                r = cur.execute(f'''SELECT * FROM "{date}"''')
                rates["rate"] = r.fetchone()[0]
            except sqlite3.OperationalError:
                return None
            return rates
