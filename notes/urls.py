from django.urls import path
from .views import NoteDetailView, NoteListView

urlpatterns = [
    path('', NoteListView.as_view(), name='list_view'),
    path('<int:pk>/', NoteDetailView.as_view(), name='detail_view'),
]
