# coding:utf-8
class User:

    def __init__(self,email):
        '''
        initialize user class with email as user unique identifier
        :param email:
        '''
        self.email = email

    def get_id(self):
        '''
        return the unique identifier for the user which is email
        :return: user's email
        '''
        return self.email

    def is_active(self):
        '''
        we asume all created users are active
        :return: boolean
        '''
        return True

    def is_anonymous(self):
        '''
        we regards all created users are not anonymous
        :return: boolean
        '''
        return False

    def is_authenticated(self):
        '''
        all created users are authenticated as we only create the user object after the correct username and passwrod is entered
        :return: boolean
        '''
        return True