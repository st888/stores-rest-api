from db import db

class DetModel(db.Model):
    __tablename__ = 'DET'

    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.String(200))
    username = db.Column(db.String(200))
    instrument = db.Column(db.String(200))
    record = db.Column(db.String(200))
    redcap_event_name = db.Column(db.String(200))
    redcap_data_access_group = db.Column(db.String(200))
    redcap_repeat_instance = db.Column(db.String(200))
    redcap_repeat_instrument = db.Column(db.String(200))
    redcap_url = db.Column(db.String(500))
    project_url = db.Column(db.String(500))

    def __init__(self, project_id,username,instrument,record,redcap_event_name,redcap_data_access_group,redcap_repeat_instance,redcap_repeat_instrument,redcap_url,project_url):
        self.project_id = project_id
        self.username = username
        self.instrument = instrument
        self.record = record
        self.redcap_event_name = redcap_event_name
        self.redcap_data_access_group = redcap_data_access_group
        self.redcap_repeat_instance = redcap_repeat_instance
        self.redcap_repeat_instrument = redcap_repeat_instrument
        self.redcap_url = redcap_url
        self.project_url = project_url
 
    def json(self):
        return {'project_id': self.project_id, 
                'username': self.username,
                'instrument': self.instrument,
                'record': self.record,
                'redcap_event_name': self.redcap_event_name,
                'redcap_data_access_group': self.redcap_data_access_group,
                'redcap_repeat_instance': self.redcap_repeat_instance,
                'redcap_repeat_instrument': self.redcap_repeat_instrument,
                'redcap_url': self.redcap_url,
                'project_url': self.project_url
            }

    @classmethod
    def find_by_projectid(cls, project_id):
        return cls.query.filter_by(project_id=project_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
