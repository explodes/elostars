import collections

from django.core import exceptions as e
from django.core.cache import get_cache
from elostars.lib.guid import make_guid
from elostars.main import models as main

cache = get_cache("matchup")

TIMEOUT_SECONDS = 10 * 60  # ten minutes

Matchup = collections.namedtuple("Matchup", ("key", "left", "right"))


def validate_matchup(key):
    return cache.has_key(key)


def close_matchup(key):
    cache.delete(key)


def create_matchup(exclude_user):
    # unique guid
    key = make_guid()
    while validate_matchup(key):
        key = make_guid()

    left, = main.Picture.objects.active() \
                .exclude(pk=exclude_user) \
                .order_by("?")[:1]
    right, = main.Picture.objects.active() \
                 .exclude(pk__in=(left.pk, exclude_user)) \
                 .order_by("?")[:1]

    cache.set(key, (left.guid, right.guid), TIMEOUT_SECONDS)

    return Matchup(key, left, right)


def get_matchup(key):
    guids = cache.get(key)
    if not guids:
        return None

    left_guid, right_guid = guids

    try:
        left = main.Picture.objects.active().get(guid=left_guid)
        right = main.Picture.objects.active().get(guid=right_guid)
        return Matchup(key, left, right)
    except e.ObjectDoesNotExist:
        return None


