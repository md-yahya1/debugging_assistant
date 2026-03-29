def build_code_generation_prompt(user_request: str, language: str = "python") -> str:
    """Build a prompt for code generation using Deepseek Coder"""

    system_instruction = (
        f"You are an expert code generation AI assistant powered by Deepseek Coder. "
        f"Generate clean, efficient, and well-commented {language} code based on user requests. "
        f"Follow best practices and include docstrings where appropriate."
    )

    template = f"""Generate {language} code for the following task:

{{USER_REQUEST}}

Requirements:
- Provide working, production-ready code
- Include docstrings and comments
- Handle edge cases
- Use clear variable names
- Follow {language} best practices

Code:"""

    full_prompt = (
        system_instruction + "\n\n" +
        template.replace("{{USER_REQUEST}}", user_request.strip())
    )

    return full_prompt
