# -*- coding:utf-8 -*-
import os
import sys
import re
import time


# extract extension name
def get_file_extension(path):
    return os.path.splitext(path)[1]


# recursively extract all files in the changed directory
def get_all_file(path):
    all_file_list = [];

    # Allowed extension
    alllow_filee_xtension = ['.html', '.htm', '.shtml'];

    # recursive extraction of all paths of a file
    for root, dirs, files in os.walk(path):
        for name in files:
            filePath = os.path.join(root, name)
            if (get_file_extension(filePath) in alllow_filee_xtension):
                all_file_list.append(filePath)

    return all_file_list


def add_version_number(path, number):
    try:
        hand = open(path, "r+")
        content = hand.read()

        # replace css
        pattern_css = '<link href="(.*?)\.css(.*?)"'
        replace_css = r'<link href="\1.css?v=%s"' % (number);
        out = re.sub(pattern_css, replace_css, content)

        # replace javascript
        pattern_css = '<script src="(.*?)\.js(.*?)"'
        replace_css = r'<script src="\1.js?v=%s"' % (number);
        out = re.sub(pattern_css, replace_css, out)

        # save file
        hand.seek(0)
        hand.write(out)
    except Exception as err:
        print('file:%s,error:%s' % (path, err))
    finally:
        hand.close()

    return out


# main
if __name__ == '__main__':
    html_path = ''
    number = time.strftime('%Y%m%d%H', time.localtime(time.time()))
    args = sys.argv

    try:
        html_path = args[1]
        number = args[2]
    except Exception as err:
        print('param can not empaty')
        sys.exit()

    all_file_list = get_all_file(html_path)
    for file in all_file_list:
        add_version_number(file, number)
        print('Processing files %s' % (file))

    print('done!')
