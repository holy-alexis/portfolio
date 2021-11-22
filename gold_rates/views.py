from django.views import generic
import sqlite3


class IndexPage(generic.TemplateView):
    template_name = "gold_rates_index.html"


class DatesPage(generic.ListView):
    template_name = "gold_rates_dates.html"
    context_object_name = "dates"

    def get_queryset(self):
        con = sqlite3.connect("/root/.suka/python/parser/gold.db")
        cur = con.cursor()
        dates = []
        for i in cur.execute("SELECT * FROM dates"):
            dates.append(i[0])
        con.close()
        return dates


class RatePage(generic.ListView):
    template_name = "gold_rate.html"
    context_object_name = "rates"

    def get_queryset(self):
        con = sqlite3.connect("/root/.suka/python/parser/gold.db")
        cur = con.cursor()
        rates = {"rates": [], "average_buy": "", "average_sell": ""}
        date = self.kwargs["date"]
        buy_sum = 0
        sell_sum = 0
        for i in cur.execute(f'''SELECT * FROM "{date}"'''):
            rates["rates"].append(i)
            buy_sum += float(i[1].replace(" ", ""))
            sell_sum += float(i[2].replace(" ", ""))
        con.close()
        x = str(round(buy_sum / 12, 2))
        y = str(round(sell_sum / 12, 2))
        if len(x[x.find(".")+1::]) == 1:
            x += "0"
        if len(y[y.find(".")+1::]) == 1:
            y += "0"
        if len(x[0:x.find(".")]) >= 4:
            x = x[0:x.find(".")-3] + " " + x[x.find(".")-3::]
        if len(y[0:y.find(".")]) >= 4:
            y = y[0:y.find(".")-3] + " " + y[y.find(".")-3::]
        rates["average_buy"] = str(x)
        rates["average_sell"] = str(y)
        return rates
