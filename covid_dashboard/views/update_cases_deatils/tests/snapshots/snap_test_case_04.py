# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase04UpdateCasesDeatilsAPITestCase::test_case status'] = 400

snapshots['TestCase04UpdateCasesDeatilsAPITestCase::test_case body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_CASES_DEATILS',
    'response': 'Invalid data, try with valid data'
}

snapshots['TestCase04UpdateCasesDeatilsAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '113',
        'Content-Length'
    ],
    'content-type': [
        'Content-Type',
        'text/html; charset=utf-8'
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
