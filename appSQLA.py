import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from securitySQLA import authenticate,identity
from resources.userSQLA import UserRegister
from resources.itemSQLA import Item, ItemList
from resources.storeSQLA import Store, StoreList
from resources.det import Det, DetList

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=os.environ.get('DATABASE_URL','sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.secret_key='jose'
api=Api(app)

jwt=JWT(app,authenticate,identity)

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(Det, '/det')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')
api.add_resource(DetList, '/dets')
api.add_resource(UserRegister, '/register')

if __name__=='__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)