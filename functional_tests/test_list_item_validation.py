from .base import FunctionalTest

class ItemValidationTest(FunctionalTest):

	def test_cannot_add_empty_list_items(self):
		# Edith goes to the home page and accidentally tries to submit 
		# am empty list item. She hits enter on the empty input box

		# The homepage refreshes, and there is an error message saying
		# that list items cannot be blank

		# She tries again with some test for the item, which now works

		# Perversely, she now decided to submit a second blank list item

		# She recieves a similar warning on the list page

		# And she can corrits it by filling some text in
		self.fail('write me!')
