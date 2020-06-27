# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase03GetStateCumulativeReportDayWiseAPITestCase::test_case status'] = 200

snapshots['TestCase03GetStateCumulativeReportDayWiseAPITestCase::test_case body'] = {
    'day_wise_statistics': [
        {
            'date': '23/06/2020',
            'total_active_cases': 12,
            'total_confirmed_cases': 15,
            'total_deaths': 0,
            'total_recovered_cases': 3
        },
        {
            'date': '24/06/2020',
            'total_active_cases': 12,
            'total_confirmed_cases': 15,
            'total_deaths': 0,
            'total_recovered_cases': 3
        },
        {
            'date': '25/06/2020',
            'total_active_cases': 26,
            'total_confirmed_cases': 35,
            'total_deaths': 1,
            'total_recovered_cases': 8
        }
    ],
    'state_name': 'state 0'
}

snapshots['TestCase03GetStateCumulativeReportDayWiseAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '428',
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
