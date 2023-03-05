import itertools

def stringify(value, replacer='.', spases_count=0, const=4, depth=1):
    current_indent = special_indent_key(value, replacer, const, depth)
    indent = replacer * spases_count

    def walk(key, val):
        return f'''{
            current_indent}{key}: {stringify(
            val, replacer, spases_count=spases_count+4, depth=depth + 1
            ) if isinstance(val, dict) else val
            }'''

    res = map(lambda x, y: walk(x, y), value.keys(), value.values())
    result = itertools.chain('{', res, [indent + '}'])
    return '\n'.join(result)

def special_indent_key(value, replacer, const, depth):
    key = ''.join(filter(lambda x: x, value.keys()))
    if key[0].isalnum():
        return replacer * (const*depth)
    return replacer * (const*depth-2)

print(stringify({
    '  common': {
        '+ follow': False, 
        '  setting1': 'Value 1', 
        '- setting2': 200, 
        '- setting3': True, 
        '+ setting3': None, 
        '+ setting4': 'blah blah', 
        '+ setting5': {'key5': 'value5'}, 
        '  setting6': {
            '  doge': {
                '- wow': '', 
                '+ wow': 'so much'
                }, 
            '  key': 'value', 
            '+ ops': 'vops'
            }
      }, 
    '  group1': {
        '- baz': 'bas', 
        '+ baz': 'bars', 
        '  foo': 'bar', 
        '- nest': {
            'key': 'value'
            }, 
        '+ nest': 'str'
      }, 
    '- group2': {
        'abc': 12345, 
        'deep': {
            'id': 45
            }
      }, 
    '+ group3': {
        'deep': {
            'id': {
                'number': 45
                }
            }, 
        'fee': 100500
        }
    })
)