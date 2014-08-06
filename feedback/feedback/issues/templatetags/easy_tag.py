from django import template

register = template.Library()
"""
Decorator to facilitate template tag creation
"""


def easy_tag(func):
    """deal with the repetitive parts of parsing template tags"""
    def inner(parser, token):
        #print token
        try:
            return func(*token.split_contents())
        except TypeError:
            raise template.TemplateSyntaxError('Bad arguments for tag "%s"' % token.split_contents()[0])
    inner.__name__ = func.__name__
    inner.__doc__ = inner.__doc__
    return inner


class AppendGetNode(template.Node):
    def __init__(self, dict):
        self.dict_pairs = {}
        for pair in dict.split(','):
            pair = pair.split('=')
            self.dict_pairs[pair[0]] = template.Variable(pair[1])

    def render(self, context):
        get = context['request'].GET.copy()
        for key in self.dict_pairs:
            get[key] = self.dict_pairs[key].resolve(context)

        path = context['request'].META['PATH_INFO']

        if len(get):
            # If first value give a "?"
            path += '?'
            for key in get:
                # Extra code required here to deal with lists code this be cleaner
                try:
                    value = get.getlist(key)
                except:
                    value = get[key]
                #print value

                if value:
                    # Extra code required here to deal with lists
                    if isinstance(value, list):
                        for item in value:
                            path += "%s=%s&" % (key, item)
                    else:
                        path += "%s=%s&" % (key, value)
            # trim the & for the last extry
            path = path.rstrip('&')
        return path


@register.tag()
@easy_tag
def append_to_get(_tag_name, dict):
    return AppendGetNode(dict)
