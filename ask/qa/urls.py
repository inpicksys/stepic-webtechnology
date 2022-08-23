from django.urls import path
from .views import test, new_questions_view, popular_questions_view, \
    single_question_view, create_question_view, signup_view, login_view


app_name = 'qa'
urlpatterns = [
    path('login/', login_view, name = 'login_url'),
    path('signup/', signup_view),
    path('question/<int:question_id>/', single_question_view, name='single_question'),
    path('ask/', create_question_view),
    path('popular/', popular_questions_view),
    path('new/', test),
    path('', new_questions_view)
]
