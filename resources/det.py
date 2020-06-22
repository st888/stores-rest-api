from flask_restful import Resource,reqparse
from models.det import DetModel

class Det(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument('username',type=str)
    parser.add_argument('instrument',type=str)
    parser.add_argument('record',type=str)
    parser.add_argument('redcap_event_name',type=str)
    parser.add_argument('redcap_data_access_group',type=str)
    parser.add_argument('redcap_repeat_instance',type=str)
    parser.add_argument('redcap_repeat_instrument',type=str)
    parser.add_argument('redcap_url',type=str)
    parser.add_argument('project_url',type=str)

    def get(self,project_id):
        det=DetModel.find_by_projectid(project_id)
        if det:
            return det.json()
        return{'message':"The det does not exist"},404  
        
    
    def post(self,project_id):
        if DetModel.find_by_projectid(project_id):
            return {'message': "An project id with name '{}' already exists.".format(project_id)},400

        data=Det.parser.parse_args()
        det=DetModel(project_id,data['username'],data['instrument'],data['record'],data['redcap_event_name'],data['redcap_data_access_group'],data['redcap_repeat_instance'],data['redcap_repeat_instrument'],data['redcap_url'],data['project_url'])

        try:
            det.save_to_db()
        except:
            return {"message":"An error occurred inserting the det."} ,500
        return det.json(),201

           
    def delete(self,project_id):
        det=DetModel.find_by_projectid(project_id)
        if det:
            det.delete_from_db()
    
        return {'message': 'The det is deleted'}

    
class DetList(Resource):
    def get(self):
       return {'Dets': [det.json() for det in DetModel.query.all()]}