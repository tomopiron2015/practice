#!/usr/bin/python
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    f = open("text","r")

    for stout in f:
        print stout

    f.close()


