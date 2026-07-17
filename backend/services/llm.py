import requests

from backend.utils.logger import logger
from backend.services.rag import RAGService
from backend.services.history import (
    get_history,
    add_message
)

from backend.config import *


def chat(message: str):

    logger.info(f"User: {message}")
    rag = RAGService()
    rag_prompt = rag.build_prompt(message)

    messages = []

    # 添加历史记录
    messages.extend(get_history())

    # 添加当前用户消息
    messages.append(
        {
            "role": "user",
            "content": rag_prompt
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

    try:
        response = requests.post(
            LLM_API_URL,
            json=payload,
            timeout=TIMEOUT
        )

        response.raise_for_status()

    except requests.exceptions.ConnectionError:
        logger.error("Cannot connect to llama-server.")
        return "错误：无法连接到 llama-server。"

    except requests.exceptions.Timeout:
        logger.error("Request timeout.")
        return "错误：模型响应超时。"

    except requests.exceptions.RequestException as e:
        logger.error(str(e))
        return "错误：请求失败。"

    result = response.json()

    answer = result["choices"][0]["message"]["content"]

    logger.info(f"Assistant: {answer}")

    # 保存 AI 回复
    add_message(
        "assistant",
        answer
    )

    return answer

