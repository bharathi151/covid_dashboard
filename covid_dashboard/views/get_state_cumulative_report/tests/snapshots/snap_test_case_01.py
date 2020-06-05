# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetStateCumulativeReportAPITestCase::test_case status'] = 400

snapshots['TestCase01GetStateCumulativeReportAPITestCase::test_case body'] = {
    'date': [
        'Date has wrong format. Use one of these formats instead: YYYY-MM-DD.'
    ]
}

snapshots['TestCase01GetStateCumulativeReportAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '81',
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
