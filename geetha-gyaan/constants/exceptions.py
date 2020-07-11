class InvalidDomainId(Exception):
    pass

class UserNotDomainFollower(Exception):
    pass

class InvalidPostIds(Exception):
    def __init__(self, invalid_post_ids):
        self.invalid_post_ids=invalid_post_ids

class InvalidLimit(Exception):
    def __init__(self, invalid_limit):
        self.invalid_limit=invalid_limit

class InvalidOffset(Exception):
    def __init__(self, invalid_offset):
        self.invalid_offset=invalid_offset