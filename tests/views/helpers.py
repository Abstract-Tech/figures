'''This module provides test helpers for Figures view tests

'''

from tests.factories import UserFactory

def create_test_users():
    '''
    Creates four test users to test the combination of permissions
    * regular_user (is_staff=False, is_superuser=False)
    * staff_user (is_staf=True, is_superuser=False)
    * super_user (is_staff=False, is_superuser=True)
    * superstaff_user (is_staff=True, is_superuser=True)
    '''
    return [
        UserFactory(username='regular_user'),
        UserFactory(username='staff_user', is_staff=True),
        UserFactory(username='super_user', is_superuser=True),
        UserFactory(username='superstaff_user', is_staff=True, is_superuser=True)
    ]


def is_response_paginated(response_data):
    """Checks if the response data dict has expected paginated results keys

    Returns True if it finds all the paginated keys, False otherwise
    """
    try:
        keys = response_data.keys()
    except AttributeError:
        # If we can't get keys, wer'e certainly not paginated
        return False
    return set(keys) == set([u'count', u'next', u'previous', u'results'])
