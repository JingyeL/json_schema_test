# demo for generating schema from json data

import unittest
import json
import datetime
import jsonschema

        
class TestPageViews(unittest.TestCase):

        
    def get_expected_schema(self, name):
        """
        get expected schema from s3 file
        """
        return json.load(open(name, 'r'))
        

    def test_jsonschema_payload_ok(self):
        """
        demo payload ok
        note: datetime field is not validated
        """
        test_data  = {
            "event_type": "pageview",
            "event_id": "12345",
            "user_id": 123,
            "user_ip": "101.188.68.135",
            "user_agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)",
            "referrer": "http://www.google.com",
            "url": "http://www.google.com",
            "price": 123.45,
            "page_title": "Google",
            "page_view_time": "2023-09-24 09:00:00",
            "custom_data": {
                "user_type": "paid",
                "user_group": "beta",
                "user_age": 23,
                "user_payload":{
                    "user_name": "john",
                    "user_email": "john@email.com"
                }
            }
        }
        jsonschema.validate(test_data, schema=self.get_expected_schema("page_view_schema.json"))

    
    def test_payload_missing_price(self):
        test_data  = {
            "event_type": "pageview",
            "event_id": "12345",
            "user_id": 123,
            "user_ip": "101.188.68.135",
            "user_agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)",
            "referrer": "http://www.google.com",
            "url": "http://www.google.com",
            "page_title": "Google",
            "page_view_time": "2023-09-24 09:00:00",
            "custom_data": {
                "user_type": "paid",
                "user_group": "beta",
                "user_age": 23,
                "user_payload":{
                    "user_name": "john",
                    "user_email": "john@email.com"
                }
            }
        }
        jsonschema.validate(test_data, schema=self.get_expected_schema("page_view_schema.json"))

    def test_payload_missing_user_id(self):
        test_data  = {
            "event_type": "pageview",
            "event_id": "12345",
            "user_ip": "101.188.68.135",
            "user_agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)",
            "referrer": "http://www.google.com",
            "url": "http://www.google.com",
            "price": 123.45,
            "page_title": "Google",
            "page_view_time": "2023-09-24 09:00:00",
            "custom_data": {
                "user_type": "paid",
                "user_group": "beta",
                "user_age": 23,
                "user_payload":{
                    "user_name": "john",
                    "user_email": "john@email.com"
                }
            }
        }

        # jsonschema.validate(test_data, schema=self.get_expected_schema("page_view_schema.json"))
        self.assertRaises(jsonschema.exceptions.ValidationError, 
                          lambda: jsonschema.validate(test_data, 
                                                      schema=self.get_expected_schema("page_view_schema.json")))
        
    def test_payload_extra_field(self):
        """
        demo extra field will not cause validation error
        """
        test_data  = {
            "event_type": "pageview",
            "event_id": "12345",
            "user_id": 123,
            "user_ip": "101.188.68.135",
            "user_agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)",
            "referrer": "http://www.google.com",
            "url": "http://www.google.com",
            "price": 123.45,
            "page_title": "Google",
            "page_view_time": "2023-09-24 09:00:00",
            "foo": "bar",
            "custom_data": {
                "user_type": "paid",
                "user_group": "beta",
                "user_age": 23,
                "user_payload":{
                    "user_name": "john",
                    "user_email": "john@email.com"
                }
            }
        }
        self.assertRaises(jsonschema.exceptions.ValidationError,
                          lambda:jsonschema.validate(test_data, schema=self.get_expected_schema("page_view_schema.json")))

    
if __name__ == '__main__':
    unittest.main()
