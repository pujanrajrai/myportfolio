from django.urls import path
from .views import blogs, blog_detail
app_name = "blog"
urlpatterns = [
    path(
        'list/', blogs, name="blog_list"
    ),
    path(
        'detail/<int:pk>/', blog_detail, name="blog_detail"
    )

]
