# -*- coding: utf-8 -*-

import unittest

from mock import call, patch
from nose.tools import eq_, istest

from intercom.client import Client
from tests.unit import page_of_contacts


class CollectionProxyTest(unittest.TestCase):

    def setUp(self):
        self.client = Client()

    @istest
    def it_stops_iterating_if_no_next_link(self):
        body = page_of_contacts(include_next_link=False)
        with patch.object(Client, 'get', return_value=body) as mock_method:
            emails = [contact.email for contact in self.client.contacts.all()]
            mock_method.assert_called_once_with('/contacts', {})
            eq_(emails, ['user1@example.com', 'user2@example.com', 'user3@example.com'])  # noqa

    @istest
    def it_keeps_iterating_if_next_link(self):
        page1 = page_of_contacts(include_next_link=True)
        page2 = page_of_contacts(include_next_link=False)
        side_effect = [page1, page2]
        with patch.object(Client, 'get', side_effect=side_effect) as mock_method:  # noqa
            emails = [contact.email for contact in self.client.contacts.all()]
            eq_([call('/contacts', {}), call('/contacts?per_page=50&page=2', {})],  # noqa
                mock_method.mock_calls)
            eq_(emails, ['user1@example.com', 'user2@example.com', 'user3@example.com'] * 2)  # noqa

    @istest
    def it_supports_indexed_array_access(self):
        body = page_of_contacts(include_next_link=False)
        with patch.object(Client, 'get', return_value=body) as mock_method:
            eq_(self.client.contacts.all()[0].email, 'user1@example.com')
            mock_method.assert_called_once_with('/contacts', {})

    @istest
    def it_supports_querying(self):
        body = page_of_contacts(include_next_link=False)
        with patch.object(Client, 'get', return_value=body) as mock_method:
            emails = [contact.email for contact in self.client.contacts.find_all(tag_name='Taggart J')]  # noqa
            eq_(emails, ['user1@example.com', 'user2@example.com', 'user3@example.com'])  # noqa
            mock_method.assert_called_once_with('/contacts', {'tag_name': 'Taggart J'})  # noqa
