import json
import datetime
class MyobjectEncoder(json.JSONEncoder):
    def default(self, obj):
        d = {}
        if not isinstance(obj,datetime.datetime):
           d['__class__'] = obj.__class__.__name__
           d['__module__'] = obj.__module__
           d.update(obj.__dict__)
        return d



class MyobjectDecoder(json.JSONDecoder):
    def __init__(self):
        json.JSONDecoder.__init__(self,object_hook=self.dict2object)
    def dict2object(self,d):
        if'__class__' in d:
            class_name = d.pop('__class__')
            module_name = d.pop('__module__')
            module = __import__(module_name)
            class_ = getattr(module,class_name)
            args = dict((key.encod('ascii'),value) for key,value in d.items())
            inst = class_(**args)
        else:
            inst = d
        return inst

