# ============================================================
# utils/styles.py — Styling for Multi-Personality AI Chatbot
# ============================================================
# All CSS lives here. Import apply_styles() into app.py only.
# ============================================================

import streamlit as st

# ============================================================
# CSS VARIABLE PALETTE & GLOBAL STYLES
# ============================================================

CUSTOM_CSS = """
<style>

/* ── Google Fonts ─────────────────────────────────────────── */
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600&family=DM+Mono:wght@400;500&display=swap');

/* ── Design Tokens ────────────────────────────────────────── */
:root {
    --bg-base:       #0f1117;
    --bg-surface:    #171b26;
    --bg-elevated:   #1e2330;
    --bg-hover:      #252b3b;

    --border:        #2a3045;
    --border-subtle: #1f2535;

    --accent:        #4f8ef7;
    --accent-dim:    #2a4a8a;
    --accent-glow:   rgba(79, 142, 247, 0.15);

    --text-primary:  #e8ecf4;
    --text-secondary:#8b95aa;
    --text-muted:    #535d72;

    --success:       #3ecf8e;
    --warning:       #f7c948;
    --error:         #f76f6f;

    --radius-sm:     6px;
    --radius-md:     10px;
    --radius-lg:     16px;

    --shadow-sm:     0 1px 3px rgba(0,0,0,0.3);
    --shadow-md:     0 4px 12px rgba(0,0,0,0.4);
    --shadow-lg:     0 8px 24px rgba(0,0,0,0.5);

    --font-sans:     'DM Sans', sans-serif;
    --font-mono:     'DM Mono', monospace;
}

/* ── Global Reset ─────────────────────────────────────────── */
*, *::before, *::after {
    box-sizing: border-box;
}

html, body, [data-testid="stAppViewContainer"] {
    background-color: var(--bg-base) !important;
    color: var(--text-primary) !important;
    font-family: var(--font-sans) !important;
}

/* ── Hide Streamlit chrome ────────────────────────────────── */
#MainMenu, footer { visibility: hidden; }

/* Keep sidebar collapse button always visible */
[data-testid="collapsedControl"],
button[kind="header"],
.eyeqlp51,
[class*="collapsedControl"] {
    visibility: visible !important;
    opacity: 1 !important;
    display: flex !important;
    background-color: #1e2330 !important;
    border: 1px solid #2a3045 !important;
    border-radius: 8px !important;
    color: #e8ecf4 !important;
}

[data-testid="collapsedControl"] svg,
[class*="collapsedControl"] svg {
    fill: #8b95aa !important;
    color: #8b95aa !important;
}

[data-testid="collapsedControl"]:hover,
[class*="collapsedControl"]:hover {
    background-color: #252b3b !important;
    border-color: #2a4a8a !important;
}

/* ── Main Content Area ────────────────────────────────────── */
[data-testid="stMain"] {
    background-color: var(--bg-base) !important;
}

.main .block-container {
    padding: 2rem 2.5rem 4rem !important;
    max-width: 860px !important;
}

/* ── Page Title ───────────────────────────────────────────── */
.main-title {
    font-size: 1.9rem;
    font-weight: 600;
    color: var(--text-primary);
    letter-spacing: -0.02em;
    margin-bottom: 0.3rem;
}

.main-desc {
    font-size: 0.9rem;
    color: var(--text-secondary);
    margin-bottom: 1.8rem;
    line-height: 1.5;
}

/* ── Sidebar ──────────────────────────────────────────────── */
[data-testid="stSidebar"] {
    background-color: var(--bg-surface) !important;
    border-right: 1px solid var(--border) !important;
    padding: 0 !important;
}

[data-testid="stSidebar"] > div:first-child {
    padding: 1.8rem 1.4rem !important;
}

.sidebar-title {
    font-size: 1.3rem;
    font-weight: 600;
    color: var(--text-primary);
    letter-spacing: -0.02em;
    margin-bottom: 0.4rem;
}

.sidebar-desc {
    font-size: 0.8rem;
    color: var(--text-secondary);
    line-height: 1.5;
    margin-bottom: 0.2rem;
}

.sidebar-divider {
    border: none;
    border-top: 1px solid var(--border);
    margin: 1.1rem 0;
}

.sidebar-section-label {
    font-size: 0.7rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    color: var(--text-muted);
    margin-bottom: 0.6rem;
}

/* ── Personality Badge ────────────────────────────────────── */
.personality-badge {
    display: inline-block;
    margin-top: 0.6rem;
    padding: 0.3rem 0.8rem;
    background: var(--accent-glow);
    border: 1px solid var(--accent-dim);
    color: var(--accent);
    border-radius: 20px;
    font-size: 0.8rem;
    font-weight: 500;
}

/* ── Sidebar Footer ───────────────────────────────────────── */
.sidebar-footer {
    margin-top: 2rem;
    font-size: 0.72rem;
    color: var(--text-muted);
    text-align: center;
    padding-top: 1rem;
    border-top: 1px solid var(--border-subtle);
}

/* ── Buttons ──────────────────────────────────────────────── */
[data-testid="stSidebar"] .stButton > button {
    background-color: var(--bg-elevated) !important;
    color: var(--text-primary) !important;
    border: 1px solid var(--border) !important;
    border-radius: var(--radius-md) !important;
    padding: 0.5rem 1rem !important;
    font-family: var(--font-sans) !important;
    font-size: 0.84rem !important;
    font-weight: 500 !important;
    transition: background 0.15s, border-color 0.15s !important;
    margin-bottom: 0.4rem !important;
    box-shadow: var(--shadow-sm) !important;
}

[data-testid="stSidebar"] .stButton > button:hover {
    background-color: var(--bg-hover) !important;
    border-color: var(--accent-dim) !important;
    color: var(--accent) !important;
}

/* ── Download Button ──────────────────────────────────────── */
[data-testid="stSidebar"] .stDownloadButton > button {
    background-color: var(--accent-glow) !important;
    color: var(--accent) !important;
    border: 1px solid var(--accent-dim) !important;
    border-radius: var(--radius-md) !important;
    font-size: 0.84rem !important;
    font-weight: 500 !important;
    font-family: var(--font-sans) !important;
    transition: background 0.15s !important;
    box-shadow: none !important;
}

[data-testid="stSidebar"] .stDownloadButton > button:hover {
    background-color: var(--accent-dim) !important;
    color: #fff !important;
}

/* ── Sidebar collapse/expand toggle button ───────────────── */
[data-testid="collapsedControl"] {
    background-color: var(--bg-surface) !important;
    border: 1px solid var(--border) !important;
    border-radius: var(--radius-md) !important;
    color: var(--text-primary) !important;
    opacity: 1 !important;
    visibility: visible !important;
}

[data-testid="collapsedControl"]:hover {
    background-color: var(--bg-hover) !important;
    border-color: var(--accent-dim) !important;
}

[data-testid="collapsedControl"] svg {
    fill: var(--text-secondary) !important;
}

/* ── Statistics ───────────────────────────────────────────── */
.stat-box {
    background: var(--bg-elevated);
    border: 1px solid var(--border);
    border-radius: var(--radius-md);
    padding: 0.7rem 0.4rem;
    text-align: center;
    font-size: 0.75rem;
    color: var(--text-secondary);
    line-height: 1.6;
}

.stat-num {
    font-size: 1.4rem;
    font-weight: 600;
    color: var(--text-primary);
    font-family: var(--font-mono);
}

.stat-words {
    font-size: 0.78rem;
    color: var(--text-secondary);
    margin-top: 0.6rem;
    padding: 0.5rem 0.6rem;
    background: var(--bg-elevated);
    border: 1px solid var(--border-subtle);
    border-radius: var(--radius-sm);
}

/* ── Selectbox ────────────────────────────────────────────── */
[data-testid="stSelectbox"] > div > div {
    background-color: var(--bg-elevated) !important;
    border: 1px solid var(--border) !important;
    border-radius: var(--radius-md) !important;
    color: var(--text-primary) !important;
    font-family: var(--font-sans) !important;
    font-size: 0.875rem !important;
}

/* ── Chat Messages ────────────────────────────────────────── */
[data-testid="stChatMessage"] {
    background-color: var(--bg-surface) !important;
    border: 1px solid var(--border-subtle) !important;
    border-radius: var(--radius-lg) !important;
    padding: 1rem 1.2rem !important;
    margin-bottom: 0.8rem !important;
    box-shadow: var(--shadow-sm) !important;
    font-size: 0.9rem !important;
    line-height: 1.65 !important;
}

/* User message — slightly brighter surface */
[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]) {
    background-color: var(--bg-elevated) !important;
    border-color: var(--border) !important;
}

/* ── Message Timestamp ────────────────────────────────────── */
.msg-timestamp {
    font-size: 0.7rem;
    color: var(--text-muted);
    margin-top: 0.5rem;
    font-family: var(--font-mono);
}

/* ── Chat Input ───────────────────────────────────────────── */
[data-testid="stChatInput"],
[data-testid="stChatInput"] > div,
[data-testid="stChatInput"] > div > div,
[data-testid="stChatInput"] > div > div > div,
.stChatInput,
.stChatInput > div,
.stChatInput > div > div {
    background: transparent !important;
    background-color: transparent !important;
    border: none !important;
    border-radius: 0 !important;
    box-shadow: none !important;
    padding: 0 !important;
}

/* Only the outermost wrapper gets the styled border */
[data-testid="stChatInput"] {
    background: linear-gradient(135deg, #1a1f2e 0%, #12151f 100%) !important;
    border: 1px solid #3a4060 !important;
    border-radius: 14px !important;
    box-shadow: 0 -2px 20px rgba(0,0,0,0.5) !important;
    padding: 0.4rem 0.6rem !important;
}

[data-testid="stChatInput"] textarea,
[data-testid="stChatInput"] textarea:focus,
[data-testid="stChatInput"] p,
.stChatInput textarea {
    background: transparent !important;
    background-color: transparent !important;
    border: none !important;
    outline: none !important;
    box-shadow: none !important;
    color: #ffffff !important;
    -webkit-text-fill-color: #ffffff !important;
    font-family: var(--font-sans) !important;
    font-size: 0.92rem !important;
    font-weight: 400 !important;
    caret-color: #4f8ef7 !important;
    line-height: 1.6 !important;
    width: 100% !important;
    resize: none !important;
    padding: 0.5rem 0.75rem !important;
}

[data-testid="stChatInput"] textarea::placeholder,
.stChatInput textarea::placeholder {
    color: #535d72 !important;
    -webkit-text-fill-color: #535d72 !important;
    opacity: 1 !important;
}

/* ── Empty Chat State ─────────────────────────────────────── */
.empty-chat {
    text-align: center;
    color: var(--text-muted);
    font-size: 0.87rem;
    padding: 3rem 1rem;
    border: 1px dashed var(--border);
    border-radius: var(--radius-lg);
    margin: 1rem 0 2rem;
}

/* ── Alerts ───────────────────────────────────────────────── */
[data-testid="stAlert"] {
    border-radius: var(--radius-md) !important;
    font-size: 0.85rem !important;
    font-family: var(--font-sans) !important;
}

/* ── Spinner ──────────────────────────────────────────────── */
[data-testid="stSpinner"] p {
    color: var(--text-secondary) !important;
    font-size: 0.85rem !important;
    font-family: var(--font-sans) !important;
}

/* ── Success / Warning / Error toast ──────────────────────── */
.stSuccess {
    background-color: rgba(62, 207, 142, 0.1) !important;
    border-left: 3px solid var(--success) !important;
    color: var(--success) !important;
}

.stWarning {
    background-color: rgba(247, 201, 72, 0.1) !important;
    border-left: 3px solid var(--warning) !important;
    color: var(--warning) !important;
}

.stError {
    background-color: rgba(247, 111, 111, 0.1) !important;
    border-left: 3px solid var(--error) !important;
    color: var(--error) !important;
}

/* ── Scrollbar ────────────────────────────────────────────── */
::-webkit-scrollbar { width: 5px; height: 5px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb {
    background: var(--border);
    border-radius: 10px;
}
::-webkit-scrollbar-thumb:hover { background: var(--text-muted); }

/* ── Code blocks inside chat ──────────────────────────────── */
code {
    font-family: var(--font-mono) !important;
    background: var(--bg-elevated) !important;
    color: var(--accent) !important;
    padding: 0.15em 0.4em !important;
    border-radius: 4px !important;
    font-size: 0.85em !important;
}

pre code {
    display: block !important;
    padding: 1rem !important;
    overflow-x: auto !important;
    border: 1px solid var(--border) !important;
    border-radius: var(--radius-md) !important;
}

/* ── Force input text always white (nuclear override) ──────── */
div[class*="stChatInput"] textarea,
div[class*="stChatInput"] div[contenteditable],
section[data-testid="stBottom"] textarea,
section[data-testid="stBottom"] input {
    color: #ffffff !important;
    -webkit-text-fill-color: #ffffff !important;
    background: transparent !important;
}

div[class*="stChatInput"] {
    background: linear-gradient(135deg, #1a1f2e, #0f1117) !important;
    border-radius: 14px !important;
    border: 1px solid #3a4060 !important;
}

</style>
"""

# ============================================================
# APPLY STYLES — called once from app.py
# ============================================================

def apply_styles():
    """Inject the custom CSS into the Streamlit app."""
    st.markdown(CUSTOM_CSS, unsafe_allow_html=True)