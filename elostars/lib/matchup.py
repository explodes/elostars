import collections

from django.core import exceptions as e
from django.core.cache import caches
from elostars.lib.guid import make_guid
from elostars.main import models as main

cache = caches["matchup"]

TIMEOUT_SECONDS = 10 * 60  # ten minutes

Matchup = collections.namedtuple("Matchup", ("key", "left", "right"))


def validate_matchup(key):
    return cache.has_key(key)


def close_matchup(key):
    cache.delete(key)

def create_matchup(from_user):
    # unique guid
    key = make_guid(64)
    while validate_matchup(key):
        key = make_guid(64)

    try:
        left, = main.Picture.objects.matchup(from_user)[:1]
        right, = main.Picture.objects.matchup(from_user, left)[:1]
    except ValueError:
        return None

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


