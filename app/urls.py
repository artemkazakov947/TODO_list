from django.urls import path

from app.views import Home, \
    TaskCreateView, \
    TaskDeleteView, \
    TaskUpdateView, \
    TagListView, \
    TagCreateView, \
    TagUpdateView, \
    TagDeleteView, \
    mark_complete_or_undo

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("create/", TaskCreateView.as_view(), name="task-create"),
    path("<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
    path("<int:pk>/mark_task/", mark_complete_or_undo, name="task-mark")
]


app_name = "app"
