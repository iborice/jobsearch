# myapi/urls.py
from django.urls import include, path
from rest_framework import routers
from . import views
from django.views.generic import TemplateView

router = routers.DefaultRouter()
router.register(r'offres', views.PosteViewSet)
router.register(r'villes', views.VilleViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/', include(router.urls)),
    path('Offres-emploi/',views.JobsView.as_view(), name='postes'),
    path('Offres-emploi/details/<int:pk>/',views.JobDetailsView.as_view(), name='job-details'),
    path('Offres-emploi/About_us/',views.AboutView.as_view(), name='about'),
    path('Offres-emploi/Licence/',views.LicenceView.as_view(), name='licence'),
    path('Offres-emploi/Terms_and_conditions/',views.TermsView.as_view(), name='terms'),
    path('Offres-emploi/Contact/',views.ContactView.as_view(), name='contact'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]