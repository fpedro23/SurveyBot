# coding=utf-8
__author__ = 'Pedro'
import random

from mechanize import *

br = Browser()
br.set_handle_robots(False)
br.set_handle_equiv(False)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 '
                                'Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

for x in range(0, 500):
    br.open("https://docs.google.com/forms/d/1p85e_083w1Wbc4No_PQWcDHTW1Lzag4kZVZ808Q0CDo/viewform?c=0&w=1")
    br.form = list(br.forms())[0]
    for control in br.form.controls:
        try:
            # print control
            br[control.name] = [control.items[random.randint(0, len(control.items) - 1)].name]

        except Exception as e:
            # print e
            if control.type == "text":
                br[control.name] = 'OLA K ASE'

    br.submit('submit')
    print x
    print br.response().code