# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01SignInUserAPITestCase::test_case status'] = 200

snapshots['TestCase01SignInUserAPITestCase::test_case body'] = {
    'access_token': 'string',
    'expires_in': 'string',
    'refresh_token': 'string',
    'user_id': 1
}

snapshots['TestCase01SignInUserAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '84',
        'Content-Length'
    ],
    'content-type': [
        'Content-Type',
        'application/json'
    ],
    'vary': [
        'Accept-Language, Origin',
        'Vary'
    ],
    'x-frame-options': [
        'DENY',
        'X-Frame-Options'
    ]
}
