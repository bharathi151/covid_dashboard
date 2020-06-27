# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02GetStateDailyReportAPITestCase::test_case status'] = 200

snapshots['TestCase02GetStateDailyReportAPITestCase::test_case body'] = {
    'districts': [
        {
            'district_id': 1,
            'district_name': 'district 0',
            'total_confirmed_cases': 0,
            'total_deaths': 0,
            'total_recovered_cases': 0
        }
    ],
    'state_name': 'state 0',
    'total_confirmed_cases': 0,
    'total_deaths': 0,
    'total_recovered_cases': 0
}

snapshots['TestCase02GetStateDailyReportAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '241',
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
