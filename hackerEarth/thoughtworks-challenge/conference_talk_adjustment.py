#!/usr/bin/env python2

"""
Author: Archit Sharma <archit.py@gmail.com>

Usage: 
    $ python conference_talk_adjustment.py input_conf.txt

Prelude: Read up ./Conf_prob_statement

This program tries to adjust slots for talks 
in a conference; ingesting inputs from a file 
and supplying output in a specified format.

The algorithm applied here is explained using
inline comments. The crux of the solution though,
depends upon finding legible combinations of talks
to fill up morning sessions in both the tracks at
first, then bothering about filling in sessions 
in leftover slots for evening, post lunch.

The lightening talk has been included in Track 1
at the end at all times, since it is of only 5 mins.
The networking event starts right after the last session 
of any track, keeping in mind the slot 4-5 pm. """

import sys
import operator
from datetime import timedelta, datetime
from pprint import pprint

class AdjustSlots:
    def __init__(self, talk_list):
        self.begin = timedelta(hours=9)
        self.lunch = timedelta(hours=1)
        self.lightening = None
        self.talk_list = talk_list
        self.track_1 = {'early': [], 'eve': []}
        self.track_2 = {'early': [], 'eve': []}
        self.subsets = []
        self.talk_dicts = {}
        
    def find_combos(self, talks, window, partial=[]):
        if partial:
            slot = reduce(lambda x,y: x + y, [i[1] for i in partial])
        else:
            slot = timedelta(hours=0)

        if slot == window:
            self.subsets.append([i[0] for i in partial])
        if slot >= window:
            return
        for i in range(len(talks)):
            x = talks[i]
            available = talks[i+1:]
            self.find_combos(available, window, partial + [x])

    def clean_sort_list(self):
        for current in self.talk_list:
            try:
                current[1] = timedelta(minutes=int(current[1].rstrip('min')))
            except ValueError:
                pop_key = current
                self.lightening = "%s" % (current[0])
            except:
	        print "Unexpected error:", sys.exc_info()[0]
	        raise
            
        self.talk_list.remove(pop_key)
        self.talk_list = [item for item in sorted(self.talk_list, key=operator.itemgetter(1))]
        for item in self.talk_list:
            self.talk_dicts[item[0]] = item[1]
        
    def settle_schedule(self, window):
        self.find_combos(self.talk_list, window)


if __name__ == '__main__':     
    try:
        talk_list = []
        # read input from file
	with open(sys.argv[1], 'rb') as f:
	    for line in f.read().splitlines():
		x = line.split()
		talk_list.append([' '.join(x[:-1]), x[-1]])
    except IOError as e:
	quit("I/O error({0}): {1}".format(e.errno, e.strerror))
    except ValueError:
	quit("\n\n\tCould not convert data to an integer.\n")
    except KeyboardInterrupt:
	quit("\n\n\tYou aborted the program!\n")
    except:
	print "Unexpected error:", sys.exc_info()[0]
	raise

    # initialize object, passing in talk_list as list of lists
    # containing [talk_title, timestamp]
    AS = AdjustSlots(talk_list)
    # clean the timestamp. Eg: 60min to a timedelta object
    AS.clean_sort_list()

    # use this list to keep track of talks already proposed
    # and check before sessions are allotted. 
    titles = []

    # supply a time window of 3 hours and find all possible
    # combinations of talks; then fill up the track sessions,
    # filtering out talks already proposed and breaking off the
    # loop at a point when all sessions have filled up
    AS.settle_schedule(timedelta(hours=3))
    for current in AS.subsets:
        if not AS.track_1['early']:
            AS.track_1['early'] = current
            titles += current
            continue

        if not AS.track_2['early']:
            if set(current) & set(titles):
                continue                
            AS.track_2['early'] = current
            titles += current
            continue

        if not AS.track_1['eve']:
            if set(current) & set(titles):
                continue
            AS.track_1['eve'] = current
            titles += current
            continue
        
        if not AS.track_2['eve']:
            if set(current) & set(titles):
                continue
            AS.track_2['eve'] = current
            titles += current
            break

    # TRACK 1
    # datetime object here is taken as referenced,
    # because we need to format the time output in
    # AM/PM and it seems better to use this module
    # than do it manually.
    init_1 = datetime(1970,1,1,0,0) + AS.begin
    print("Track 1:") 
    # Track 1: morning sessions
    for track in AS.track_1['early']:
        print("%s %s"%(init_1.time().strftime("%I:%M%p"), track))
        init_1 += AS.talk_dicts[track]
    print("%s Lunch"%(init_1.time().strftime("%I:%M%p")))
    init_1 += AS.lunch
    # Track 1: evening sessions
    for track in AS.track_1['eve']:
        print("%s %s"%(init_1.time().strftime("%I:%M%p"), track))
        init_1 += AS.talk_dicts[track]
    print("%s %s lightening" % (init_1.time().strftime("%I:%M%p"), AS.lightening))
    init_1 += timedelta(minutes=5)
    print("%s Networking Event"%(init_1.time().strftime("%I:%M%p")))

    # TRACK 2
    print
    init_2 = datetime(1970,1,1,0,0) + AS.begin
    print("Track 2:")    
    # Track 2: morning sessions
    for track in AS.track_2['early']:
        print("%s %s"%(init_2.time().strftime("%I:%M%p"), track))
        init_2 += AS.talk_dicts[track]
    print("%s Lunch"%(init_2.time().strftime("%I:%M%p")))
    init_2 += AS.lunch
    # Track 2: evening sessions
    for track in AS.track_2['eve']:
        print("%s %s"%(init_2.time().strftime("%I:%M%p"), track))
        init_2 += AS.talk_dicts[track]
    print("%s Networking Event"%(init_2.time().strftime("%I:%M%p")))
