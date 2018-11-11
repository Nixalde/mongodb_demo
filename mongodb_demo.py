# -*- coding: utf-8 -*-
from bottle import route, run, request, redirect, post, get, template, static_file, error
import requests
import json
import pymongo
from sys import argv
import os
mykey=os.environ["KEY"]

@get('/')
def index():
return template('Index.tpl')

myclient = pymongo.MongoClient('mongodb://172.22.200.178:27017/')
mydb = myclient["test"]
mycol = mydb["personal"]

for x in mycol.find():
  return (x)

@error(404)
def error404(error):
    return 'Data not found'

run(host='0.0.0.0', port=argv[1])
