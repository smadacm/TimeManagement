from django import template

register = template.Library()

@register.inclusion_tag('messages.html', takes_context=True)
def get_messages(context):
    session = context['request'].session
    ret = {}
    for t in ('good_message', 'info', 'warning', 'error'):
        if t in session:
            ret[t] = session[t]
            del session[t]
        else:
            ret[t] = None
    return ret

@register.inclusion_tag('top_menu.html', takes_context=True)
def top_menu(context):
    return {}

@register.filter
def count(array):
    return len(array)
