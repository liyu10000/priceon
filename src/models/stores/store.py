import uuid
from src.common.database import Database
import src.models.stores.constants as StoreConstants
import src.models.stores.errors as StoreErrors

class Store(object):

    def __init__(self, name, url_prefix, tag_name, query, _id=None):
        # Amazon: <span id="priceblock_ourprice" class="a-size-medium a-color-price">$1,375.00</span>
        self.name = name
        self.url_prefix = url_prefix
        self.tag_name = tag_name
        self.query = query
        self._id = uuid.uuid4().hex if _id is None else _id

    def __repr__(self):
        return "<Store {}>".format(self.name)

    def json(self):
        return {
            "_id": self._id,
            "name": self.name,
            "url_prefix": self.url_prefix,
            "tag_name": self.tag_name,
            "query": self.query
        }

    @classmethod
    def get_by_id(cls, _id):
        return cls(**Database.find_one(StoreConstants.COLLECTION, {"_id": _id}))

    def save_to_mongo(self):
        Database.update(StoreConstants.COLLECTION, {"_id": self._id}, self.json())

    @classmethod
    def get_by_name(cls, name):
        return cls(**Database.find_one(StoreConstants.COLLECTION, {"name": name}))

    @classmethod
    def get_by_url_prefix(cls, url_prefix):
        """
        http://www.amazon -> http://wwww.amazon.com
        :param url_prefix:
        :return:
        """
        # {"$regex": '^{}'.format(url_prefix)}: the regex mongo uses
        return cls(**Database.find_one(StoreConstants.COLLECTION, {"url_prefix": {"$regex": '^{}'.format(url_prefix)}}))

    @classmethod
    def find_by_url(cls, url):
        """
        Return a store from a complete url
        :param url: the item's url
        :return: a Store, or raises a StoreNotFoundException if no store matches the url
        """
        i = len(url) + 1
        while i >= 0:
            try:
                if Database.find_one(StoreConstants.COLLECTION,
                                     {'url_prefix': {"$regex": '^{}'.format(url[:i])}}) is not None:
                    store = cls.get_by_url_prefix(url[:i])
                    return store
                i = i - 1
            except:
                raise StoreErrors.StoreNotFoundException(
                    "The URL Prefix used to find the store did not fetch any results")


    @classmethod
    def all(cls):
        return [cls(**elem) for elem in Database.find(StoreConstants.COLLECTION, {})]

    def delete(self):
        Database.remove(StoreConstants.COLLECTION, {"_id": self._id})