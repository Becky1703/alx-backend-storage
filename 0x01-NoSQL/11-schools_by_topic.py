#!/usr/bin/env python3
"""Mongodb Collection"""


def schools_by_topic(mongo_collection, topic):
    """Function returns the list of schools having a specific topic"""
    topic_filter = {
        'topics': {
            '$elemMatch': {
                '$eq': topic,
                },
            }
        }
    return [doc for doc in mongo_collection.find(topic_filter)]
