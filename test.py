#!/Users/yuanyuanliu/miniconda3/envs/flask/bin/python

import os
import unittest
from config import basedir
from app import app, db
from app.models import User


class TestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLES'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
            os.path.join(basedir, 'test.db')
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_avatar(self):
        u = User(social_id="abcd", nickname='john', email='john@example.com')
        avatar = u.avatar(128)
        expected = 'http://www.gravatar.com/avatar/d4c74594d841139328695756648b6bd6'
        assert avatar[:len(expected)] == expected

    def test_make_unique_nickname(self):
        u = User(social_id='abcd', nickname='john', email='john@example.com')
        db.session.add(u)
        db.session.commit()

        nickname = User.make_unique_nickname('john')
        u = User(social_id="efg", nickname=nickname, email='susam@example.com')
        db.session.add(u)
        db.session.commit()
        assert nickname != 'john'
        nickname2 = User.make_unique_nickname('john')
        assert nickname2 != 'john'
        assert nickname2 != nickname

if __name__ == "__main__":
    unittest.main(verbosity=2)
