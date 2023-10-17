#!/usr/bin/env python3
"""Mongodb Collection"""


def top_students(mongo_collection):
    """ Function prints all students in a collection sorted by the 
    average score """
    students = mongo_collection.aggregate(
        [
            {
                '$project': {
                    '_id': 1,
                    'name': 1,
                    'averageScore': {
                        '$avg': {
                            '$avg': '$topics.score',
                            },
                        },
                    'topics': 1,
                    },
                },
            {
                '$sort': {'averagScore': -1},
                },
            ]
        )
    return students
