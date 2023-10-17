#!/usr/bin/env python3
""" Function to list all documents"""
import pymongo


def list_all(mongo_collection):
    """fuction lists all collections and returns empty list
     if no document is found"""
    return [doc for doc in mongo_collection.find()]

