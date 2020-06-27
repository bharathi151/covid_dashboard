# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetDistrictsCumulativeReportDayWiseAPITestCase::test_case status'] = 200

snapshots['TestCase01GetDistrictsCumulativeReportDayWiseAPITestCase::test_case body'] = [
    {
        'day_wise_statistics': [
            {
                'date': '27/06/2020',
                'total_active_cases': 7,
                'total_confirmed_cases': 10,
                'total_deaths': 0,
                'total_recovered_cases': 3
            }
        ],
        'district_id': 1,
        'district_name': 'district 0'
    },
    {
        'day_wise_statistics': [
            {
                'date': '27/06/2020',
                'total_active_cases': 14,
                'total_confirmed_cases': 20,
                'total_deaths': 1,
                'total_recovered_cases': 5
            }
        ],
        'district_id': 2,
        'district_name': 'district 1'
    }
]

snapshots['TestCase01GetDistrictsCumulativeReportDayWiseAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '403',
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
