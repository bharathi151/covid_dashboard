# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01UpdateCasesDeatilsAPITestCase::test_case status'] = 200

snapshots['TestCase01UpdateCasesDeatilsAPITestCase::test_case body'] = {
    'date': '30/05/2020',
    'mandal_id': 1,
    'total_confirmed_cases': 3,
    'total_deaths': 1,
    'total_recovered_cases': 1
}

snapshots['TestCase01UpdateCasesDeatilsAPITestCase::test_case header_params'] = {
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

snapshots['TestCase01UpdateCasesDeatilsAPITestCase::test_case date'] = '30/05/2020'

snapshots['TestCase01UpdateCasesDeatilsAPITestCase::test_case mandal_id'] = 1

snapshots['TestCase01UpdateCasesDeatilsAPITestCase::test_case total_recovered_cases'] = 1

snapshots['TestCase01UpdateCasesDeatilsAPITestCase::test_case total_confirmed_cases'] = 3

snapshots['TestCase01UpdateCasesDeatilsAPITestCase::test_case total_deaths'] = 1
