from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage
from django.http import Http404
from django.utils.crypto import get_random_string
from datetime import datetime, timedelta


def paginate(request, objects):
    '''
    Pagination with validation checks
    '''
    try:
        limit = int(request.GET.get('limit', 10))
    except ValueError:
        limit = 10
    if limit > 100:
        limit = 10
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    paginator = Paginator(objects, limit)
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return page


def do_login(username, password):
    '''
    Validates the user, generates session key and returns it.
    '''
    user = authenticate(username=username, password=password)
    if not user:
        return None
    session = Session()
    session.key = get_random_string(length=32)
    session.user = user
    session.expires = datetime.now() + timedelta(days=5)
    session.save()
    return session.key