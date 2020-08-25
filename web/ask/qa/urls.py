from django.urls import path
from .views import test, new_questions_view, popular_questions_view, \
    single_question_view, create_question_view


app_name = 'qa'
urlpatterns = [
    path('login/', test),
    path('signup/', test),
    path('question/<int:id>/', single_question_view, name='single_question'),
    path('ask/', create_question_view),
    path('popular/', popular_questions_view),
    path('new/', test),
    path('', new_questions_view)
]
