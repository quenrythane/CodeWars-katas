# https://www.codewars.com/kata/515bb423de843ea99400000a
"""
For this exercise you will be strengthening your page-fu mastery. You will complete the PaginationHelper class, which
is a utility class helpful for querying paging information related to an array.

The class is designed to take in an array of values and an integer indicating how many items will be allowed per each
page. The types of values contained within the collection/array are not relevant.


The following are some examples of how this class is used:

helper = PaginationHelper(['a','b','c','d','e','f'], 4)
helper.page_count() # should == 2
helper.item_count() # should == 6
helper.page_item_count(0)  # should == 4
helper.page_item_count(1) # last page - should == 2
helper.page_item_count(2) # should == -1 since the page is invalid

# page_index takes an item index and returns the page that it belongs on
helper.page_index(5) # should == 1 (zero based index)
helper.page_index(2) # should == 0
helper.page_index(20) # should == -1
helper.page_index(-10) # should == -1 because negative indexes are invalid
"""


class PaginationHelper:

    # The constructor takes in an array of items and a integer indicating how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.item_per_page = items_per_page

    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.collection)

    # returns the number of pages
    def page_count(self):
        from math import ceil
        return ceil(len(self.collection) / self.item_per_page)
        # return -(len(self.collection) // -self.item_per_page) <- alternative

    # returns the number of items on the current page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        # return -1 if page_index >= 2 else item_count - ((page_index + 1) * items_per_page)
        if page_index >= self.page_count():
            return -1
        else:
            return self.item_per_page if self.item_per_page < self.item_count() - self.item_per_page * page_index \
                else self.item_count() - self.item_per_page * page_index
        # return min(self.items_per_page, len(self.collection) - page_index * self.items_per_page) \
        #             if 0 <= page_index < self.page_count() else -1  <- alternative

    # determines what page an item is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        return item_index//self.item_per_page if 0 <= item_index < self.item_count() else -1


helper = PaginationHelper(['a', 'b', 'c', 'd', 'e', 'f'], 4)
print(helper.page_index(-23), 'should == -1 \n')

print(
    helper.page_count(), 'should == 2 \n',
    helper.item_count(), 'should == 6 \n',
    helper.page_item_count(0), 'should == 4 \n',
    helper.page_item_count(1), 'should == 2 \n',
    helper.page_item_count(2), "should == -1 since the page is invalid \n",
    helper.page_index(5), '\n')

helper2 = PaginationHelper(['a', 'b', 'c', 'd', 'e', 'a', 'b', 'c', 'd', 'e'], 4)
print(
    helper2.page_count(), 'should == 3 \n',
    helper2.item_count(), 'should == 10 \n',
    helper2.page_item_count(0), 'should == 4 \n',
    helper2.page_item_count(1), 'should == 4 \n',
    helper2.page_item_count(2), 'should == 2 \n',
    helper2.page_item_count(3), "should == -1 since the page is invalid \n",
    helper2.page_index(9), '\n')
