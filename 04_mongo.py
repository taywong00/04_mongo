from pymongo import MongoClient

# Charles Weng, Taylor Wong# SoftDev2 pd7
# K #04: Mi only nyam ital food, mon!
# 2018-02-15


'''
================================================================================
                                  setup
================================================================================
'''

c = MongoClient('lisa.stuy.edu', 27017)
mfDB = c['test']
r = mfDB['restaurants']


'''
================================================================================
                                 functions
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
    d = r.find({'$and':[{"address.zipcode":str(z)}, {"grades.score": {'$lt': s}}]})
    for doc in d:
        print doc
    return d

# search by zipcode and cuisine type
def find_a(z, c):
    d = r.find({'$and':[{"address.zipcode":str(z)}, {"cuisine": cuisine}]})
    for doc in d:
        print doc
    return d


'''
================================================================================
                                      tests
================================================================================
'''

# find_b('Manhattan') # very big
find_z('10282')
find_zg('10282', 'A')
find_zs('10282', '11')
find_a('10282', 'Chinese'):
                                                
