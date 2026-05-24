from langchain_core.prompts import PromptTemplate

template = """
You are an expert AI code reviewer.

Analyze the provided code snippet carefully.

Rules:
- Do NOT execute the code
- Only analyze the given code
- Detect syntax issues
- Detect readability problems
- Detect bad coding practices
- Suggest improvements
- Consider the programming language

Programming Language:
{language}

Return output STRICTLY in this format:
{format_instructions}

Code:
{code}
"""

prompt = PromptTemplate(
    input_variables=[
        "code",
        "language",
        "format_instructions"
    ],
    template=template
)