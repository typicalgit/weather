#!/usr/bin/env python3
import io3 as io
import datetime as dt

now = dt.datetime.now()

listy = [['a','1'],['b','2'],['c','3']]
dicky = dict(listy)

dicky['time'] = now

io.write_object(dicky,'dickytest','json')
imp = io.load_object('dickytest.csv')

print(dicky)
print(imp)
