#!/usr/bin/python2

from urllib import urlopen
import os
url="https://ipecho.net/plain"
x=urlopen(url)
pub = x.read()
print "Public IP:",pub
pri = os.popen('hostname -I').read()
print "Private IP:",pri
