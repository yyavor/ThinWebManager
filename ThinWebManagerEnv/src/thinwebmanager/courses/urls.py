from django.urls import path
from .views import CourseDetailView, CoursesListView, CourseCreateView, CourseUpdateView, CourseDeleteView

app_name = "courses"
urlpatterns = [
    path('', CoursesListView.as_view(), name="course-list"),
    path('create/', CourseCreateView.as_view(), name="course-create"),
    path('<int:course_id>/', CourseDetailView.as_view(), name="course-detail"),
    path('<int:course_id>/delete/', CourseDeleteView.as_view(), name="course-delete"),
    path('<int:course_id>/update/', CourseUpdateView.as_view(), name="course-update"),
]
