from django.conf import settings


def cdn_link(href):
    if not href:
        return href
    if href.startswith("http"):
        return href
    return settings.CDN_URL + href
