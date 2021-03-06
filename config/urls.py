from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views import defaults as default_views
from django.views.generic import TemplateView
from entrega1tacchetti.rentapp.views import (
    PostDetailView,
    PostListView,
    TenantCreateView, 
    RentCarCreateView, 
    RentPlaceCreateView,
    TenantDetailView,
    PlaceDetailView,
    CarDetailView,
    search_results,
    PostCreateView,
    PostUpdateView,
    PostDeleteView)
from entrega1tacchetti.users import views as user_views

urlpatterns = [
    path("", PostListView.as_view(), name="home"),
    path( "about/", TemplateView.as_view(template_name="rentapp/about.html"), name="about"),
    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
    # User management
    path('profile/', user_views.profile, name='profile'),
    path("users/", include("entrega1tacchetti.users.urls", namespace="users")),
    path("accounts/", include("allauth.urls")),
    path('register/', user_views.register, name='register'),
    # Your stuff: custom urls includes go here
    
    #Creation Forms Views
    path( "tenant/new", TenantCreateView.as_view(), name="tenant-create"),
    path( "place/new", RentPlaceCreateView.as_view(), name="rentable-place-create"),
    path( "car/new", RentCarCreateView.as_view(), name="rentable-car-create"),
    
    #Created Objects Views
    path( "tenant/<str:pk>/created", TenantDetailView.as_view(), name="tenant-cretion-detail"),
    path( "place/<str:pk>/created", PlaceDetailView.as_view(), name="place-cretion-detail"),
    path( "car/<str:pk>/created", CarDetailView.as_view(), name="car-cretion-detail"),

    #Objects Detail View
    path( "tenant/<str:pk>", TenantDetailView.as_view(), name="tenant-detail"),
    path( "place/<str:pk>", PlaceDetailView.as_view(), name="place-detail"),
    path( "car/<str:pk>", CarDetailView.as_view(), name="car-detail"),

    #Search Results
    path( "search_results", search_results, name="search-results"),

    #Post Views
    path( "post/<int:pk>", PostDetailView.as_view(), name="post-detail"),
    path( "post/new", PostCreateView.as_view(), name="post-create"),
    path( "post/<int:pk>/update", PostUpdateView.as_view(), name="post-update"),
    path( "post/<int:pk>/delete", PostDeleteView.as_view(), name="post-delete"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
