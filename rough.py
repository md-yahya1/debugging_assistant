# ======================================================
# Test 1 -> Config (COMMENTED)
# ======================================================

# from config.model_config import load_config
# cfg = load_config()
# print(cfg.model)
# print(cfg.debugging_app)


# ======================================================
# Test 2 -> Direct Gemini SDK (COMMENTED)
# ======================================================

# from google import genai
# import os
#
# client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
#
# response = client.models.generate_content(
#     model="models/gemini-pro-latest",
#     contents="What is the capital of India?"
# )
#
# print(response.text)


# ======================================================
# Test 3 -> Hugging Face LLM Client (ACTIVE ✅)
# ======================================================
#response = llm.ask("What is the capital of India?")
#print(response)

# # Test 4
# import json 
# from utils.llm_client import HuggingFaceClient
# from pathlib import Path

# prompt_path = Path("utils/prompts/debugging_prompt.json")
# data = json.loads(prompt_path.read_text())

# system_instruction = data["system_instruction"]
# template = data["user_prompt_template"]

# user_input = "print(Hello World)"

# prompt = system_instruction + "\n\n" + template.replace("{{USER_INPUT}}", user_input)

# client = HuggingFaceClient()
# print(client.ask(prompt))

# ======================================================
# Test 5 -> Debugging helper test (COMMENTED)
# ======================================================

from utils.llm_client import HuggingFaceClient
from utils.debugging_helper import build_debugging_prompt

client = HuggingFaceClient()

user_code = "x = 5\nprint('x')"
prompt = build_debugging_prompt(user_code)

result = client.ask(prompt)
print(result)