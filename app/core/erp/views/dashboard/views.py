from django.db.models import Sum
from django.db.models.functions import Coalesce
from django.views.generic import TemplateView
from datetime import datetime

from core.erp.models import Sale


class DashboardView(TemplateView):
    template_name = 'dashboard.html'

    def get_graph_sales_year_month(self):
        data = []
        try:
            year = datetime.now().year
            year = datetime.now().year
            for m in range(1, 13):
                total = Sale.objects.filter(date_joined__year=year, date_joined__month=m).aggregate(r=Coalesce(Sum('total'), 0)).get('r')
                data.append(float(total))
        except:
            pass
        return data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['panel'] = 'Panel de administrador'
        context['graph_sales_year_month'] = self.get_graph_sales_year_month()
        return context
