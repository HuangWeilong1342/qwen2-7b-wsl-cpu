import requests

from backend.services.prompt import load_system_prompt
from backend.services.history import (
    get_history,
    add_message
)

from backend.config import *


def chat(message: str):

    # 读取 System Prompt
    system_prompt = load_system_prompt()

    # 构造 messages
    messages = [
        {
            "role": "system",
            "content": system_prompt
        }
    ]

    # 添加历史记录
    messages.extend(get_history())

    # 添加当前用户消息
    messages.append(
        {
            "role": "user",
            "content": message
        }
    )

    # 保存用户消息
    add_message(
        "user",
        message
    )

    payload = {
        "model": MODEL_NAME,
        "messages": messages,
        "temperature": TEMPERATURE,
        "max_tokens": MAX_TOKENS
    }

    response = requests.post(
        LLM_API_URL,
        json=payload,
        timeout=TIMEOUT
    )

    response.raise_for_status()

    result = response.json()

    answer = result["choices"][0]["message"]["content"]

    # 保存 AI 回复
    add_message(
        "assistant",
        answer
    )

    return answer

