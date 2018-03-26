import csv
import os

from app import app, get_db
from flask_assets import ManageAssets
from flask_script import Manager
from pymongo import MongoClient


manager = Manager(app)
manager.add_command('assets', ManageAssets())


@manager.command
def fix_dates():
    from datetime import datetime
    cur = get_db().users.find({}, {'_id': 1, 'registered_on': 1, 'confirmed_on': 1})
    for c in cur:
        if type(c['registered_on']) == str:
            print(f'original: {c["registered_on"]}')
            new_d = datetime.strptime(c['registered_on'], '%a, %d %b %Y %H:%M:%S %Z')
            get_db().users.update_one({'_id': c['_id']}, {'$set': {'registered_on': new_d}})
            print(f'fixed: {new_d}')
        if type(c['confirmed_on']) == str:
            print(f'original: {c["confirmed_on"]}')
            new_d = datetime.strptime(c['confirmed_on'], '%a, %d %b %Y %H:%M:%S %Z')
            get_db().users.update_one({'_id': c['_id']}, {'$set': {'confirmed_on': new_d}})
            print(f'fixed: {new_d}')


@manager.command
def drop_schools_():
    cur = get_db().users.find({'profile.school_': {'$exists': True}}, {'_id': 0, 'profile.school_': 1})
    for c in cur:
        print(c)


@manager.command
def complete_companies():
    path = os.path.join(os.path.dirname(__file__), 'data/Entreprises2018.csv')
    reader = csv.DictReader(open(path,'rt', encoding='utf8'), delimiter=';')
    for row in reader:
        get_db().companies.update_one({'id': row['id_entreprise']}, {'$set': {'info': row}})
        get_db().companies.update_one({'id': row['id_entreprise']}, {'$unset': {'info.id_entreprise': 1}})


@manager.command
def create_transport():
    get_db().users.update_many({}, {'$set': {'events.fra.transports': []}})


# set registred fra false for all users
@manager.command
def set_registered_false():
    get_db().users.update_many({}, {'$set' : {'events': {'fra': {'registered': False}, 'joi': {'registered': False }, 'styf': {'registered': False}, 'master_class':{'registered': False}}}})


# change admin password
@manager.command
def set_admin_password(password):
    get_db().companies.update_one({'id': 'admin'}, {'$set': {'password': password}})


# delete 2017 jobs
@manager.command
def delete_jobs():
    get_db().jobs.delete_many({})


# delete 2017 stream
@manager.command
def delete_stream():
    get_db().stream.delete_many({})


@manager.command
def update_event():
    get_db().events.delete_one({'id':"networking"})
    get_db().events.delete_one({'id':"conference"})
    get_db().events.insert_one({'image': "images/vie.jpg", 'id':"vie" , 'price':0, 'description':"Volontariat international en entreprise.", 'name' : "V.I.E."})


if __name__ == '__main__':
    manager.run()
