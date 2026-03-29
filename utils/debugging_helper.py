from pathlib import Path
import json


def load_debugging_prompt() -> dict:
    prompt_path = Path(__file__).resolve().parent / "prompts" / "debugging_prompt.json"
    if not prompt_path.exists():
        raise FileNotFoundError(f"Debugging prompt file not found: {prompt_path}")

    with open(prompt_path, "r", encoding="utf-8") as f:
        return json.load(f)


def build_debugging_prompt(user_input: str, language: str = "auto") -> str:
    prompt_json = load_debugging_prompt()

    system_instruction = prompt_json["system_instruction"]
    template = prompt_json["user_prompt_template"]

    context = f"Language Context: {language}\n\n" if language.lower() != "auto" else ""
    full_prompt = (
        system_instruction + "\n\n" +
        template.replace("{{USER_INPUT}}", context + user_input.strip())
    )

    return full_prompt