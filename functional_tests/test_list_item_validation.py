from .base import FunctionalTest

class ItemValidationTest(FunctionalTest):

	def test_cannot_add_empty_list_items(self):
		# Edith goes to the home page and accidentally tries to submit 
		# am empty list item. She hits enter on the empty input box
		self.browser.get(self.server_url)
		self.browser.find_element_by_id('id_new_item').send_keys('\n')

		# The homepage refreshes, and there is an error message saying
		# that list items cannot be blank
		error = self.browser.find_element_by_css_selector('.has-error')
		self.assertEqual(error.text, "You can't have an empty list item")

		# She tries again with some test for the item, which now works
		self.browser.find_element_by_id('id_new_item').send_keys('Buy milk\n')
		self.check_for_row_in_list_table('1: Buy milk')

		# Perversely, she now decided to submit a second blank list item
		self.browser.find_element_by_id('id_new_item').send_keys('\n')

		# She recieves a similar warning on the list page
		self.check_for_row_in_list_table('1: Buy milk')
		error = self.browser.find_element_by_css_selector('.has-error')
		self.assertEqual(error.text, "You can't have an empty list item")

		# And she can corrits it by filling some text in
		self.browser.find_element_by_id('id_new_item').send_keys('Make tea\n')
		self.check_for_row_in_list_table('1: Buy milk')
		self.check_for_row_in_list_table('2: Make tea')
