# core/tests.py

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Booking

class BookingTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='testuser', password='password')
        self.booking = Booking.objects.create(user=self.user, route='Test Route', driver='Test Driver')

    def test_booking_confirmation(self):
        self.client.login(username='testuser', password='password')
        response = self.client.post(reverse('confirm_booking', args=[self.booking.id]))
        self.booking.refresh_from_db()
        self.assertTrue(self.booking.confirmed)
        self.assertRedirects(response, reverse('booking_success'))

    def test_booking_history(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('booking_history'))
        self.assertContains(response, 'Test Route')
