from django.contrib.auth.forms import AuthenticationForm
from django.template import Library

register = Library()


@register.inclusion_tag("auth/login_form.html", takes_context=True)
def login_form(context):
    request = context.request
    return {
        "request": request,
        "form": AuthenticationForm(request.POST or None),
    }
