import json


def cleandict(d):
    if not isinstance(d, dict):
        return d
    return dict((k, cleandict(v)) for k, v in d.iteritems() if (v is not None and v is not ''))


def to_json(obj):
    return json.dumps(cleandict(obj), default=lambda o: o.__dict__, sort_keys=True)
