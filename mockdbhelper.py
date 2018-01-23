# coding:utf-8
import datetime
MOCK_USERS = [{'email':'test@example.com',
              'salt': '7J+crXckrID8rCG1PEWu+pJnG+4=',
              'hashed':'35fac70c6fe8e07628296a72942898efdbd030534681986ac5f03ddd0d5c8d584196f7e767e28da59faeb7b686cb5b202bfda74a0a7a73035898d59bcc2645d8'
              }]

MOCK_TABLES = [{'_id': '1',
                'number':'1',
                'owner':'test@example.com',
                'url':'mockrul'}]

MOCK_REQUESTS = [{'_id':'1',
                  'table_number':'1',
                  'table_id':'1',
                  'time':datetime.datetime.now()}]

class MockDBHelper:

    def get_user(self, email):
        user = [x for x in MOCK_USERS if x.get('email') == email]
        if user:
            return user[0]
        return None

    def add_user(self, email, salt, hashed):
        MOCK_USERS.append({'email':email, 'salt':salt, 'hashed':hashed})

    def add_table(self, number, owner):
        MOCK_TABLES.append({'_id':number, 'number':number,'owner':owner})
        return number

    def update_table(self, _id, url):
        for table in MOCK_TABLES:
            if table.get("_id") == _id:
                table['url'] = url
                break

    def get_tables(self, owner_id):
        return MOCK_TABLES

    def delete_table(self, table_id):
        for i, table in enumerate(MOCK_TABLES):
            if table.get('_id') == table_id:
                del MOCK_TABLES[i]
                break

    def add_request(self, number, datetime):
        MOCK_REQUESTS.append({'_id':number,
                             'table_number':number,
                             'table_id':number,
                             'time':datetime})
        return number

    def get_request(self, owner_id):
        return MOCK_REQUESTS

    def delete_request(self, request_id):
        for i, request in enumerate(MOCK_REQUESTS):
            if request.get('_id') == request_id:
                del MOCK_REQUESTS[i]
                break