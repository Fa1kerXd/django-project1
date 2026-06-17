from unittest import TestCase

from utils.pagination import make_pagination_range


class PaginationClassTest(TestCase):
    def test_make_pagination_range_returns_a_pagination_range(self):
        pagination_range = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_page=4,
            current_page=1
        )['pagination']
        self.assertEqual([1, 2, 3, 4], pagination_range)

    def test_first_range_is_static_if_current_page_is_less_than_middle_page(self):  # noqa: E501
        pagination_range = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_page=4,
            current_page=1
        )['pagination']
        self.assertEqual([1, 2, 3, 4], pagination_range)

        pagination_range = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_page=4,
            current_page=2
        )['pagination']
        self.assertEqual([1, 2, 3, 4], pagination_range)

        pagination_range = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_page=4,
            current_page=3
        )['pagination']
        self.assertEqual([2, 3, 4, 5], pagination_range)
    
    def test_make_pagination_range_is_static_when_last_page_is_next(self):
        pagination_range = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_page=4,
            current_page=21
        )['pagination']
        self.assertEqual([17, 18, 19, 20], pagination_range)
