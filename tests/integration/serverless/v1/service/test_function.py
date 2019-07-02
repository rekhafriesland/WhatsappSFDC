# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class FunctionTestCase(IntegrationTestCase):

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.serverless.v1.services(sid="ZSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                     .functions.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://serverless.twilio.com/v1/Services/ZSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Functions',
        ))

    def test_read_empty_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "functions": [],
                "meta": {
                    "first_page_url": "https://serverless.twilio.com/v1/Services/ZS00000000000000000000000000000000/Functions?PageSize=50&Page=0",
                    "key": "functions",
                    "next_page_url": null,
                    "page": 0,
                    "page_size": 50,
                    "previous_page_url": null,
                    "url": "https://serverless.twilio.com/v1/Services/ZS00000000000000000000000000000000/Functions?PageSize=50&Page=0"
                }
            }
            '''
        ))

        actual = self.client.serverless.v1.services(sid="ZSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                          .functions.list()

        self.assertIsNotNone(actual)

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.serverless.v1.services(sid="ZSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                     .functions(sid="ZHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://serverless.twilio.com/v1/Services/ZSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Functions/ZHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "sid": "ZH00000000000000000000000000000000",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "service_sid": "ZS00000000000000000000000000000000",
                "friendly_name": "test-function",
                "date_created": "2018-11-10T20:00:00Z",
                "date_updated": "2018-11-10T20:00:00Z",
                "url": "https://serverless.twilio.com/v1/Services/ZS00000000000000000000000000000000/Functions/ZH00000000000000000000000000000000",
                "links": {
                    "function_versions": "https://serverless.twilio.com/v1/Services/ZS00000000000000000000000000000000/Functions/ZH00000000000000000000000000000000/Versions"
                }
            }
            '''
        ))

        actual = self.client.serverless.v1.services(sid="ZSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                          .functions(sid="ZHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.assertIsNotNone(actual)

    def test_create_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.serverless.v1.services(sid="ZSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                     .functions.create(friendly_name="friendly_name")

        values = {'FriendlyName': "friendly_name", }

        self.holodeck.assert_has_request(Request(
            'post',
            'https://serverless.twilio.com/v1/Services/ZSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Functions',
            data=values,
        ))

    def test_create_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "sid": "ZH00000000000000000000000000000000",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "service_sid": "ZS00000000000000000000000000000000",
                "friendly_name": "function-friendly",
                "date_created": "2018-11-10T20:00:00Z",
                "date_updated": "2018-11-10T20:00:00Z",
                "url": "https://serverless.twilio.com/v1/Services/ZS00000000000000000000000000000000/Functions/ZH00000000000000000000000000000000",
                "links": {
                    "function_versions": "https://serverless.twilio.com/v1/Services/ZS00000000000000000000000000000000/Functions/ZH00000000000000000000000000000000/Versions"
                }
            }
            '''
        ))

        actual = self.client.serverless.v1.services(sid="ZSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                          .functions.create(friendly_name="friendly_name")

        self.assertIsNotNone(actual)

    def test_update_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.serverless.v1.services(sid="ZSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                     .functions(sid="ZHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update(friendly_name="friendly_name")

        values = {'FriendlyName': "friendly_name", }

        self.holodeck.assert_has_request(Request(
            'post',
            'https://serverless.twilio.com/v1/Services/ZSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Functions/ZHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
            data=values,
        ))

    def test_update_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "sid": "ZH00000000000000000000000000000000",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "service_sid": "ZS00000000000000000000000000000000",
                "friendly_name": "function-friendly-update",
                "date_created": "2018-11-10T20:00:00Z",
                "date_updated": "2018-11-10T20:00:00Z",
                "url": "https://serverless.twilio.com/v1/Services/ZS00000000000000000000000000000000/Functions/ZH00000000000000000000000000000000",
                "links": {
                    "function_versions": "https://serverless.twilio.com/v1/Services/ZS00000000000000000000000000000000/Functions/ZH00000000000000000000000000000000/Versions"
                }
            }
            '''
        ))

        actual = self.client.serverless.v1.services(sid="ZSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                          .functions(sid="ZHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update(friendly_name="friendly_name")

        self.assertIsNotNone(actual)
