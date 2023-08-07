##importing necessary libraries
from flask import Flask,jsonify,Blueprint
from flask_restful import Resource,Api,reqparse
from flask_pymongo import PyMongo

app=Flask(__name__)

##creating blueprint
api_crud = Blueprint('crud', __name__)
api=Api(api_crud)


##connecting to Mongodb Atlas
app.config['MONGO_URI']="mongodb_link"
mongo = PyMongo(app)
##creating collection in mongodb
my_coll=mongo.db.user_docs

###  arguements for crud operations
inserting_user = reqparse.RequestParser()
inserting_user.add_argument('unique_id', type=str, required=True)
inserting_user.add_argument('name', type=str, required=True)
inserting_user.add_argument('email_id', type=str, required=True)
inserting_user.add_argument('password', type=str, required=True)

update_user=reqparse.RequestParser()
update_user.add_argument('unique_id', type=str)
update_user.add_argument('name', type=str)
update_user.add_argument('email_id', type=str)
update_user.add_argument('password', type=str)


class user(Resource):
    ##adding_user to mongodb
    def post(self):
        try:
            args = inserting_user.parse_args()
            unique_id= args['unique_id']
            name = args['name']
            email_id = args['email_id']
            password = args['password']
            #print(unique_id, email_id, name, password)
            user_details = {'unique_id': unique_id, 'name': name, 'email_id': email_id, 'password': password}
            my_coll.insert_one(user_details)
        except:
            return jsonify(str("enter all the values"))
        else:
            return jsonify(str("user_records inserted"))
            
    ##updating user
    def put(self):
        try:
            args=update_user.parse_args()
            filter = {"unique_id": args['unique_id']}
            for key, value in args.items():
                if key!=None and value!=None:
                    #print(key, value)
                    updates = {'$set': {key: value}}
                    my_coll.update_one(filter, updates)
        except:
            return jsonify(str("enter data to be updated"))
        else:
            return jsonify(str(my_coll.find_one(filter)))

    ##deleting user from  mongodb
    def delete(self,unique_id):
        try:
            records = my_coll.find_one({'unique_id': unique_id})
        except Exception as e:
            return e
        else:
            if records:
                my_coll.delete_one({'unique_id': unique_id})
                return jsonify(str("record deleted"))
            else:
                return jsonify(str("no record found"))


class get_user(Resource):
    ## fetching all users from mongodb
    def post(self):
        documnets = []
        try:
            for docs in my_coll.find():
                documnets.append(docs)
        except Exception as e:
            return e
        else:
            if documnets:
                return jsonify(str(documnets))
            else:
                return jsonify(str("no records"))

    ## fetching one user from mongodb
    def get(self,unique_id):
        try:
            filter = {'unique_id': unique_id}
            records = my_coll.find_one(filter)
        except  Exception as e:
            return e
        else:
            if records:
                return jsonify(str(records))
            else:
                return jsonify(str("no record found"))


api.add_resource(user,"/insert_user","/update","/delete/<string:unique_id>")
api.add_resource(get_user,"/get_all","/get_one/<string:unique_id>")

app.register_blueprint(api_crud,url_prefix="/api")

if __name__=="__main__":
    (app.run(debug=True))
