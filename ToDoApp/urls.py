from django.urls import path
from . import views


urlpatterns = [
    path('fetch',views.fetching.as_view(),name='fetch'),
    path('create',views.creating.as_view(),name='create'),
    path('update/<int:pk>',views.updating.as_view(),name='update'),
    path('delete/<int:pk>',views.deleting.as_view(),name='delete')
]
