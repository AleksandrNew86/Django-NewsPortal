from django import template

register = template.Library()


@register.filter()
def censor(value, forbid_words):
    return value.replace(forbid_words, f'{"*"* len(forbid_words)}')
