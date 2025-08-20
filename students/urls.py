from rest_framework.routers import DefaultRouter
from .views import StudentViewSet

router = DefaultRouter()
router.register(r"", StudentViewSet, basename='student')

# urlpatterns = [
#     path('', include(router.urls)),
# ]

urlpatterns = router.urls

# This will automatically create the necessary URL patterns for the StudentViewSet.
# The URLs will be accessible at /students/ for listing and creating students,
# and /students/<id>/ for retrieving, updating, or deleting a specific student.
# Make sure to include this in your project's main urls.py file.
# Example:
# from django.urls import path, include
# urlpatterns = [
#     path('api/', include('students.urls')),
# ]