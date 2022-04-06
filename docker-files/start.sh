#!/bin/bash

/etc/init.d/redis-server start&
cd /APP/mdc/src && python2 sitsd.py&
