from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string

from lists.views import home_page
from lists.models import Item

# Create your tests here.

class HomePageTest(TestCase):

	def test_uses_home_template(self):

		response = self.client.get('/')
		html = response.content.decode('utf8')

		self.assertTemplateUsed(response, 'home.html')

	def test_only_save_items_necessary(self):
		self.client.get('/')
		self.assertEqual(Item.objects.count(), 0)

	def test_can_save_post_request(self):

		response = self.client.post('/', data={'item_text':'A new list item'})

		self.assertEqual(Item.objects.count(), 1)
		new_item = Item.objects.first()
		self.assertEqual(new_item.text, 'A new list item')

	def test_redirects_after_post(self):

		response = self.client.post('/', data={'item_text':'A new list item'})

		self.assertEqual(response.status_code, 302)
		self.assertEqual(response['location'], '/')

	def test_all_list_items_display(self):
		Item.objects.create(text='item numba one')
		Item.objects.create(text='item numba two')

		response = self.client.get('/')

		self.assertIn('item numba one', response.content.decode())
		self.assertIn('item numba two', response.content.decode())

class ItemModelTest(TestCase):

	def test_saving_retrieving_items(self):

		first_item = Item()
		first_item.text = 'The first (ever) list item'
		first_item.save()

		second_item = Item()
		second_item.text = 'Item the second'
		second_item.save()

		saved_items = Item.objects.all()
		self.assertEqual(saved_items.count(), 2)

		first_saved_item = saved_items[0]
		second_saved_item = saved_items[1]

		self.assertEqual(first_saved_item.text, 'The first (ever) list item')
		self.assertEqual(second_saved_item.text, 'Item the second')


