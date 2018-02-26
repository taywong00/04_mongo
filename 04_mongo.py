#!/usr/bin/python
# -*- coding: utf-8 -*-
from pymongo import MongoClient
import urllib2
import json

# Charles Weng, Taylor Wong
# SoftDev2 pd7
# K #04: Mi only nyam ital food, mon!
# 2018-02-15


'''
================================================================================
                                  setup
================================================================================
'''

c = MongoClient('lisa.stuy.edu', 27017)
test = c['test']
r = test['restaurants']


'''
================================================================================
                                 functions
                        test.returant parsing functions
================================================================================
'''


# search by borough
def find_b(b):
    d = r.find({'borough': b})
    for doc in d:
        print doc
    return d


# search by zipcode
def find_z(z):
    d = r.find({'address.zipcode': z})
    for doc in d:
        print doc
    return d


# search by zipcode
def find_zg(z, g):
    d = r.find({'$and': [{'address.zipcode': z}, {'grades.grade': g}]})
    for doc in d:
        print doc
    return d


# search by zipcode and score
def find_zs(z, s):
    d = r.find({'$and': [{"address.zipcode": str(z)}, {"grades.score": {'$lt': s}}]})
    for doc in d:
        print doc
    return d


# search by zipcode and cuisine type
def find_a(z, c):
    d = r.find({'$and': [{"address.zipcode": str(z)}, {"cuisine": c}]})
    for doc in d:
        print doc
    return d


'''
================================================================================
                                set up & functions 2
================================================================================
'''

db = c[u'+X米X+']
p = db['pokedex']
url = 'https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json'

# does data already exist
if(p.count() == 0):
    resp = urllib2.urlopen(url)
    dex = json.loads(resp.read())
    # print dex
    for poke in dex['pokemon']:
        p.insert_one(poke)

# searches by type
def find_t(t):
    d = p.find({"type": t})
    for doc in d:
        print doc
    return d


# searches by weaknesses
def find_w(w):
    d = p.find({"weaknesses": w})
    for doc in d:
        print doc
    return d


# searches by type and weaknesses
def find_tw(t, w):
    d = p.find({"$and": [{"type": t}, {"weaknesses": w}]})
    for doc in d:
        print doc
    return d


# searches by average spawns
def find_s(s):
    d = p.find({"avg_spawns": {"$lt": s}})
    for doc in d:
        print doc
    return d


'''
================================================================================
                                    tests
================================================================================
'''

# restaurant tests
if(False):
    find_b('Manhattan')  # very big
    find_z('10282')
    find_zg('10282', 'A')
    find_zs('10282', '11')
    find_a('10282', 'Chinese')


# pokedex tests
if(True):
    # find_t('Water')
    # find_w('Fire')
    # find_tw('Grass', 'Poison')
    find_s(2)
