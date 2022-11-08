from django.urls import path
from . import views # the '.' refers to referencing from the same folder we are in.

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('flowers/', views.flowers_index, name='index'),
    path('flowers/<int:flower_id>/', views.flowers_detail, name='detail'),
    path('flowers/create/', views.FlowerCreate.as_view(), name='flowers_create'),
    path('flowers/<int:pk>/update/', views.FlowerUpdate.as_view(), name='flowers_update'),
    path('flowers/<int:pk>/delete/', views.FlowerDelete.as_view(), name='flowers_delete'),
    path('flowers/<int:flower_id>/add_sighting/', views.add_sighting, name='add_sighting'),
    # Added Use patterns
    path('flowers/<int:flower_id>/assoc_use/<int:use_id>/', views.assoc_use, name='assoc_use'),
    path('flowers/<int:flower_id>/assoc_use/<int:use_id>/delete/', views.assoc_use_delete, name='assoc_use_delete'),
    path('uses/', views.UseList.as_view(), name='uses_index'),
    path('uses/<int:pk>/', views.UseDetail.as_view(), name='uses_detail'),
    path('uses/create/', views.UseCreate.as_view(), name='uses_create'),
    path('uses/<int:pk>/update/', views.UseUpdate.as_view(), name='uses_update'),
    path('uses/<int:pk>/delete/', views.UseDelete.as_view(), name='uses_delete'),
    path('accounts/signup/', views.signup, name='signup'),
]