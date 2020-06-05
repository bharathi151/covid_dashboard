# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetDistrictCumulativeReportAPITestCase::test_case status'] = 200

snapshots['TestCase01GetDistrictCumulativeReportAPITestCase::test_case body'] = {
    'district_id': 1,
    'district_name': 'string',
    'mandals': [
        {
            'mandal_id': 1,
            'mandal_name': 'string',
            'total_active_cases': 1,
            'total_confirmed_cases': 1,
            'total_deaths': 1,
            'total_recovered_cases': 1
        }
    ],
    'total_active_cases': 1,
    'total_confirmed_cases': 1,
    'total_deaths': 1,
    'total_recovered_cases': 1
}

snapshots['TestCase01GetDistrictCumulativeReportAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '277',
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
