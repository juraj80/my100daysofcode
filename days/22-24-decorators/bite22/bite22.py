'''
Write a decorator called make_html that wraps text inside one or more html tags.

As shown in the tests decorating get_text with make_html twice should wrap the text in the corresponding html tags, so:

@make_html('p')
@make_html('strong')
def get_text(text='I code with PyBites'):
    return text
- would return: <p><strong>I code with PyBites</strong></p>
'''

from functools import wraps

def make_html(element):
    def decorator(func):
        @wraps(func)
        def wrapper():
            return f'<{element}>{func()}</{element}>'
        return wrapper
    return decorator


@make_html("p")
@make_html("strong")
def get_text(text='I code with PyBites'):
    return text

if __name__ == '__main__':
    print(get_text())
