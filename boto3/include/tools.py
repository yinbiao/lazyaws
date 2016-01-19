# -*- coding=utf-8 -*-
#!/bin/env python

'''
aws的CreateDate值是：datetime.datetime(2015, 12, 3, 1, 55, 14, tzinfo=tzutc())
'''
import sys
import datetime
from dateutil.tz import tzutc


def die(msg):
    print msg
    sys.exit()

def fprint(obj,l=0):
    space = ' ' * (l*4)
    if type(obj) == type({}):
        for k,v in obj.items():
            if type(v) == type("") or type(v) == type(u""):
                print space + k + " : " + repr(v)
            elif type(v) == type(datetime.datetime(2015,12,3)):
                print space + k + " : " + v.strftime('%y-%m-%d %H:%M:%S')
            else:
                print space + k + " : "
                fprint(v,l+1)
    if type(obj) == type([]):
        for item in obj:
            if type(item) == type("") or type(item) == type(u""):
                print space + repr(item)
            elif type(item) == type(datetime.datetime(2015,12,3)):
                print space + item.strftime('%y-%m-%d %H:%M:%S')
            else:
                fprint(item, l+1)

def convertvar(v):
    _action = {}
    if isinstance(v, str):
        _action['type'] = 'str'
        _action['v'] = v
    elif isinstance(v, list):
        _action['type'] = 'list'
        _action['v'] = v
    elif v == None:
        _action = None
    else:
        die("unsupport value: " + repr(v))
    return _action


