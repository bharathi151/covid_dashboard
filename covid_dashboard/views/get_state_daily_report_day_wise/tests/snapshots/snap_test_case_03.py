# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase03GetStateDailyReportDayWiseAPITestCase::test_case status'] = 200

snapshots['TestCase03GetStateDailyReportDayWiseAPITestCase::test_case body'] = {
    'day_wise_statistics': [
        {
            'date': '23/06/2020',
            'total_confirmed_cases': 15,
            'total_deaths': 0,
            'total_recovered_cases': 3
        },
        {
            'date': '24/06/2020',
            'total_confirmed_cases': 0,
            'total_deaths': 0,
            'total_recovered_cases': 0
        },
        {
            'date': '25/06/2020',
            'total_confirmed_cases': 20,
            'total_deaths': 1,
            'total_recovered_cases': 5
        }
    ],
    'state_name': 'state 0'
}

snapshots['TestCase03GetStateDailyReportDayWiseAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '349',
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
