from pathlib import Path

PROMPT_PATH = Path(__file__).parent.parent / "prompts" / "system_prompt.txt"


def load_system_prompt() -> str:
    """
    读取系统 Prompt
    """
    with open(PROMPT_PATH, "r", encoding="utf-8") as f:
        return f.read().strip()


def build_prompt(question: str, context: str) -> str:
    """
    构建 RAG Prompt
    """

    system_prompt = load_system_prompt()

    prompt = f"""{system_prompt}

请根据下面提供的知识库内容回答用户问题。

【知识库】
{context}

【用户问题】
{question}

【回答】
"""

    return prompt
