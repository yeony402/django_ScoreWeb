from django.urls import path, include
from django.contrib.auth.decorators import permission_required
from . import views


# app_name을 지정해주면 template에 {% url %}에도 app_name을 명시해야함 ex-{% url 'appname:name' %}
app_name = 'django_ex'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('docs/<int:current_user>/', views.document_list, name='document_list'),
    path('docs/<int:current_user>/<int:current_ceo>/', views.document_post, name='document_post'),
    path('docs/<int:current_user>/<int:current_ceo>/results/', views.document_results, name='document_results'),
    path('presentation/<int:current_user>/', views.presentation_list, name='presentation_list'),
    path('manager/base_info_list/', views.BaseListView.as_view(), name='base_info_list'),
    path('manager/base-info-change/<int:current_ceo>/', views.base_info_change, name='base-info-change'),
    path('manager/base-info-check/', views.base_info_check, name='base-info-check'),
    path('manager/input/', views.base_info, name='base_info'),
    path('show-results/<int:current_user>/', views.checked_evaluation, name='checked-evaluation'),
    path('change-results/<int:current_user>/<int:current_ceo>/', views.changed_evaluation, name='changed-evaluation'),
    path('docs/발표평가-1차/', views.TestListView.as_view(), name='test_list'),
    path('docs/발표평가-1차/평가목록/', views.select_year, name='select_year'),
    path('docs/발표평가-1차/종합결과/', views.test_total_results, name='test_total_results'),
    path('docs/발표평가-1차/평가결과목록/', views.select_year_results, name='select_year_results'),
    path('docs/발표평가-1차/발표차수/', views.select_th, name='select_th'),
]
