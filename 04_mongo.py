from pymongo import MongoClient

c = MongoClient('lisa.stuy.edu', 27017)
mfDB = c['test']
r = mfDB['restaurants']


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


# tests
# find_b('Manhattan') # very big
find_z('10282')
find_zg('10282', 'A')
