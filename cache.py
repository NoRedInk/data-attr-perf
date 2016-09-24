#!/usr/bin/env python3
'''
Cache testcases.
'''
import os.path
import urllib.parse
import urllib.request


CACHE_DIR = 'cache'


def download_testcase(**params):
    query_params = {k: v for k, v in params.items() if v}
    url = 'http://10.0.1.8:4567/?' + urllib.parse.urlencode(query_params)
    filename = format_filename(**params)
    dest = os.path.join(CACHE_DIR, filename)
    print(dest)
    if not os.path.exists(dest):
        urllib.request.urlretrieve(url, dest)
        print('ok downloaded')
    else:
        print('ok cached')


def format_filename(**params):
    return 'w{w}xh{h}xd{d}.html'.format(**params)


def main():
    os.makedirs(CACHE_DIR, exist_ok=True)
    dimensions = ['w', 'h', 'd']
    baselines = [1, 10, 100]
    prev_filename = None
    for baseline_value in baselines:
        defaults = {dimension: baseline_value for dimension in dimensions}
        for dimension_to_drill in dimensions:
            if baseline_value < 100:
                drill_values = [100, 1000, 10000]
            else:
                drill_values = [1000]
            for dimension_value in drill_values:
                params = dict(defaults)
                params[dimension_to_drill] = dimension_value
                if params['d'] >= 1000:
                    # ruby 2.2.3 stack overflows in this case: skip
                    continue
                # FIXME: there's a gap somewhere and w1000xh100xd100.html is not in the chain
                # probably because 100x100x100 is visited multiple times?
                params['prev_filename'] = prev_filename
                download_testcase(**params)
                prev_filename = format_filename(**params)


if __name__ == '__main__':
    main()
