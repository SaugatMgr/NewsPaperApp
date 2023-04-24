from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

# Create your tests here.

class SignUpPageExists(TestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get('/accounts/signup/')
        
        self.assertEqual(response.status_code, 200)
        
    def test_signup_view_name(self):
        response = self.client.get(reverse('signup'))
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/signup.html')
        
    def test_signup_form(self):
        response = self.client.post(
            reverse('signup'),
            {
                'username': 'test_user',
                'email': 'test_user@email.com',
                'password1': 'pwd_test123',
                'password2': 'pwd_test123',
            }
        )
        
        self.assertEqual(response.status_code, 302)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, 'test_user')
        self.assertEqual(get_user_model().objects.all()[0].email, 'test_user@email.com')