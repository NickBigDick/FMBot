from telebot.handler_backends import State, StatesGroup


class UserState(StatesGroup):
    name = State()
    my_requests = State()
    new_requests = State()
    set_moderator_attributes = State()
    find_family = State()
    find_family_by_id = State()
    find_family_by_versionid = State()
    add_json_version = State()