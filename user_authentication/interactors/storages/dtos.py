from dataclasses import dataclass


@dataclass
class UserDTO:
    user_id: int
    name: str
    profile_pic_url: str
