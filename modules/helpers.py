from datetime import datetime
import json
import os
import re
import streamlit as st

# Base Project Directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Storage Folder Path
STORAGE_DIR = os.path.join(BASE_DIR, "storage")


# =========================
# INPUT VALIDATION
# =========================

def validate_input(input_text):

    # Remove unwanted spaces
    text = input_text.strip()

    # Check empty input
    if text == "":
        return False

    # Check minimum length
    if len(text) <= 1:
        return False

    # Check repeated symbols spam
    if re.fullmatch(r"[!@#$%^&*()_+=/<>?.,\\-]+", text):
        return False

    return True


# =========================
# RESPONSE FORMATTING
# =========================

def format_response(output_text):

    if not output_text:
        return ""

    text = output_text.strip()
    
    # Remove bold markers
    text = re.sub(r"\*\*", "", text)
    
    # Remove triple stars
    text = re.sub(r"\*{3,}", "", text)

    # Remove multiple underscores
    text = re.sub(r"_{2,}", "", text)

    # Remove opening code fences
    text = re.sub(r"```[a-zA-Z0-9_+-]*", "", text)

    # Remove closing code fences
    text = re.sub(r"```", "", text)

    # Normalize line endings
    text = text.replace("\r\n", "\n")
    text = text.replace("\r", "\n")

    # Remove trailing spaces
    text = re.sub(r"[ \t]+$", "", text, flags=re.MULTILINE)

    # ----------------------------------
    # Fix numbered lists
    # Example:
    # 1.First -> 1. First
    # ----------------------------------
    text = re.sub(r"(?m)^(\d+)\.(\S)", r"\1. \2", text)

    # Process line-by-line
    lines = text.split("\n")

    cleaned_lines = []

    for line in lines:

        line = line.strip()

        if not line:
            cleaned_lines.append("")
            continue

        # Ensure blank line after headings
        text = re.sub(r"(#{1,6}\s.*)\n(?!\n)", r"\1\n\n", text)

        # Fix accidental multiple spaces
        line = re.sub(r"[ ]{2,}", " ", line)

        cleaned_lines.append(line)

    # Rejoin text
    text = "\n".join(cleaned_lines)

    # Reduce excessive blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)

    # ----------------------------------
    # Add spacing after common headings
    # ----------------------------------
    section_titles = [
        "Overview",
        "Explanation",
        "Example",
        "Examples",
        "Solution",
        "Benefits",
        "Advantages",
        "Disadvantages",
        "Summary",
        "Conclusion",
        "Key Points",
        "Step-by-Step Explanation",
        "Action Plan",
        "Workout Plan",
        "Career Advice",
        "Code Implementation"
    ]

    for title in section_titles:

        pattern = rf"(?m)^({re.escape(title)}:?)$"

        text = re.sub(pattern, r"\1\n", text)

    # Final cleanup
    text = text.strip()

    return text

# =========================
# SESSION STATE
# =========================

def initialize_session_state():

    if "messages" not in st.session_state:
        st.session_state.messages = []

    if "selected_mode" not in st.session_state:
        st.session_state.selected_mode = "Study Teacher"

    if "chat_started" not in st.session_state:
        st.session_state.chat_started = False


# =========================
# CURRENT TIMESTAMP
# =========================

def get_current_timestamp():

    return datetime.now().strftime("%d-%m-%Y %H:%M:%S")

# =========================
# CHAT MESSAGE STRUCTURE
# =========================

def create_chat_message(role, personality, content):

    return {
        "role": role,
        "personality" : personality,
        "content": content,
        "timestamp": get_current_timestamp()
    }

# =========================
# STORAGE FOLDER CREATION
# =========================

def create_storage_folder():

    os.makedirs(STORAGE_DIR, exist_ok=True)


# =========================
# GENERATE CHAT FILENAME
# =========================

def generate_chat_filename():

    create_storage_folder()

    numbers = []

    for file in os.listdir(STORAGE_DIR):

        match = re.search(
            r"chat_(\d+)\.json",
            file
        )

        if match:
            numbers.append(int(match.group(1)))

    next_num = max(numbers, default=0) + 1

    filename = f"chat_{next_num:03d}.json"

    filepath = os.path.join(STORAGE_DIR, filename)

    return filepath


# =========================
# SAVE CHAT HISTORY
# =========================

def save_chat_history(messages):

    filepath = generate_chat_filename()

    with open(filepath, "w", encoding="utf-8") as file:

        json.dump(
            messages,
            file,
            indent=4,
            ensure_ascii=False
        )

    return filepath


# =========================
# LOAD CHAT HISTORY
# =========================

def load_chat_history(filepath):

    with open(filepath, "r", encoding="utf-8") as file:

        messages = json.load(file)

    return messages


# =========================
# CLEAR CHAT HISTORY
# =========================

def clear_chat_history():

    st.session_state.messages = []


# =========================
# TRUNCATE CHAT HISTORY
# =========================

def truncate_chat_history(messages, limit=10):

    return messages[-limit:]


# =========================
# EXPORT CHAT AS TEXT
# =========================

def export_chat_as_text(messages):

    chat_text = ""

    for msg in messages:

        role = msg["role"].capitalize()
        content = msg["content"]

        chat_text += f"{role}: {content}\n\n"

    return chat_text


# =========================
# SANITIZE FILENAME
# =========================

def sanitize_filename(filename):

    cleaned_name = re.sub(
        r'[\\\\/*?:"<>|]',
        "",
        filename
    )

    return cleaned_name


# =========================
# WORD COUNT
# =========================

def count_words(text):

    words = text.split()

    return len(words)


# =========================
# LIMIT PROMPT SIZE
# =========================

def limit_prompt_size(text, max_chars=3000):

    if len(text) > max_chars:

        return text[:max_chars]

    return text


# =========================
# DETECT USER INTENT
# =========================

def detect_user_intent(user_input):

    text = user_input.lower()

    if "python" in text or "code" in text:
        return "coding"

    elif "workout" in text or "gym" in text:
        return "fitness"

    elif "resume" in text or "career" in text:
        return "career"

    elif "health" in text or "sleep" in text:
        return "health"

    else:
        return "general"