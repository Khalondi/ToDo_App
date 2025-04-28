from django.urls import path
# from .views import TaskList
from .  import views

# urlpatterns = [
#     path('', TaskList.as_view() ,name='tasks')
# ]
urlpatterns = [
    path('',views.homepage, name='home'),
    path('create_todo/',views.create_todo,name='create_todo'),
    path('view_todo/',views.view_todo,name='view_todo'),
    path('edit_todo/<int:todo_id>',views.edit_todo,name='edit_todo')
]

