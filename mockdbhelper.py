MOCK_USERS = [{'email':'test@example.com',
              'salt': 'mddXZIP82y0uB70gMlW+VGYfeh0=',
              'hashed':'ba3253876aed6bc22d4a6ff53d8406c6ad864195ed144ab5c87621b6c233b548baeae6956df346ec8c17f5ea10f35ee3cbc514797ed7ddd3145464e2a0bab413'
              }]

class MockDBHelper:

    def get_user(self, email):
        user = [x for x in MOCK_USERS if x.get('email') == email]
        if user:
            return user[0]
        return None

    def add_user(self, email, salt, hashed):
        MOCK_USERS.append({'email':email, 'salt':salt, 'hashed':hashed})