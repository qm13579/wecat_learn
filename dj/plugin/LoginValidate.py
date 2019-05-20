import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dj.settings')
# import unittest
#
#
# class MyTestCase(unittest.TestCase):
#     def test_something(self):
#         self.assertEqual(True, False)
#
#
# if __name__ == '__main__':
#     unittest.main()
import hashlib
import random,string
from api.models import Session,UserProfile

def genRandomString(slen=40):
    return ''.join(random.sample(string.ascii_letters + string.digits, slen))

def session(username):
    """自定义session"""
    print(username)
    user=UserProfile.objects.get(email=username)
    obj=Session.objects.create(session_key=genRandomString(),session_value='',userprofile_id=1)
    return obj