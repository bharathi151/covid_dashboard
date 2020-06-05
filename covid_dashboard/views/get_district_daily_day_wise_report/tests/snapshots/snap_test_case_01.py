# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetDistrictDailyDayWiseReportAPITestCase::test_case status'] = 200

snapshots['TestCase01GetDistrictDailyDayWiseReportAPITestCase::test_case body'] = {
    'day_wise_statistics': [
        {
            'date': 'string',
            'total_confirmed_cases': 1,
            'total_deaths': 1,
            'total_recovered_cases': 1
        }
    ],
    'district_id': 1,
    'district_name': 'string'
}

snapshots['TestCase01GetDistrictDailyDayWiseReportAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '153',
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
