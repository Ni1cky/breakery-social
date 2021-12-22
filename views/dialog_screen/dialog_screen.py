from controllers.message import get_time_send_sorted_message


def get_validate_message(sender_id: int, recipient_id: int):
    messages = get_time_send_sorted_message(sender_id, recipient_id)
    sent_messages = [message for message in messages if message.id == sender_id]
    received_messages = [message for message in messages if message.id == recipient_id]
    return sent_messages, received_messages
