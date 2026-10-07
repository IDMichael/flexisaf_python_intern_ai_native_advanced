SYSTEM_INSTRUCTIONS = ("You are a concise backend engineering assistant. "
                       "Return only information supported by the supplied user text.")
DEVELOPER_INSTRUCTIONS = ("Summarise the user's text accurately. Use the required typed output contract. "
                          "Do not invent facts that are absent from the input.")

def build_user_prompt(text: str) -> str:
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("text must not be empty")
    return cleaned
