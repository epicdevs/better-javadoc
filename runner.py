# -*- coding: utf-8 -*-
import os
import sys
import shutil

rep = '''
<!-- ======== START OF BETTER-JAVADOC ======== -->
<link rel="stylesheet" type="text/css" href="/better-javadoc-example/better-javadoc.css">
<script type="text/javascript" src="/better-javadoc-example/better-javadoc.js"></script>
<!-- ======== END OF BETTER-JAVADOC ======== -->
'''

def list_files(dir):
    list = []
    for dpath, _, files in os.walk(dir):
        list.extend([os.path.join(dpath, file) for file in files])
    return list

def filter_by_ext(list):
    return filter(lambda x: x.endswith('.html'), list)

if __name__ == '__main__':
    dir = sys.argv[1]
    files = filter_by_ext(list_files(dir))

    hint = '<!-- ======== END OF BOTTOM NAVBAR ======= -->'
    for file in files:
        f_r = open(file, 'r')
        content = f_r.read()
        f_r.close()

        loc = content.find(hint)
        if loc != -1:
            f_w = open(file, 'w')
            f_w.write(content[:loc + len(hint) + 1] + rep + content[loc + len(hint):])
            f_w.close()
