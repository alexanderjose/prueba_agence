from django.conf.urls import url
from . import views as desempenho_views

urlpatterns = [

    url(
        '^home$',
        desempenho_views.DesempenhoHomeView.as_view(),
        name='desempenho_home'
    ),
    url(
        r'^detail_receitas/$',
        desempenho_views.detail_receitas,
        name='detail_receitas'
    ),
    url(
        r'^detail_bar/$',
        desempenho_views.detail_bar,
        name='detail_bar'
    ),
    url(
        r'^detail_pizza/$',
        desempenho_views.detail_pizza,
        name='detail_pizza'
    ),

]
