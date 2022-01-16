import datetime

from controllers.user import get_user
from store.models.models import Dialog


def get_dialog(dialog_id: int):
    d = Dialog(user=get_user(1), last_message="", time_send=datetime.datetime.now(), is_read=False)
    return d