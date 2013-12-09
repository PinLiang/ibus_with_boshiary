#!/usr/bin/python
# -*- coding: UTF-8
soruce = '/home/munch/下載/ibus版嘸蝦米-liu5/ibus安裝版/liu5.db'
destination = '/usr/share/ibus-table/tables/liu5.db'
source2 = '/home/munch/下載/ibus版嘸蝦米-liu5/ibus安裝版/liu5.png'
destination2 = '/usr/share/ibus-table/icons/liu5.png'
cmd = 'sudo service ibus'
import shutil

shutil.copy2(soruce, destination)
shutil.copy2(source2, destination2)
