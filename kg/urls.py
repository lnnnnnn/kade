from django.conf.urls import url
from . import views
from django.contrib.staticfiles import views as static_views

app_name = 'kg'
from django.conf.urls.static import static
from django.conf import settings
# from args import TRIPLE_ARG
# from api import args
import kg.api as api
args = api.args

TRIPLE_ARG=args.TRIPLE_ARG
triple_params=""
for field in TRIPLE_ARG:
    if TRIPLE_ARG[field]['node']!=2:
        triple_params+='(.*)/'
    else :
        triple_params += '(.*)/(.*)/'#接受两个参数om,oe

# print('triple_params:',triple_params)
MENT2ENT_ARG=args.MENT2ENT_ARG
ment2ent_params=""
if MENT2ENT_ARG!=None:
    for field in MENT2ENT_ARG:
        ment2ent_params+='(.*)/'

urlpatterns = [
    # url(r'^add/((?:-|\d)+)/((?:-|\d)+)/$', views.add, name='add'),
    # url(r'^static/(?P<path>.*)$', static_views.serve, name='static'),
    # url(r'^remove_action(?P<nid>[a-z0-9]{24})/$',views.remove_action,name='remove_action'),
    # url(r'^modify_action(?P<id>[a-z0-9]{24})/$', views.modify_action, name='modify_action'),
    # url(r'^add/action$', views.add_action,name='add_action'),
    url(r'^$', views.login, name='login'),
    url(r'^index/$', views.index),
    url(r'^visindex/$', views.visindex),
    url(r'^temp/$', views.temp),
    url(r'^login/$', views.login, name='login'),
    url(r'^settings/$', views.settings, name='settings'),

    # url(r'^query/action$', views.query_action,name='query_action'),
    url(r'^query_auto/(.*)/$', views.query_edge, name='query_edge'),
	url(r'^modify/([a-z0-9]{24})/', views.modify, name='modify'),
    url(r'^add/', views.add, name='add'),
    #url(r'^modify/([a-z0-9]{24})/'+triple_params+'$', views.modify, name='modify'),
    #url(r'^add/{}$'.format(triple_params), views.add, name='add'),
    url(r'^remove/([a-z0-9]{24})/$', views.remove, name='remove'),
    # url(r'^add_choice/(.*)/(.*)/(.*)/$', views.add_choice, name='add_choice'),
    # ----------------------------------------------------------------------------------------------------
    url(r'^query_auto_entity/(.*)/$', views.query_auto_entity, name='query_auto_entity'),

    # url(r'^modify_entity/(.*)/(.*)/$', views.modify_entity, name='modify_entity'),
    # url(r'^add_entity/((?:-|\w)+)/$', views.add_entity, name='add_entity'),
    url(r'^add_entity/(.*)/$', views.add_entity, name='add_entity'),
    # ?????没处理括号等特殊字符
    url(r'^remove_entity/(.*)/$', views.remove_entity, name='remove_entity'),
    # ------------------------------------ ment2ent -------------------------------------------------------------------------------------------------

    url(r'^query_ment2ent_by_entity/(.*)/$', views.query_ment2ent_by_entity,name='query_ment2ent_by_entity'),
    url(r'^modify_ment2ent/([a-z0-9]{24})/' + ment2ent_params + '$', views.modify_ment2ent, name='modify_ment2ent'),
    url(r'^add_ment2ent/{}$'.format(ment2ent_params), views.add_ment2ent, name='add_ment2ent'),
    url(r'^remove_ment2ent/(.*)/$', views.remove_ment2ent, name='remove_ment2ent'),
    # vis editor-------------------------------------------------------------------------------------------------
    url(r'^api/v1/entitiesAdvice/$', views.getEntitiesAdvice, name='getEntitiesAdvice'),
    url(r'^api/v1/getTriples/$',views.getTriples_vis,name='getTriples_vis'),
    url(r'^api/v1/addEntity$',views.addEntity_vis,name='addEntity_vis'),
    url(r'^api/v1/removeEntity$',views.removeEntity_vis,name='removeEntity_vis'),
    url(r'^api/v1/removeTriple$',views.removeTriple_vis,name='removeTriple_vis'),
    url(r'^api/v1/addTriple$',views.addTriple_vis,name='addTriple_vis'),

    # -----------------------------------------------------------------------------------------------------
    # url(r'^query_auto_ment2ent/(.*)/$', views.query_auto_ment2ent, name='query_auto_ment2ent'),
    # url(r'^query_auto_ment2ent_entity/(.*)/$', views.query_auto_ment2ent_entity, name='query_auto_ment2ent_entity'),
    #
    # url(r'^modify_ment2ent/([a-z0-9]{24})/(.*)/(.*)/$', views.modify_ment2ent, name='modify_ment2ent'),
    # url(r'^add_ment2ent/(.*)/(.*)/$', views.add_ment2ent, name='add_ment2ent'),
    # # ?????没处理括号等特殊字符
    # url(r'^remove_ment2ent/([a-z0-9]{24})/$', views.remove_ment2ent, name='remove_ment2ent'),
    # url(r'^upload/(.*)/(.*)/$', views.upload, name='upload'),
    # url(r'^get_link/(.*)/$', views.getLink, name='getLink'),
    #
    # # ------------------------------------------------------------------------------
    # url(r'^get_progress/$', views.getProgress, name='getProgress'),
    # # ------------------------------------------------------------------------------
    # url(r'^query_auto_types/(.*)/$', views.query_auto_types, name='query_auto_types'),
    # url(r'^modify_types/([a-z0-9]{24})/(.*)/(.*)/$', views.modify_types, name='modify_types'),
    # url(r'^add_types/(.*)/(.*)/$', views.add_types, name='add_types'),
    # url(r'^remove_types/([a-z0-9]{24})/$', views.remove_types, name='remove_types'),

    # ---db-settings-----------------------------------------------
    url(r'^saveDB_settings_server/(.*)/(.*)/(.*)/(.*)/(.*)/$', views.saveDB_settings_server,
        name='saveDB_settings_server'),

    # url(r'^saveDB_settings_user/(.*)/(.*)/(.*)/$', views.saveDB_settings_user,
    #     name='saveDB_settings_user'),
    #
    # url(r'^saveDB_settings_entities/(.*)/(.*)/(.*)/(.*)/$', views.saveDB_settings_nodes,
    #     name='saveDB_settings_entities'),
    #
    # url(r'^saveDB_settings_triples/(.*)/(.*)/(.*)/(.*)/(.*)/(.*)/(.*)/$', views.saveDB_settings_edges,
    #     name='saveDB_settings_triples'),

    # url(r'^saveDB_settings_ment2ent/(.*)/(.*)/(.*)/(.*)/(.*)/$', views.saveDB_settings_ment2ent,
    #     name='saveDB_settings_ment2ent'),
    #
    # url(r'^saveDB_settings_types/(.*)/(.*)/(.*)/(.*)/(.*)/$', views.saveDB_settings_types,
    #     name='saveDB_settings_types'),
    url(r'^query_schema/$', views.query_schema, name='query_schema'),
    url(r'^modify_schema/([a-z0-9]{24})/', views.modify_schema, name='modify_schema'),
    url(r'^add_schema/', views.add_schema, name='add_schema'),
    url(r'^remove_schema/([a-z0-9]{24})/$', views.remove_schema, name='remove_schema')
]
# (?P<id>[a-z0-9]{24})/(?P<subject>\w+)/(?P<predicate>\w+)/(?P<object>\w+)

