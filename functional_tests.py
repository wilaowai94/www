from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
import unittest

class NewVisitorTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def test_can_start_list_retrieve_later(self):
		# Mitsy has learned of a cool new online to-do list app
		# She scurries to check out its homepage
		self.browser.get('http://localhost:8000')

		# She notices the page title and header mention to-do lists
		self.assertIn('To-Do', self.browser.title)

		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)

		# She is invited to enter a to-do item immediately
		input_box = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(input_box.get_attribute('placeholder'), 'Enter a to-do item')

		# She types "pee in a corner" into a text box
		# She loves rage peeing like a geriatric cat
		input_box.send_keys('pee in a corner')


		# When Mitsy hits enter, the page updates
		# Now the page lists "1: pee in a corner" as an item in the to-do list
		input_box.send_keys(Keys.ENTER)
		time.sleep(1)

		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertTrue(any(row.text == '1: pee in a corner' for row in rows))

		# There is still a text box inviting her to add another item
		# She enters "projectile vomit kibble on the carpet" 
		self.fail('Finish the test!')

		# The page updates again, and now shows both items on her list

		# Mitsy wonders whether the website will remember her list
		# Then she sees that the site has generated a unique URL for her
		# There is some explanatory text to that effect

		# She visits that URL - her to-do list is still there

		# Satisfied, she goes back to sleep for another 22 hours

if __name__ == '__main__':
	unittest.main()