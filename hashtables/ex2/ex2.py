#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = []

    for tix in tickets:
        source = tix.source
        destination = tix.destination

        hash_table_insert(hashtable, source, destination)

    # find the origin
    destination = hash_table_retrieve(hashtable, 'NONE')

    # print(destination)

    while destination != 'NONE':  # loop inserting hashtable then stop at 'NONE'

        route.append(destination)
        destination = hash_table_retrieve(hashtable, destination)

        # print(route)

    return route

