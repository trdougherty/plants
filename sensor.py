import datetime
import json

# import whatever sensor equiptment may be valuable

def gather_values():
    ### All the special sauce associated with collecting data
    ### Returns a list of two value tuples, with the first entry as a string and second as a value
    return []

def get_tags():
    ## Add flavors to the data for filtering later
    return {}

def read_json():
    json_body = []
    values = gather_values()
    time = datetime.datetime.now(datetime.timezone.utc).astimezone().isoformat()
    for value in values:
        element = {
            "measurement":value[0],
            "tags": get_tags(),
            "time":time,
            "fields": {
                "value":value[1]
            }
        }
        json_body.append(element)
    return json_body
