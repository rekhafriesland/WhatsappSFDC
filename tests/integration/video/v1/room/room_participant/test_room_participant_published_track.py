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


class PublishedTrackTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.video.v1.rooms(sid="RMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                .participants(sid="PAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                .published_tracks(sid="MTXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://video.twilio.com/v1/Rooms/RMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Participants/PAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/PublishedTracks/MTXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "room_sid": "RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "participant_sid": "PAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "sid": "MTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "name": "bob-track",
                "kind": "data",
                "enabled": true,
                "url": "https://video.twilio.com/v1/Rooms/RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants/PAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/PublishedTracks/MTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.video.v1.rooms(sid="RMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                     .participants(sid="PAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                     .published_tracks(sid="MTXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.assertIsNotNone(actual)

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.video.v1.rooms(sid="RMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                .participants(sid="PAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                .published_tracks.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://video.twilio.com/v1/Rooms/RMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Participants/PAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/PublishedTracks',
        ))

    def test_read_empty_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "published_tracks": [],
                "meta": {
                    "page": 0,
                    "page_size": 50,
                    "first_page_url": "https://video.twilio.com/v1/Rooms/RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants/PAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/PublishedTracks?PageSize=50&Page=0",
                    "previous_page_url": null,
                    "url": "https://video.twilio.com/v1/Rooms/RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants/PAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/PublishedTracks?PageSize=50&Page=0",
                    "next_page_url": null,
                    "key": "published_tracks"
                }
            }
            '''
        ))

        actual = self.client.video.v1.rooms(sid="RMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                     .participants(sid="PAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                     .published_tracks.list()

        self.assertIsNotNone(actual)
