#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

if __name__ == "__main__":
    filepath = "/Users/tomohiro/Plactice/python"
    if os.path.exists(filepath):
        print "ファイルかディレクトリがある。"

        if os.path.isfile(filepath):
            print "指定のパスはファイルです。"

        if os.path.isdir(filepath):
            print "指定のパスはディレクトリです。"

    else:
        print "指定のファイルもしくはディレクトリは存在しません。"
