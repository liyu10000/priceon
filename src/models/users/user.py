import uuid
from src.common.database import Database
from src.common.utils import Utils
import src.models.users.errors as UserErrors
import src.models.users.constants as UserConstants
from src.models.alerts.alert import Alert


class User(object):

    def __init__(self, email, password, _id=None):
        self.email = email
        self.password = password
        self._id = uuid.uuid4().hex if _id is None else _id

    def __repr__(self):
        return "<User {}>".format(self.email)

    @staticmethod
    def is_login_valid(email, password):
        """
        This method verifies that an email/password combo (as sent by the site forms) is valid or not.
        Checks that the email exists, and that the password associated to that email is correct.
        :param email: the user's email
        :param password: a sha512 hashed password
        :return: True if valid, False otherwise
        """

        user_data = Database.find_one(UserConstants.COLLECTION, {"email": email})  # password in sha512->pbkdf2_sha512
        if user_data is None:
            # email doesn't exist
            raise UserErrors.UserNotExistsError("User does not exist.")
        if not Utils.check_hashed_password(password, user_data['password']):
            # password is wrong
            raise UserErrors.IncorrectPasswordError("Wrong password.")

        return True

    @staticmethod
    def register_user(email, password):
        """
        This methods registers a user using email and password
        The password already comes hashing as sha-512
        :param email: user's email (might be invalid)
        :param password: sha512-hashed password
        :return: True if registered successfully, or False otherwise (exceptions can also be raised)
        """
        user_data = Database.find_one(UserConstants.COLLECTION, {"email": email})  # password in sha512->pbkdf2_sha512
        if user_data is not None:
            # user is already registered
            raise UserErrors.UserAlreadyRegisteredError("The email has already been registered.")
        if not Utils.email_is_valid(email):  # ^[\w-]+@([\w-]+\.)+[\w]+$ for liyu10000@pku.edu.cn
            # the email is not constructed properly
            raise UserErrors.InvalidEmailError("The email does not have the right format")

        User(email, Utils.hash_password(password)).save_to_db()

        return True

    def save_to_db(self):
        Database.insert(UserConstants.COLLECTION, self.json())

    def json(self):
        return {
            "_id": self._id,
            "email": self.email,
            "password": self.password
        }

    @classmethod
    def find_by_email(cls, email):
        return cls(**Database.find_one(UserConstants.COLLECTION, {'email': email}))

    def get_alerts(self):
        return Alert.find_by_user_email(self.email)