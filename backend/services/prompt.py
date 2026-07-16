from pathlib import Path

PROMPT_PATH = Path(__file__).parent.parent / "prompts" / "system_prompt.txt"


def load_system_prompt() -> str:
    """
    读取系统 Prompt
    """
    with open(PROMPT_PATH, "r", encoding="utf-8") as f:
        return f.read().strip()
