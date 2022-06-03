from django.test import TestCase
from django.contrib.auth import get_user_model


class UserTest(TestCase):

    def test_create_superuser(self):
        db = get_user_model()
        superuser = db.objects.create_superuser(
            email='admin@admin.fr', username='username', password='password', is_superuser=False, is_active=False,
            is_staff=False
        )
        self.assertEqual(superuser.email, 'admin@admin.fr')
        self.assertEqual(superuser.username, 'username')
        self.assertTrue(superuser.is_superuser)
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_active)

        self.assertEqual(str(superuser), 'username')


    def test_create_user(self):
        db = get_user_model()
        user = db.objects.create_user(
            email='user@user.fr', username='user', password='password'
        )
        self.assertEqual(user.email, 'user@user.fr')
        self.assertEqual(user.username, 'user')
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_active)

        # with self.assertRaises(ValueError):
        #     db.objects.create_user(
        #         email='admin', username='user2', password='password'
        #     )

        with self.assertRaises(ValueError):
            db.objects.create_user(
                email='', username='user3', password='password'
            )

