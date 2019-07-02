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


class ConferenceTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.api.v2010.accounts(sid="ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .conferences(sid="CFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://api.twilio.com/2010-04-01/Accounts/ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Conferences/CFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.json',
        ))

    def test_fetch_valid_mixer_zone_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "api_version": "2010-04-01",
                "date_created": "Fri, 18 Feb 2011 19:26:50 +0000",
                "date_updated": "Fri, 18 Feb 2011 19:27:33 +0000",
                "friendly_name": "AHH YEAH",
                "sid": "CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "region": "us1",
                "status": "completed",
                "subresource_uris": {
                    "participants": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants.json",
                    "recordings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings.json"
                },
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
            }
            '''
        ))

        actual = self.client.api.v2010.accounts(sid="ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .conferences(sid="CFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.assertIsNotNone(actual)

    def test_fetch_valid_region_in_progress_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "api_version": "2010-04-01",
                "date_created": "Fri, 18 Feb 2011 19:26:50 +0000",
                "date_updated": "Fri, 18 Feb 2011 19:27:33 +0000",
                "friendly_name": "AHH YEAH",
                "sid": "CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "region": "au1",
                "status": "in-progress",
                "subresource_uris": {
                    "participants": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants.json",
                    "recordings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings.json"
                },
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
            }
            '''
        ))

        actual = self.client.api.v2010.accounts(sid="ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .conferences(sid="CFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.assertIsNotNone(actual)

    def test_fetch_without_mixer_zone_integer_status_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "api_version": "2010-04-01",
                "date_created": "Fri, 18 Feb 2011 19:26:50 +0000",
                "date_updated": "Fri, 18 Feb 2011 19:27:33 +0000",
                "friendly_name": "AHH YEAH",
                "sid": "CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "region": "us1",
                "status": "completed",
                "subresource_uris": {
                    "participants": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants.json",
                    "recordings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings.json"
                },
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
            }
            '''
        ))

        actual = self.client.api.v2010.accounts(sid="ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .conferences(sid="CFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.assertIsNotNone(actual)

    def test_fetch_unknown_mixer_zone_init_integer_status_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "api_version": "2010-04-01",
                "date_created": "Fri, 18 Feb 2011 19:26:50 +0000",
                "date_updated": "Fri, 18 Feb 2011 19:27:33 +0000",
                "friendly_name": "AHH YEAH",
                "sid": "CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "region": "unknown",
                "status": "init",
                "subresource_uris": {
                    "participants": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants.json",
                    "recordings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings.json"
                },
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
            }
            '''
        ))

        actual = self.client.api.v2010.accounts(sid="ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .conferences(sid="CFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.assertIsNotNone(actual)

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.api.v2010.accounts(sid="ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .conferences.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://api.twilio.com/2010-04-01/Accounts/ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Conferences.json',
        ))

    def test_read_empty_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "conferences": [],
                "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences.json?Status=init&DateUpdated%3E=2018-11-12&DateUpdated%3C=2018-11-11&DateCreated=2008-01-03&FriendlyName=friendly_name&DateUpdated=2018-11-13&DateCreated%3C=2008-01-01&DateCreated%3E=2008-01-02&PageSize=50&Page=0",
                "next_page_uri": null,
                "previous_page_uri": null,
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences.json?Status=init&DateUpdated%3E=2018-11-12&DateUpdated%3C=2018-11-11&DateCreated=2008-01-03&FriendlyName=friendly_name&DateUpdated=2018-11-13&DateCreated%3C=2008-01-01&DateCreated%3E=2008-01-02&PageSize=50&Page=0",
                "page": 0,
                "page_size": 50,
                "start": 0,
                "end": 0
            }
            '''
        ))

        actual = self.client.api.v2010.accounts(sid="ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .conferences.list()

        self.assertIsNotNone(actual)

    def test_read_full_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "conferences": [
                    {
                        "status": "in-progress",
                        "region": "jp1",
                        "sid": "CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "date_updated": "Sat, 03 Jan 2015 11:23:45 +0000",
                        "date_created": "Sat, 03 Jan 2015 11:23:45 +0000",
                        "subresource_uris": {
                            "participants": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants.json",
                            "recordings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings.json"
                        },
                        "friendly_name": "friendly_name",
                        "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
                        "api_version": "2010-04-01",
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                    },
                    {
                        "status": "in-progress",
                        "region": "unknown",
                        "sid": "CFbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",
                        "date_updated": "Fri, 02 Jan 2015 11:23:45 +0000",
                        "date_created": "Fri, 02 Jan 2015 11:23:45 +0000",
                        "subresource_uris": {
                            "participants": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb/Participants.json",
                            "recordings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb/Recordings.json"
                        },
                        "friendly_name": "friendly_name",
                        "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.json",
                        "api_version": "2010-04-01",
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                    },
                    {
                        "status": "in-progress",
                        "region": "us1",
                        "sid": "CFcccccccccccccccccccccccccccccccc",
                        "date_updated": "Thu, 01 Jan 2015 11:23:45 +0000",
                        "date_created": "Thu, 01 Jan 2015 11:23:45 +0000",
                        "subresource_uris": {
                            "participants": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFcccccccccccccccccccccccccccccccc/Participants.json",
                            "recordings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFcccccccccccccccccccccccccccccccc/Recordings.json"
                        },
                        "friendly_name": "friendly_name",
                        "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFcccccccccccccccccccccccccccccccc.json",
                        "api_version": "2010-04-01",
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                    }
                ],
                "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences.json?Status=in-progress&DateUpdated%3E=2018-11-12&DateUpdated%3C=2018-11-11&DateCreated=2008-01-03&FriendlyName=friendly_name&DateUpdated=2018-11-13&DateCreated%3C=2008-01-01&DateCreated%3E=2008-01-02&PageSize=3&Page=0",
                "next_page_uri": null,
                "previous_page_uri": null,
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences.json?Status=in-progress&DateUpdated%3E=2018-11-12&DateUpdated%3C=2018-11-11&DateCreated=2008-01-03&FriendlyName=friendly_name&DateUpdated=2018-11-13&DateCreated%3C=2008-01-01&DateCreated%3E=2008-01-02&PageSize=3&Page=0",
                "page": 0,
                "page_size": 3,
                "start": 0,
                "end": 2
            }
            '''
        ))

        actual = self.client.api.v2010.accounts(sid="ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .conferences.list()

        self.assertIsNotNone(actual)

    def test_read_next_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "conferences": [
                    {
                        "status": "in-progress",
                        "region": "jp1",
                        "sid": "CFdddddddddddddddddddddddddddddddd",
                        "date_updated": "Thu, 01 Jan 2015 10:23:45 +0000",
                        "date_created": "Thu, 01 Jan 2015 10:23:45 +0000",
                        "subresource_uris": {
                            "participants": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFdddddddddddddddddddddddddddddddd/Participants.json",
                            "recordings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFdddddddddddddddddddddddddddddddd/Recordings.json"
                        },
                        "friendly_name": "friendly_name",
                        "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFdddddddddddddddddddddddddddddddd.json",
                        "api_version": "2010-04-01",
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                    },
                    {
                        "status": "in-progress",
                        "region": "unknown",
                        "sid": "CFeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee",
                        "date_updated": "Thu, 01 Jan 2015 09:23:45 +0000",
                        "date_created": "Thu, 01 Jan 2015 09:23:45 +0000",
                        "subresource_uris": {
                            "participants": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee/Participants.json",
                            "recordings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee/Recordings.json"
                        },
                        "friendly_name": "friendly_name",
                        "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee.json",
                        "api_version": "2010-04-01",
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                    },
                    {
                        "status": "in-progress",
                        "region": "us1",
                        "sid": "CFffffffffffffffffffffffffffffffff",
                        "date_updated": "Thu, 01 Jan 2015 08:23:45 +0000",
                        "date_created": "Thu, 01 Jan 2015 08:23:45 +0000",
                        "subresource_uris": {
                            "participants": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFffffffffffffffffffffffffffffffff/Participants.json",
                            "recordings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFffffffffffffffffffffffffffffffff/Recordings.json"
                        },
                        "friendly_name": "friendly_name",
                        "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFffffffffffffffffffffffffffffffff.json",
                        "api_version": "2010-04-01",
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                    }
                ],
                "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences.json?Status=in-progress&DateUpdated%3E=2018-11-12&DateUpdated%3C=2018-11-11&DateCreated=2008-01-03&FriendlyName=friendly_name&DateUpdated=2018-11-13&DateCreated%3C=2008-01-01&DateCreated%3E=2008-01-02&PageSize=3&Page=0",
                "next_page_uri": null,
                "previous_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences.json?Status=in-progress&DateUpdated%3E=2018-11-12&DateUpdated%3C=2018-11-11&DateCreated=2008-01-03&FriendlyName=friendly_name&DateUpdated=2018-11-13&DateCreated%3C=2008-01-01&DateCreated%3E=2008-01-02&PageSize=3&Page=0&PageToken=PBCFdddddddddddddddddddddddddddddddd",
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences.json?Status=in-progress&DateUpdated%3E=2018-11-12&DateUpdated%3C=2018-11-11&DateCreated=2008-01-03&FriendlyName=friendly_name&DateUpdated=2018-11-13&DateCreated%3C=2008-01-01&DateCreated%3E=2008-01-02&PageSize=3&Page=1&PageToken=PACFcccccccccccccccccccccccccccccccc",
                "page": 1,
                "page_size": 3,
                "start": 3,
                "end": 5
            }
            '''
        ))

        actual = self.client.api.v2010.accounts(sid="ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .conferences.list()

        self.assertIsNotNone(actual)

    def test_read_previous_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "conferences": [
                    {
                        "status": "in-progress",
                        "region": "jp1",
                        "sid": "CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "date_updated": "Sat, 03 Jan 2015 11:23:45 +0000",
                        "date_created": "Sat, 03 Jan 2015 11:23:45 +0000",
                        "subresource_uris": {
                            "participants": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants.json",
                            "recordings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings.json"
                        },
                        "friendly_name": "friendly_name",
                        "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
                        "api_version": "2010-04-01",
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                    },
                    {
                        "status": "in-progress",
                        "region": "unknown",
                        "sid": "CFbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",
                        "date_updated": "Fri, 02 Jan 2015 11:23:45 +0000",
                        "date_created": "Fri, 02 Jan 2015 11:23:45 +0000",
                        "subresource_uris": {
                            "participants": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb/Participants.json",
                            "recordings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb/Recordings.json"
                        },
                        "friendly_name": "friendly_name",
                        "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.json",
                        "api_version": "2010-04-01",
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                    },
                    {
                        "status": "in-progress",
                        "region": "us1",
                        "sid": "CFcccccccccccccccccccccccccccccccc",
                        "date_updated": "Thu, 01 Jan 2015 11:23:45 +0000",
                        "date_created": "Thu, 01 Jan 2015 11:23:45 +0000",
                        "subresource_uris": {
                            "participants": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFcccccccccccccccccccccccccccccccc/Participants.json",
                            "recordings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFcccccccccccccccccccccccccccccccc/Recordings.json"
                        },
                        "friendly_name": "friendly_name",
                        "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFcccccccccccccccccccccccccccccccc.json",
                        "api_version": "2010-04-01",
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                    }
                ],
                "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences.json?Status=in-progress&DateUpdated%3E=2018-11-12&DateUpdated%3C=2018-11-11&DateCreated=2008-01-03&FriendlyName=friendly_name&DateUpdated=2018-11-13&DateCreated%3C=2008-01-01&DateCreated%3E=2008-01-02&PageSize=3&Page=0",
                "next_page_uri": null,
                "previous_page_uri": null,
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences.json?Status=in-progress&DateUpdated%3E=2018-11-12&DateUpdated%3C=2018-11-11&DateCreated=2008-01-03&FriendlyName=friendly_name&DateUpdated=2018-11-13&DateCreated%3C=2008-01-01&DateCreated%3E=2008-01-02&PageSize=3&Page=0&PageToken=PBCFdddddddddddddddddddddddddddddddd",
                "page": 0,
                "page_size": 3,
                "start": 0,
                "end": 2
            }
            '''
        ))

        actual = self.client.api.v2010.accounts(sid="ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .conferences.list()

        self.assertIsNotNone(actual)

    def test_update_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.api.v2010.accounts(sid="ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .conferences(sid="CFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update()

        self.holodeck.assert_has_request(Request(
            'post',
            'https://api.twilio.com/2010-04-01/Accounts/ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Conferences/CFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.json',
        ))

    def test_update_end_conference_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "api_version": "2010-04-01",
                "date_created": "Mon, 22 Aug 2011 20:58:45 +0000",
                "date_updated": "Mon, 22 Aug 2011 20:58:46 +0000",
                "friendly_name": null,
                "region": "us1",
                "sid": "CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "status": "completed",
                "subresource_uris": {
                    "participants": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants.json",
                    "recordings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings.json"
                },
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
            }
            '''
        ))

        actual = self.client.api.v2010.accounts(sid="ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .conferences(sid="CFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update()

        self.assertIsNotNone(actual)
