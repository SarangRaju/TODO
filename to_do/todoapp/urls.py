from django.urls import path
from . import views
app_name='todoapp'

urlpatterns = [
    path('',views.task,name='tasks'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:upid>/',views.update,name='update'),
    # path('details',views.details,name='details'),
    path('cbvhome/',views.tasklistview.as_view(),name='tasklistview'),
    path('cbvdetail/<int:pk>/',views.taskdetailview.as_view(),name='taskdetailview'),
    path('cbvupdate/<int:pk>/',views.taskupdateview.as_view(),name='taskupdateview'),
    path('cbvdelete/<int:pk>/',views.taskdeleteview.as_view(),name='taskdeleteview'),
]
