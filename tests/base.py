import unittest
import os
import tap_tester.connections as connections
import tap_tester.menagerie as menagerie
import tap_tester.runner as runner
from datetime import datetime as dt
from datetime import timedelta
import dateutil.parser
import pytz

class ActiveCampaignTest(unittest.TestCase):
    start_date = ""
    
    START_DATE_FORMAT = "%Y-%m-%dT00:00:00Z"
    PRIMARY_KEYS = "table-key-properties"
    REPLICATION_METHOD = "forced-replication-method"
    REPLICATION_KEYS = "valid-replication-keys"
    FULL_TABLE = "FULL_TABLE"
    INCREMENTAL = "INCREMENTAL"
    OBEYS_START_DATE = "obey-start-date"

    def tap_name(self):
        """The name of the tap"""
        return "tap-activecampaign"
    
    def setUp(self):
        required_env = {
            "TAP_ACTIVECAMPAIGN_API_TOKEN",
            "TAP_ACTIVECAMPAIGN_API_URL",
        }
        missing_envs = [v for v in required_env if not os.getenv(v)]
        if missing_envs:
            raise Exception("set " + ", ".join(missing_envs))
        
    def get_type(self):
        return "platform.activecampaign"

    def get_credentials(self):
        """Authentication information for the test account"""
        return {
            'api_url': os.getenv('TAP_ACTIVECAMPAIGN_API_URL'),
            'api_token': os.getenv('TAP_ACTIVECAMPAIGN_API_TOKEN')
        }

    def get_properties(self, original: bool = True):
        """Configuration properties required for the tap."""
        return_value = {
            "start_date" : "2021-12-01T00:00:00Z",
        }
        if original:
            return return_value

        # Reassign start date
        return_value["start_date"] = self.start_date
        return return_value
    
    def expected_metadata(self):
        """The expected streams and metadata about the streams"""
        return {
            'accounts': {
                self.PRIMARY_KEYS: {'id'},
                self.REPLICATION_METHOD: self.INCREMENTAL,
                self.REPLICATION_KEYS: {'updated_timestamp'},
                self.OBEYS_START_DATE: True
            },
            'account_contacts': {
                self.PRIMARY_KEYS: {'id'},
                self.REPLICATION_METHOD: self.INCREMENTAL,
                self.REPLICATION_KEYS: {'updated_timestamp'},
                self.OBEYS_START_DATE: True      
            },
            'account_custom_fields': {
                self.PRIMARY_KEYS: {'id'},
                self.REPLICATION_METHOD: self.INCREMENTAL,
                self.REPLICATION_KEYS: {'updated_timestamp'},
                self.OBEYS_START_DATE: True
            },
            'account_custom_field_values': {
                self.PRIMARY_KEYS: {'id'},
                self.REPLICATION_METHOD: self.INCREMENTAL,
                self.REPLICATION_KEYS: {'updated_timestamp'},
                self.OBEYS_START_DATE: True
            },
            'addresses': {
                self.PRIMARY_KEYS: {'id'},
                self.REPLICATION_METHOD: self.FULL_TABLE,
                self.OBEYS_START_DATE: False
            },
            'automations': {
                self.PRIMARY_KEYS: {'id'},
                self.REPLICATION_METHOD: self.INCREMENTAL,
                self.REPLICATION_KEYS: {'mdate'},
                self.OBEYS_START_DATE: True
            },
            'brandings': {
                self.PRIMARY_KEYS: {'id'},
                self.REPLICATION_METHOD: self.FULL_TABLE,
                self.OBEYS_START_DATE: False
            },
            'calendars': {
                self.PRIMARY_KEYS: {'id'},
                self.REPLICATION_METHOD: self.INCREMENTAL,
                self.REPLICATION_KEYS: {'mdate'},
                self.OBEYS_START_DATE: True
            },
            'campaigns': {
                self.PRIMARY_KEYS: {'id'},
                self.REPLICATION_METHOD: self.INCREMENTAL,
                self.REPLICATION_KEYS: {'updated_timestamp'},
                self.OBEYS_START_DATE: True
            },
            'campaign_links': {
                self.PRIMARY_KEYS: {'id'},
                self.REPLICATION_METHOD: self.INCREMENTAL,
                self.REPLICATION_KEYS: {'updated_timestamp'},
                self.OBEYS_START_DATE: True
            },
            'contacts': {
                self.PRIMARY_KEYS: {'id'},
                self.REPLICATION_METHOD: self.INCREMENTAL,
                self.REPLICATION_KEYS: {'updated_timestamp'},
                self.OBEYS_START_DATE: True
            },
            'contact_automations': {
                self.PRIMARY_KEYS: {'id'},
                self.REPLICATION_METHOD: self.INCREMENTAL,
                self.REPLICATION_KEYS: {'lastdate'},
                self.OBEYS_START_DATE: True
            },
            'contact_custom_fields': {
                self.PRIMARY_KEYS: {'id'},
                self.REPLICATION_METHOD: self.FULL_TABLE,
                self.OBEYS_START_DATE: False
            },
            'contact_custom_field_options': {
                self.PRIMARY_KEYS: {'id'},
                self.REPLICATION_METHOD: self.FULL_TABLE,
                self.OBEYS_START_DATE: False
            },
            'contact_custom_field_rels': {
                self.PRIMARY_KEYS: {'id'},
                self.REPLICATION_METHOD: self.FULL_TABLE,
                self.OBEYS_START_DATE: False
            },
            'contact_custom_field_values': {
                self.PRIMARY_KEYS: {'id'},
                self.REPLICATION_METHOD: self.INCREMENTAL,
                self.REPLICATION_KEYS: {'udate'},
                self.OBEYS_START_DATE: True
            },
            'contact_deals': {
                self.PRIMARY_KEYS: {'id'},
                self.REPLICATION_METHOD: self.INCREMENTAL,
                self.REPLICATION_KEYS: {'updated_timestamp'},
                self.OBEYS_START_DATE: True
            },
            'deal_stages': {
                self.PRIMARY_KEYS: {'id'},
                self.REPLICATION_METHOD: self.INCREMENTAL,
                self.REPLICATION_KEYS: {'udate'},
                self.OBEYS_START_DATE: True
            },
            'deal_groups': {
                self.PRIMARY_KEYS: {'id'},
                self.REPLICATION_METHOD: self.INCREMENTAL,
                self.REPLICATION_KEYS: {'udate'},
                self.OBEYS_START_DATE: True
            },
            'deal_custom_fields': {
                self.PRIMARY_KEYS: {'id'},
                self.REPLICATION_METHOD: self.INCREMENTAL,
                self.REPLICATION_KEYS: {'updated_timestamp'},
                self.OBEYS_START_DATE: True
            },
            'deal_custom_field_values': {
                self.PRIMARY_KEYS: {'id'},
                self.REPLICATION_METHOD: self.INCREMENTAL,
                self.REPLICATION_KEYS: {'updated_timestamp'},
                self.OBEYS_START_DATE: True
            },
            'deals': {
                self.PRIMARY_KEYS: {'id'},
                self.REPLICATION_METHOD: self.INCREMENTAL,
                self.REPLICATION_KEYS: {'mdate'},
                self.OBEYS_START_DATE: True
            },
            'ecommerce_connections': {
                self.PRIMARY_KEYS: {'id'},
                self.REPLICATION_METHOD: self.INCREMENTAL,
                self.REPLICATION_KEYS: {'udate'},
                self.OBEYS_START_DATE: True
            },
            'ecommerce_customers': {
                self.PRIMARY_KEYS: {'id'},
                self.REPLICATION_METHOD: self.INCREMENTAL,
                self.REPLICATION_KEYS: {'tstamp'},
                self.OBEYS_START_DATE: True
            },
            'ecommerce_orders': {
                self.PRIMARY_KEYS: {'id'},
                self.REPLICATION_METHOD: self.INCREMENTAL,
                self.REPLICATION_KEYS: {'updated_date'},
                self.OBEYS_START_DATE: True
            },
            'ecommerce_order_products': {
                self.PRIMARY_KEYS: {'id'},
                self.REPLICATION_METHOD: self.FULL_TABLE,
                self.OBEYS_START_DATE: False
            },
            'forms': {
                self.PRIMARY_KEYS: {'id'},
                self.REPLICATION_METHOD: self.INCREMENTAL,
                self.REPLICATION_KEYS: {'udate'},
                self.OBEYS_START_DATE: True
            },
            'groups': {
                self.PRIMARY_KEYS: {'id'},
                self.REPLICATION_METHOD: self.FULL_TABLE,
                self.OBEYS_START_DATE: False
            },
            'lists': {
                self.PRIMARY_KEYS: {'id'},
                self.REPLICATION_METHOD: self.INCREMENTAL,
                self.REPLICATION_KEYS: {'updated_timestamp'},
                self.OBEYS_START_DATE: True
            },
            'messages': {
                self.PRIMARY_KEYS: {'id'},
                self.REPLICATION_METHOD: self.INCREMENTAL,
                self.REPLICATION_KEYS: {'mdate'},
                self.OBEYS_START_DATE: True
            },
            'saved_responses': {
                self.PRIMARY_KEYS: {'id'},
                self.REPLICATION_METHOD: self.INCREMENTAL,
                self.REPLICATION_KEYS: {'mdate'},
                self.OBEYS_START_DATE: True
            },
            'scores': {
                self.PRIMARY_KEYS: {'id'},
                self.REPLICATION_METHOD: self.INCREMENTAL,
                self.REPLICATION_KEYS: {'mdate'},
                self.OBEYS_START_DATE: True
            },
            'segments': {
                self.PRIMARY_KEYS: {'id'},
                self.REPLICATION_METHOD: self.FULL_TABLE,
                self.OBEYS_START_DATE: False
            },
            'tags': {
                self.PRIMARY_KEYS: {'id'},
                self.REPLICATION_METHOD: self.FULL_TABLE,
                self.OBEYS_START_DATE: False
            },
            'task_types': {
                self.PRIMARY_KEYS: {'id'},
                self.REPLICATION_METHOD: self.FULL_TABLE,
                self.OBEYS_START_DATE: False
            },
            'tasks': {
                self.PRIMARY_KEYS: {'id'},
                self.REPLICATION_METHOD: self.INCREMENTAL,
                self.REPLICATION_KEYS: {'udate'},
                self.OBEYS_START_DATE: True
            },
            'templates': {
                self.PRIMARY_KEYS: {'id'},
                self.REPLICATION_METHOD: self.INCREMENTAL,
                self.REPLICATION_KEYS: {'mdate'},
                self.OBEYS_START_DATE: True
            },
            'users': {
                self.PRIMARY_KEYS: {'id'},
                self.REPLICATION_METHOD: self.FULL_TABLE,
                self.OBEYS_START_DATE: False
            },
            'webhooks': {
                self.PRIMARY_KEYS: {'id'},
                self.REPLICATION_METHOD: self.FULL_TABLE,
                self.OBEYS_START_DATE: False
            },
            'activities': {
                self.PRIMARY_KEYS: {'id'},
                self.REPLICATION_METHOD: self.INCREMENTAL,
                self.REPLICATION_KEYS: {'tstamp'},
                self.OBEYS_START_DATE: True
            },
            'automation_blocks': {
                self.PRIMARY_KEYS: {'id'},
                self.REPLICATION_METHOD: self.INCREMENTAL,
                self.REPLICATION_KEYS: {'mdate'},
                self.OBEYS_START_DATE: True
            },
            'bounce_logs': {
                self.PRIMARY_KEYS: {'id'},
                self.REPLICATION_METHOD: self.INCREMENTAL,
                self.REPLICATION_KEYS: {'updated_timestamp'},
                self.OBEYS_START_DATE: True
            },
            'campaign_lists': {
                self.PRIMARY_KEYS: {'id'},
                self.REPLICATION_METHOD: self.FULL_TABLE,
                self.OBEYS_START_DATE: False
            },
            'campaign_messages': {
                self.PRIMARY_KEYS: {'id'},
                self.REPLICATION_METHOD: self.FULL_TABLE,
                self.OBEYS_START_DATE: False
            },
            'configs': {
                self.PRIMARY_KEYS: {'id'},
                self.REPLICATION_METHOD: self.INCREMENTAL,
                self.REPLICATION_KEYS: {'updated_timestamp'},
                self.OBEYS_START_DATE: True
            },
            'contact_data': {
                self.PRIMARY_KEYS: {'id'},
                self.REPLICATION_METHOD: self.INCREMENTAL,
                self.REPLICATION_KEYS: {'tstamp'},
                self.OBEYS_START_DATE: True
            },
            'contact_emails': {
                self.PRIMARY_KEYS: {'id'},
                self.REPLICATION_METHOD: self.INCREMENTAL,
                self.REPLICATION_KEYS: {'sdate'},
                self.OBEYS_START_DATE: True
            },
            'contact_lists': {
                self.PRIMARY_KEYS: {'id'},
                self.REPLICATION_METHOD: self.INCREMENTAL,
                self.REPLICATION_KEYS: {'updated_timestamp'},
                self.OBEYS_START_DATE: True
            },
            'contact_tags': {
                self.PRIMARY_KEYS: {'id'},
                self.REPLICATION_METHOD: self.INCREMENTAL,
                self.REPLICATION_KEYS: {'updated_timestamp'},
                self.OBEYS_START_DATE: True
            },
            'contact_conversions': {
                self.PRIMARY_KEYS: {'id'},
                self.REPLICATION_METHOD: self.INCREMENTAL,
                self.REPLICATION_KEYS: {'cdate'},
                self.OBEYS_START_DATE: True
            },
            'conversions': {
                self.PRIMARY_KEYS: {'id'},
                self.REPLICATION_METHOD: self.INCREMENTAL,
                self.REPLICATION_KEYS: {'udate'},
                self.OBEYS_START_DATE: True
            },
            'conversion_triggers': {
                self.PRIMARY_KEYS: {'id'},
                self.REPLICATION_METHOD: self.INCREMENTAL,
                self.REPLICATION_KEYS: {'udate'},
                self.OBEYS_START_DATE: True
            },
            'deal_activities': {
                self.PRIMARY_KEYS: {'id'},
                self.REPLICATION_METHOD: self.INCREMENTAL,
                self.REPLICATION_KEYS: {'cdate'},
                self.OBEYS_START_DATE: True
            },
            'deal_group_users': {
                self.PRIMARY_KEYS: {'id'},
                self.REPLICATION_METHOD: self.FULL_TABLE,
                self.OBEYS_START_DATE: False
            },
            'ecommerce_order_activities': {
                self.PRIMARY_KEYS: {'id'},
                self.REPLICATION_METHOD: self.INCREMENTAL,
                self.REPLICATION_KEYS: {'updated_date'},
                self.OBEYS_START_DATE: True
            },
            'email_activities': {
                self.PRIMARY_KEYS: {'id'},
                self.REPLICATION_METHOD: self.INCREMENTAL,
                self.REPLICATION_KEYS: {'tstamp'},
                self.OBEYS_START_DATE: True
            },
            'goals': {
                self.PRIMARY_KEYS: {'id'},
                self.REPLICATION_METHOD: self.FULL_TABLE,
                self.OBEYS_START_DATE: False
            },
            'site_messages': {
                self.PRIMARY_KEYS: {'id'},
                self.REPLICATION_METHOD: self.INCREMENTAL,
                self.REPLICATION_KEYS: {'ldate'},
                self.OBEYS_START_DATE: True
            },
            'sms': {
                self.PRIMARY_KEYS: {'id'},
                self.REPLICATION_METHOD: self.INCREMENTAL,
                self.REPLICATION_KEYS: {'tstamp'},
                self.OBEYS_START_DATE: True
            }
        }


    def expected_check_streams(self):
        """A set of expected stream names"""
        return set(self.expected_metadata().keys())

    def expected_replication_keys(self):
        """return a dictionary with key of table name and value as a set of replication key fields"""

        return {table: properties.get(self.REPLICATION_KEYS, set()) for table, properties
                in self.expected_metadata().items()}

    def expected_primary_keys(self):
        """return a dictionary with key of table name and value as a set of primary key fields"""
        return {table: properties.get(self.PRIMARY_KEYS, set()) for table, properties
                in self.expected_metadata().items()}

    def expected_replication_method(self):
        """return a dictionary with key of table name nd value of replication method"""
        return {table: properties.get(self.REPLICATION_METHOD, set()) for table, properties
                in self.expected_metadata().items()}
        
    def expected_automatic_fields(self):
        """return a dictionary with key of table name and set of value of automatic(primary key and bookmark field) fields"""
        auto_fields = {}
        for k, v in self.expected_metadata().items():
            auto_fields[k] = v.get(self.PRIMARY_KEYS, set()) |  v.get(self.REPLICATION_KEYS, set())
        return auto_fields

    def run_and_verify_check_mode(self, conn_id):
        """
        Run the tap in check mode and verify it succeeds.
        This should be ran prior to field selection and initial sync.
        Return the connection id and found catalogs from menagerie.
        """
        # run in check mode
        check_job_name = runner.run_check_mode(self, conn_id)

        # verify check exit codes
        exit_status = menagerie.get_exit_status(conn_id, check_job_name)
        menagerie.verify_check_exit_status(self, exit_status, check_job_name)

        found_catalogs = menagerie.get_catalogs(conn_id)
        self.assertGreater(len(found_catalogs), 0, msg="unable to locate schemas for connection {}".format(conn_id))

        found_catalog_names = set(map(lambda c: c['stream_name'], found_catalogs))
        self.assertSetEqual(self.expected_check_streams(), found_catalog_names, msg="discovered schemas do not match")
        print("discovered schemas are OK")

        return found_catalogs

    def run_and_verify_sync(self, conn_id):
        """
        Run a sync job and make sure it exited properly.
        Return a dictionary with keys of streams synced
        and values of records synced for each stream
        """

        # Run a sync job using orchestrator
        sync_job_name = runner.run_sync_mode(self, conn_id)

        # verify tap and target exit codes
        exit_status = menagerie.get_exit_status(conn_id, sync_job_name)
        menagerie.verify_sync_exit_status(self, exit_status, sync_job_name)

        sync_record_count = runner.examine_target_output_file(self,
                                                              conn_id,
                                                              self.expected_check_streams(),
                                                              self.expected_primary_keys())

        self.assertGreater(
            sum(sync_record_count.values()), 0,
            msg="failed to replicate any data: {}".format(sync_record_count)
        )
        print("total replicated row count: {}".format(sum(sync_record_count.values())))

        return sync_record_count

    def perform_and_verify_table_and_field_selection(self,
                                                     conn_id,
                                                     test_catalogs,
                                                     select_all_fields=True):
        """
        Perform table and field selection based off of the streams to select
        set and field selection parameters.
        Verify this results in the expected streams selected and all or no
        fields selected for those streams.
        """

        # Select all available fields or select no fields from all testable streams
        self.select_all_streams_and_fields(
            conn_id=conn_id, catalogs=test_catalogs, select_all_fields=select_all_fields
        )

        catalogs = menagerie.get_catalogs(conn_id)

        # Ensure our selection affects the catalog
        expected_selected = [tc.get('stream_name') for tc in test_catalogs]
        for cat in catalogs:
            catalog_entry = menagerie.get_annotated_schema(conn_id, cat['stream_id'])

            # Verify all testable streams are selected
            selected = catalog_entry.get('annotated-schema').get('selected')
            print("Validating selection on {}: {}".format(cat['stream_name'], selected))
            if cat['stream_name'] not in expected_selected:
                self.assertFalse(selected, msg="Stream selected, but not testable.")
                continue # Skip remaining assertions if we aren't selecting this stream
            self.assertTrue(selected, msg="Stream not selected.")

            if select_all_fields:
                # Verify all fields within each selected stream are selected
                for field, field_props in catalog_entry.get('annotated-schema').get('properties').items():
                    field_selected = field_props.get('selected')
                    print("\tValidating selection on {}.{}: {}".format(
                        cat['stream_name'], field, field_selected))
                    self.assertTrue(field_selected, msg="Field not selected.")
            else:
                # Verify only automatic fields are selected
                expected_automatic_fields = self.expected_automatic_fields().get(cat['stream_name'])
                selected_fields = self.get_selected_fields_from_metadata(catalog_entry['metadata'])
                self.assertEqual(expected_automatic_fields, selected_fields)

    @staticmethod
    def get_selected_fields_from_metadata(metadata):
        selected_fields = set()
        for field in metadata:
            is_field_metadata = len(field['breadcrumb']) > 1
            inclusion_automatic_or_selected = (
                field['metadata']['selected'] is True or \
                field['metadata']['inclusion'] == 'automatic'
            )
            if is_field_metadata and inclusion_automatic_or_selected:
                selected_fields.add(field['breadcrumb'][1])
        return selected_fields


    @staticmethod
    def select_all_streams_and_fields(conn_id, catalogs, select_all_fields: bool = True):
        """Select all streams and all fields within streams"""
        for catalog in catalogs:
            schema = menagerie.get_annotated_schema(conn_id, catalog['stream_id'])

            non_selected_properties = []
            if not select_all_fields:
                # get a list of all properties so that none are selected
                non_selected_properties = schema.get('annotated-schema', {}).get(
                    'properties', {}).keys()

            connections.select_catalog_and_fields_via_metadata(
                conn_id, catalog, schema, [], non_selected_properties)

    def calculated_states_by_stream(self, current_state):
        timedelta_by_stream = {stream: [0,0,1]  # {stream_name: [days, hours, minutes], ...}
                               for stream in self.expected_check_streams()}

        stream_to_calculated_state = {stream: "" for stream in current_state['bookmarks'].keys()}
        for stream, state in current_state['bookmarks'].items():
            state_as_datetime = dateutil.parser.parse(state)

            days, hours, minutes = timedelta_by_stream[stream]
            calculated_state_as_datetime = state_as_datetime - timedelta(days=days, hours=hours, minutes=minutes)

            calculated_state_formatted = dt.strftime(calculated_state_as_datetime, self.START_DATE_FORMAT)

            stream_to_calculated_state[stream] = calculated_state_formatted

        return stream_to_calculated_state

    def convert_state_to_utc(self, date_str):
        """
        Convert a saved bookmark value of the form '2020-08-25T13:17:36-07:00' to
        a string formatted utc datetime,
        in order to compare aginast json formatted datetime values
        """
        date_object = dateutil.parser.parse(date_str)
        date_object_utc = date_object.astimezone(tz=pytz.UTC)
        return dt.strftime(date_object_utc, "%Y-%m-%dT%H:%M:%SZ")
    
    def timedelta_formatted(self, dtime, days=0):
        try:
            date_stripped = dt.strptime(dtime, self.START_DATE_FORMAT)
            return_date = date_stripped + timedelta(days=days)

            return dt.strftime(return_date, self.START_DATE_FORMAT)

        except ValueError:
                return Exception("Datetime object is not of the format: {}".format(self.START_DATE_FORMAT))

    def parse_date(self, date_value):
        """
        Pass in string-formatted-datetime, parse the value, and return it as an unformatted datetime object.
        """
        date_formats = {
            "%Y-%m-%dT%H:%M:%S.%fZ",
            "%Y-%m-%dT%H:%M:%SZ",
            "%Y-%m-%dT%H:%M:%S.%f+00:00",
            "%Y-%m-%dT%H:%M:%S+00:00",
            "%Y-%m-%d"
        }
        for date_format in date_formats:
            try:
                date_stripped = dt.strptime(date_value, date_format)
                return date_stripped
            except ValueError:
                continue

        raise NotImplementedError(
            "Tests do not account for dates of this format: {}".format(date_value))
