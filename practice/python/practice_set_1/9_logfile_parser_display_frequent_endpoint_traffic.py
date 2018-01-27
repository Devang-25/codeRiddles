#!/bin/env python3

# Given a log file with following format:

# 127.0.0.1 -- [1458656026] "GET /search HTTP/1.1"
# 127.0.0.1 -- [1458656026] "GET /landing HTTP/1.1"
# 127.0.0.1 -- [1458656026] "GET /landing HTTP/1.1"
# 127.0.0.1 -user2 [1458656027] "GET /chatty HTTP/1.1"
# 127.0.0.1 -- [1458656027] "GET /search?params=foo HTTP/1.1"
# 127.0.0.1 -user2 [1458656027] "GET /search? HTTP/1.1"
# 127.0.0.1 -user7 [1458656027] "GET /chatty HTTP/1.1"
# 127.0.0.1 fake_login [1458656027] "GET /less_chatty HTTP/1.1"
# 127.0.0.1 -user6 [1458656027] "GET /chatty HTTP/1.1"

# Let's assume that you have an API that returns the already parsed string into an array:

# String[] api.getLineAsArray()
# # returns an Array("127.0.0.1", "--", "[1458656026]", '"GET', '/search', 'HTTP/1.1"')

# Create a solution that will process the log and display which path (/search, /landing, etc..) has the most traffic, for each second

# For example, for '1458656027', the path '/chatty' will have 3 hits.

import unittest

from ast import literal_eval
from operator import itemgetter
from collections import OrderedDict, \
    defaultdict, \
    Counter


# looking for tsamp = 2

# ts = 1
# ts = 1
# ts = 2


class LogParserAPI(object):
    '''
    Helper class for parsing logfile.
    ..mocks the 'api' object
    '''
    def __init__(self, fpath):
        self.fpath = fpath

    def open_stream(self):
        try:
            self.stream = open(self.fpath, 'r')
        except (FileNotFoundError, IsADirectoryError):
            quit("Invalid File: %s" % self.fpath)

    def parse_line(self, line):
        return line.split()

    def getLineAsArray(self):
        line = self.stream.readline()
        if line:
            return self.parse_line(line)
        else:
            return []

    def close_stream(self):
        self.stream.close()


class TrafficAnalyzer(object):

    def __init__(self, datapath=None):
        self.api = LogParserAPI(datapath)
        self.traffic_dict = defaultdict(list)

    def form_traffic_dict(self, tstamp):
        try:
            found_from_api = False
            began_parsing_yet = False
            while True:
                line = self.api.getLineAsArray()
                if not bool(line):
                    print("..no more log lines to process")
                    break
                timestamp = int(literal_eval(line[3])[0])
                path = line[-2]
                # is_fake = line[1]
                # user = line[2]
                self.traffic_dict[timestamp].append(path)

                if timestamp == tstamp:
                    found_from_api = True
                    began_parsing_yet = True
                    continue
                elif timestamp > tstamp:
                    break
                else:
                    print("..waiting for more data")
                    began_parsing_yet = True
                    continue

            if tstamp in self.traffic_dict and not began_parsing_yet:
                # historical data found in traffic_dict
                print("..using historical data")

            if not began_parsing_yet and tstamp not in self.traffic_dict:
                # The timestamp supplied belongs to a prior day
                print("Err..couldn't find timestamp from log file api calls")
                # raise ValueError
                return False

            if began_parsing_yet and not found_from_api: #and not_found_yet:
                # timestamp lies in the future
                print("This timestamp is not yet a part of the log..")
                return False

            return True
        except:
            raise

    def get_frequent_paths(self, tstamp):
        path_counts = Counter(self.traffic_dict[tstamp])
        # print(path_counts)
        sorted_hits = sorted(path_counts.items(), key=itemgetter(1), reverse=True)
        try:
            return sorted_hits[0]
        except IndexError:
            return []

    def process_frequent(self, tstamp, paths=[]):
        print("\nGathering traffic for timestamp: ", tstamp)
        found = self.form_traffic_dict(tstamp)
        # print(self.traffic_dict)
        if found:
            paths = self.get_frequent_paths(tstamp)
            print("Popular hit: ", paths)
        return paths

class DataGatheringCases(unittest.TestCase):
    '''
    Test Cases
    '''
    analyzer = TrafficAnalyzer('data/traffic.log')

    def test_data_curated_first(self):
        print("\n ---- test_data_curated_first ---- ")
        self.analyzer.traffic_dict = defaultdict(list)
        self.analyzer.api.open_stream()
        assert self.analyzer.process_frequent(1458656028) == ('',)
        self.analyzer.api.close_stream()
        self.analyzer.api.open_stream()
        assert self.analyzer.process_frequent(1458656026) == ('/landing', 2)
        self.analyzer.api.close_stream()
        self.analyzer.api.open_stream()
        assert self.analyzer.process_frequent(1458656027) == ('/chatty', 3)
        self.analyzer.api.close_stream()

    def test_data_eventually_gathered(self):
        print("\n ---- test_data_eventually_gathered ---- ")
        self.analyzer.traffic_dict = defaultdict(list)
        self.analyzer.api.open_stream()
        assert self.analyzer.process_frequent(1458656026) == ('/landing', 2)
        self.analyzer.api.close_stream()
        self.analyzer.api.open_stream()
        assert self.analyzer.process_frequent(1458656027) == ('/chatty', 3)
        self.analyzer.api.close_stream()
        self.analyzer.api.open_stream()


    def test_data_reverse_ordered(self):
        print("\n ---- test_data_reverse_ordered ---- ")
        self.analyzer.traffic_dict = defaultdict(list)
        self.analyzer.api.open_stream()
        assert self.analyzer.process_frequent(1458656027) == ('/chatty', 3)
        self.analyzer.api.close_stream()
        self.analyzer.api.open_stream()
        assert self.analyzer.process_frequent(1458656026) == ('/landing', 2)
        self.analyzer.api.close_stream()
        self.analyzer.api.open_stream()

    def test_old_nonexistant_data(self):
        print("\n ---- test_old_nonexistant_data ---- ")
        self.analyzer.traffic_dict = defaultdict(list)
        self.analyzer.api.open_stream()
        assert self.analyzer.process_frequent(1458656025) == ('',)
        self.analyzer.api.close_stream()

    def test_future_timestamped_data(self):
        print("\n ---- test_future_timestamped_data ---- ")
        self.analyzer.traffic_dict = defaultdict(list)
        self.analyzer.api.open_stream()
        assert self.analyzer.process_frequent(1458656028) == ('',)
        self.analyzer.api.close_stream()

    def test_data_open_stream_throughout(self):
        print("\n ---- test_data_open_stream_throughout ---- ")
        self.analyzer.traffic_dict = defaultdict(list)
        self.analyzer.api.open_stream()
        assert self.analyzer.process_frequent(1458656028) == ('',)
        self.analyzer.api.close_stream()
        self.analyzer.api.open_stream()
        assert self.analyzer.process_frequent(1458656026) == ('/landing', 2)
        self.analyzer.api.close_stream()
        self.analyzer.api.open_stream()
        assert self.analyzer.process_frequent(1458656027) == ('/chatty', 3)
        self.analyzer.api.close_stream()


if __name__ == '__main__':
    # runner = unittest.TextTestRunner(failfast=True)
    # runner.run(suite())
    unittest.main()


# OUTPUT

# Gathering traffic for timestamp:  1458656026
# Popular hit:  ('/landing', 2)

# Gathering traffic for timestamp:  1458656027
# Popular hit:  ('/chatty', 3)

# Gathering traffic for timestamp:  1458656028
# ..waiting for more data
# ..waiting for more data
# ..waiting for more data
# ..waiting for more data
# ..waiting for more data
# ..waiting for more data
# ..waiting for more data
# ..waiting for more data
# ..waiting for more data
# This timestamp is not yet a part of the log..

# Gathering traffic for timestamp:  1458656025
# Err..couldn't find timestamp from log file api calls
