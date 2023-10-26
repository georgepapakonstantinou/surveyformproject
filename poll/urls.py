from django.contrib import admin
from django.urls import path
from poll import views

#template urls
app_name= 'poll'

urlpatterns=[
    path('admin/', admin.site.urls),
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'),
    path('questions/',views.questions,name='questions'),
    path('submit_answers/',views.submit_answers,name='submit_answers'),
    path('user_answers/', views.user_answers, name='user_answers'),
    path('create_patient/',views.create_patient, name='create_patient'),
    path('saved_patients/',views.saved_patients, name='saved_patients'),
    path('patient_choices',views.patient_choices, name='patient_choices'),
    path('demo',views.demo,name='demo'),
    path('search_patients',views.search_patients, name='search_patients'),
    path('download_patient_choices_csv/<int:patient_id>/', views.download_patient_choices_csv, name='download_patient_choices_csv'),


]
