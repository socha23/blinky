import json

class Filestore:
    def __init__(self, path):
        self._path = path
        self._collections = {}
        self._load()

    def collection_names(self):
        return [k for k in self._collections.keys()]

    def put(self, collection, obj_id, value):
        if collection not in self._collections:
            self._collections[collection] = {}
        self._collections[collection][obj_id] = value
        self._save()

    def get(self, collection, obj_id):
        if collection in self._collections and obj_id in self._collections[collection]:
            return self._collections[collection][obj_id]
        else:
            return None

    def _load(self):
        try:
            file = open(self._path, 'r')
            self._collections = json.load(file)
            file.close()
        except FileNotFoundError:
            self._collections = {}

    def _save(self):
            file = open(self._path, 'w')
            json.dump(self._collections, file, indent=4)
            file.close()
