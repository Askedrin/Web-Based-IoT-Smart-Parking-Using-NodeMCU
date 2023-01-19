from datetime import datetime
from mongoengine import (Document,
                        DateTimeField,
                         ReferenceField)

from models.rfid_data import RFID
from models.clients import Clients


class Logs(Document):
    client = ReferenceField(Clients)
    entry_date = DateTimeField(default=datetime.now)
    exit_date = DateTimeField(default=None)
    used_tag=ReferenceField(RFID)
    


   







