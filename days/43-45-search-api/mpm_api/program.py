import api
import re

import cProfile
profiler = cProfile.Profile()
profiler.disable()


chars = {'&#8222;': '"',
         '&#8220;': '"',
         '&#8211;': '-',
         '&nbsp;': ' '
         }

def replace_multiple(old_string, chars_dict):
    for key, value in chars_dict.items():
        if key in old_string:
            old_string = old_string.replace(key, value)
    return old_string

def parse_mpm(mpm_json):
    for item in mpm_json:
        # print(item)
        line = re.sub(r'(<[^>]*>)', r'\0', item)
        r = replace_multiple(line, chars)
        print(r)

if __name__ == '__main__':
    profiler.enable()
    results = api.get_results_from_api()
    print(parse_mpm(results))
    profiler.disable()
    profiler.print_stats(sort='cumtime')