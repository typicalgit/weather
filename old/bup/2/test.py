#!/bin/python3
import datetime
import projutils as utils
import pprint

listy = []
date = datetime.datetime.now()

dom = date.strftime('%-d')
pprint.pprint(dom)

#suffix = utils.dayOfMonthSuffix()

