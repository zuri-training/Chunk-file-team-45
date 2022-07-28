from django.test import TestCase
from user.models import Profile
from django.contrib.auth.models import User



class ProfileTestCase(TestCase):

    def setUp(self) -> None:
        ins = User.objects.create_user(
            username='Testing User',
            email='test@gmail.com',
            password='test1234'
        )
        Profile.objects.create(
            user=ins,
            location='Lagos',
        )
    
    def test_profile_object_created(self):
        """
        Test checks an object of Profile was 
        sucessfully created.
        """
        obj = Profile.objects.get(pk=1)
        check = 'Testing User'

        self.assertIsInstance(obj, Profile)
        self.assertEqual(obj.__str__(), check)

    def test_profile_object_not_created(self):
        """
        Test checks if the object created is not
        an instance of Profile 
        """

        obj = Profile.objects.get(pk=1)

        self.assertNotIsInstance('Dummy data', Profile)
        self.assertNotEqual(obj.__str__(), 'Dummy data')

    def test_data_for_instance(self):
        """
        Testing an instance data is correct
        """
        ins = Profile.objects.get(pk=1)

        self.assertEqual(ins.location, 'Lagos')

    def test_data_not_for_instance(self):
        """
        Testing an instance data is not correct
        """
        ins = Profile.objects.get(pk=1)

        self.assertNotEqual(ins.location, 'This is not your data')
