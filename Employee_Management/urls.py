from django.contrib import admin
from django.urls import include, path
from .views import *

urlpatterns = [
    path('home/',emp_home),
    path('add_emp/',add_emp),
    path("delete-emp/<int:emp_id>",delete_emp),
    path("edit-emp/<int:emp_id>",edit_emp),
    path("do-edit-emp/<int:emp_id>",do_edit_emp),

]