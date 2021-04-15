from django.urls import path
from . import views,api

urlpatterns = [
	path('',views.frontpage,name='frontpage'),
	path('write_post/',views.write_post,name='write_post'),
	path('tag/<slug:tag_slug>/',views.tag_post_list,name='tag_post_list'),
	path('search/',views.search,name='search'),

	path('api/post/',api.post,name='post'),

]