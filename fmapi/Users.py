import json
from utils.request_to_api import send_request_to_api


class User:

    def __init__(self, user_email):
        self.user_email = user_email

    def get_user(self):

        response = send_request_to_api(f"https://fm-api.bimteam.ru/v1/Users/{self.user_email}")
        if response:
            file = json.loads(response.text)
            return file

    @property
    def get_user_id(self):
        if self.get_user():
            return self.get_user()['id']
        else:
            return None


if __name__ == "__main__":
    # user = User(get_userid_from_telegramusername('Niko0707'))
    user = User("tevosiannkh@pik.ru")
    print(user.get_user_id)
