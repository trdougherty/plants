import datetime
import json

# import whatever sensor equiptment may be valuable

def gather_values():
    ### All the special sauce associated with collecting data
    return []

def read_json():
    json_body = []
    values = gather_values()
    time = datetime.datetime.now(datetime.timezone.utc).astimezone().isoformat()
    for value in values:
        element = {
            "measurement":value[0],
            "time":time,
            "fields": {
                "value":value[1]
            }
        }
        json_body.append(element)
    return json_body
