
conversation = []


def get_history():
    return conversation


def add_message(role: str, content: str):
    conversation.append({
        "role": role,
        "content": content
    })


def clear_history():
    conversation.clear()
