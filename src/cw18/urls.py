from django.urls import path

from cw18.views import cw18_index_01
from cw18.views import cw18_index_02
from cw19.views import comment_add

urlpatterns = [
   path(r'cw18_index_01/', cw18_index_01, name='index_01'),
   path(r'cw18_index_02/', cw18_index_02, name='index_02'),
   path(r'cw19/', comment_add, name='cw19')
]
