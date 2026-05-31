# ============================================================
# app.py — Multi-Personality AI Chatbot
# Built with Streamlit + Gemini API
# ============================================================

# ============================================================
# 1. IMPORT LIBRARIES
# ============================================================

import streamlit as st
from modules.chatbot import generate_output
from modules.helpers import (
    validate_input,
    format_response,
    initialize_session_state,
    create_chat_message,
    save_chat_history,
    clear_chat_history,
    truncate_chat_history,
    export_chat_as_text,
    limit_prompt_size,
    count_words,
)
from modules.styles import apply_styles

# ============================================================
# 2. CONFIGURE STREAMLIT PAGE
# ============================================================

st.set_page_config(
    page_title="AI Chatbot",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ============================================================
# 3. IMPORT AND APPLY EXTERNAL STYLES
# ============================================================

apply_styles()

# ============================================================
# 4. INITIALIZE SESSION STATE
# ============================================================

initialize_session_state()

# ============================================================
# PERSONALITY ROLE MAPPING
# Maps display names → keys used in prompts.json
# ============================================================

PERSONALITY_MAP = {
    "Study Teacher":    "study_teacher",
    "Career Assistant": "career_assistant",
    "Fitness Coach":    "fitness_coach",
    "Coding Mentor":    "coding_mentor",
    "Health Partner":   "health_partner",
}

PERSONALITY_ICONS = {
    "Study Teacher":    "📚",
    "Career Assistant": "💼",
    "Fitness Coach":    "🏋️",
    "Coding Mentor":    "💻",
    "Health Partner":   "🩺",
}

# ============================================================
# 5. SIDEBAR
# ============================================================

with st.sidebar:

    # -- Title & Description --
    st.markdown('<div class="sidebar-title">AI Chatbot</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="sidebar-desc">Your personal AI assistant with multiple expert personalities.</div>',
        unsafe_allow_html=True,
    )
    st.markdown('<hr class="sidebar-divider"/>', unsafe_allow_html=True)

    # --------------------------------------------------------
    # 6. CHATBOT PERSONALITY SELECTOR
    # --------------------------------------------------------

    st.markdown('<div class="sidebar-section-label">Choose Personality</div>', unsafe_allow_html=True)

    selected_mode = st.selectbox(
        label="Personality",
        options=list(PERSONALITY_MAP.keys()),
        index=list(PERSONALITY_MAP.keys()).index(st.session_state.selected_mode)
              if st.session_state.selected_mode in PERSONALITY_MAP else 0,
        label_visibility="collapsed",
    )

    # Persist selection
    st.session_state.selected_mode = selected_mode

    # Show active personality badge
    icon = PERSONALITY_ICONS.get(selected_mode, "🤖")
    st.markdown(
        f'<div class="personality-badge">{icon} {selected_mode}</div>',
        unsafe_allow_html=True,
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # --------------------------------------------------------
    # 7. SIDEBAR BUTTONS
    # --------------------------------------------------------

    st.markdown('<div class="sidebar-section-label">Actions</div>', unsafe_allow_html=True)

    # -- Clear Chat Button --
    if st.button("Clear Chat", use_container_width=True, key="clear_btn"):
        clear_chat_history()
        st.session_state.chat_started = False
        st.rerun()

    # -- Save Chat Button --
    if st.button("Save Chat", use_container_width=True, key="save_btn"):
        if st.session_state.messages:
            filepath = save_chat_history(st.session_state.messages)
            st.success(f"Chat saved!")
        else:
            st.warning("No messages to save.")

    # -- Download Chat Button --
    if st.session_state.messages:
        chat_text = export_chat_as_text(st.session_state.messages)
        st.download_button(
            label="Download Chat (.txt)",
            data=chat_text,
            file_name="chat_export.txt",
            mime="text/plain",
            use_container_width=True,
            key="download_btn",
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # --------------------------------------------------------
    # STATISTICS SECTION
    # --------------------------------------------------------

    st.markdown('<div class="sidebar-section-label">Statistics</div>', unsafe_allow_html=True)

    total_messages = len(st.session_state.messages)
    user_messages  = sum(1 for m in st.session_state.messages if m["role"] == "user")
    ai_messages    = total_messages - user_messages

    total_words = sum(
        count_words(m["content"])
        for m in st.session_state.messages
    )

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f'<div class="stat-box"><span class="stat-num">{user_messages}</span><br>You</div>',
                    unsafe_allow_html=True)
    with col2:
        st.markdown(f'<div class="stat-box"><span class="stat-num">{ai_messages}</span><br>AI</div>',
                    unsafe_allow_html=True)

    st.markdown(
        f'<div class="stat-words">Total words exchanged: <strong>{total_words}</strong></div>',
        unsafe_allow_html=True,
    )

    # -- Footer --
    st.markdown(
        '<div class="sidebar-footer">Powered by Gemini API</div>',
        unsafe_allow_html=True,
    )

# ============================================================
# 6. MAIN CHAT AREA
# ============================================================

st.markdown('<div class="main-title">AI Chatbot</div>', unsafe_allow_html=True)
st.markdown(
    f'<div class="main-desc">Currently active: <strong>{icon} {selected_mode}</strong> — ask anything to get started.</div>',
    unsafe_allow_html=True,
)

# ============================================================
# 8. DISPLAY CHAT HISTORY
# ============================================================

chat_container = st.container()

with chat_container:
    if not st.session_state.messages:
        st.markdown(
            '<div class="empty-chat">No messages yet. Start the conversation below.</div>',
            unsafe_allow_html=True,
        )
    else:
        for message in st.session_state.messages:
            role      = message["role"]
            content   = message["content"]
            timestamp = message.get("timestamp", "")

            with st.chat_message(role):
                st.markdown(content)
                if timestamp:
                    st.markdown(
                        f'<div class="msg-timestamp">{timestamp}</div>',
                        unsafe_allow_html=True,
                    )

# ============================================================
# 9. USER INPUT
# ============================================================

user_input = st.chat_input("Ask anything...")

# ============================================================
# 10–17. INPUT PROCESSING FLOW
# ============================================================

if user_input:

    # STEP 1 — Validate input
    if not validate_input(user_input):
        st.warning("Please enter a valid message.")

    else:
        # STEP 2 — Limit prompt size
        user_input = limit_prompt_size(user_input, max_chars=3000)

        # STEP 3 — Create user message
        user_message = create_chat_message(role="user", personality= st.session_state.selected_mode, content=user_input)

        # STEP 4 — Append user message to session
        st.session_state.messages.append(user_message)
        st.session_state.chat_started = True

        # Display user message immediately
        with st.chat_message("user"):
            st.markdown(user_input)
            st.markdown(
                f'<div class="msg-timestamp">{user_message["timestamp"]}</div>',
                unsafe_allow_html=True,
            )

        # STEP 5 — Generate AI response
        with st.spinner("Generating response..."):
            try:
                # Truncate history before sending to model (token management)
                truncated = truncate_chat_history(st.session_state.messages, limit=10)

                # Map display name → prompt key
                role_key = PERSONALITY_MAP.get(st.session_state.selected_mode, "study_teacher")

                # Call chatbot
                raw_response = generate_output(user_input, role_key)

                # STEP 6 — Format AI response
                formatted_response = format_response(raw_response)

                # STEP 7 — Create assistant message
                assistant_message = create_chat_message(
                    role="assistant",
                    personality= role_key,
                    content=formatted_response,
                )

                # STEP 8 — Append assistant message
                st.session_state.messages.append(assistant_message)

                # Display assistant message
                with st.chat_message("assistant"):
                    st.markdown(formatted_response)
                    st.markdown(
                        f'<div class="msg-timestamp">{assistant_message["timestamp"]}</div>',
                        unsafe_allow_html=True,
                    )

            except Exception as e:
                st.error(f"Something went wrong while generating a response: {e}")