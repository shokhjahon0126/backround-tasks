from django.urls import path


from .views import celery_view,get_status

urlpatterns = [
    
  path('task/',celery_view),
  path('status/',get_status)

]
