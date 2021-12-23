from controllers.message import get_time_send_sorted_message


def get_validate_message(sender_id: int, recipient_id: int):
    messages = get_time_send_sorted_message(sender_id, recipient_id)
    for message in messages:
        if message.id == recipient_id:
            message.send_from_me = True
        else:
            message.send_from_me = False
    return messages
