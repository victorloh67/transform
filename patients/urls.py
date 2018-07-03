from django.urls import path
from . import views

app_name = 'patients'
urlpatterns = [
    path('', views.index, name='index'),
    # path('info/', views.InfoListView.as_view(), name='info'),
    path('profile/',views.ProfileListView.as_view(), name='profile'),
    path('profile/create/',views.register_profile, name='profile_create'),
    path('profile/<int:pk>', views.ProfileDetailView.as_view(), name='profile-details'),
    path('profile/<int:pk>/update/', views.ProfileUpdateView.as_view(), name='profile_update'),
    path('profile/<int:pk>/delete/', views.ProfileDeleteView.as_view(), name='profile_delete'),
    # path('info/<int:pk>', views.InfoDetailView.as_view(), name='info-details'),
    # path('info/create/', views.InfoCreate.as_view(), name='info_create'),
    # path('info/create/',views.register_user, name='info_create'),
    path('biometric/',views.BiometricListView.as_view(), name='biometric'),
    path('biometric/create/',views.BiometricCreate.as_view(), name='biometric_create'),
    path('biometric/<int:pk>', views.BiometricDetailView.as_view(), name='biometric-details'),
    path('biometric/<int:pk>/update/', views.BiometricUpdate.as_view(), name='biometric_update'),
    path('biometric/<int:pk>/delete/', views.BiometricDelete.as_view(), name='biometric_delete'),
    path('initial/create/',views.InitialCreate.as_view(), name='initial_create'),
    path('initial/', views.InitialListView.as_view(), name='initial'),
    path('initial/<int:pk>', views.InitialDetailView.as_view(), name='initial-details'),
    path('initial/<int:pk>/update/', views.InitialUpdate.as_view(), name='initial_update'),
    path('initial/<int:pk>/delete/', views.InitialDelete.as_view(), name='initial_delete'),
    path('week/', views.WeekListView.as_view(), name='week'),
    path('week/create/',views.WeekCreateView.as_view(),name='week_create'),
    path('week/<int:pk>',views.WeekDetailView.as_view(), name='week-detail'),
    path('week/<int:pk>/update/', views.WeekUpdateView.as_view(), name='week_update'),
    path('week/<int:pk>/delete/', views.WeekDelete.as_view(), name='week_delete'),
    path('checklist/', views.ChecklistList.as_view(), name='checklist'),
    path('checklist/create', views.ChecklistCreate.as_view(), name='checklist_create'),
    path('checklist/<int:pk>', views.ChecklistDetailView.as_view(), name='checklist-details'),
    path('checklist/<int:pk>/update/', views.ChecklistUpdateView.as_view(), name='checklist_update'),
    path('checklist/<int:pk>/delete/', views.ChecklistDelete.as_view(), name='checklist_delete'),

]
