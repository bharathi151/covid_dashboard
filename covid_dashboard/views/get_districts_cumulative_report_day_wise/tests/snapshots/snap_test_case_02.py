# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02GetDistrictsCumulativeReportDayWiseAPITestCase::test_case status'] = 200

snapshots['TestCase02GetDistrictsCumulativeReportDayWiseAPITestCase::test_case body'] = [
    {
        'day_wise_statistics': [
        ],
        'district_id': 1,
        'district_name': 'district 0'
    },
    {
        'day_wise_statistics': [
        ],
        'district_id': 2,
        'district_name': 'district 1'
    }
]

snapshots['TestCase02GetDistrictsCumulativeReportDayWiseAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '156',
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
