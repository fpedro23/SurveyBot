__author__ = 'Pedro'
from mechanize import *

br = Browser()
br.set_handle_robots(False)
br.set_handle_equiv(False)
br.open("http://www.google.com/")
for f in br.forms():
    print f