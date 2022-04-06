from django.urls import path
from graphene_django.views import GraphQLView


from . import views

urlpatterns = [
    path('cars', views.ListCreateCarView.as_view()),
    path('cars/<int:pk>', views.UpdateDeleteCarView.as_view()),
    path("graphql", GraphQLView.as_view(graphiql=True)),

]
