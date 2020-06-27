# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase03GetStateCumulativeReportAPITestCase::test_case status'] = 200

snapshots['TestCase03GetStateCumulativeReportAPITestCase::test_case body'] = {
    'districts': [
        {
            'district_id': 1,
            'district_name': 'district 0',
            'total_active_cases': 26,
            'total_confirmed_cases': 35,
            'total_deaths': 1,
            'total_recovered_cases': 8
        }
    ],
    'state_name': 'state 0',
    'total_active_cases': 26,
    'total_confirmed_cases': 35,
    'total_deaths': 1,
    'total_recovered_cases': 8
}

snapshots['TestCase03GetStateCumulativeReportAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '295',
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
