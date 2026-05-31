# Custom AI Chatbot

A multi-personality AI chatbot built using **Python**, **Streamlit**, and **Google Gemini API**. The application allows users to interact with different AI assistants, each designed for a specific purpose such as learning, career guidance, fitness coaching, coding support, and wellness advice.

---

## Project Overview

This project demonstrates how Large Language Models (LLMs) can be customized using prompt engineering to behave like different professional assistants.

Instead of giving generic answers, the chatbot responds according to the selected personality, providing more focused and relevant guidance.

The application is designed with a clean user interface, chat history management, response formatting, and conversation export functionality.

---

## Features

### Multiple AI Personalities

The chatbot supports the following specialized assistants:

* **Study Teacher**

  * Explains concepts in a simple and beginner-friendly way.
  * Provides step-by-step explanations and examples.

* **Career Assistant**

  * Offers career guidance, skill recommendations, interview preparation, and learning roadmaps.

* **Fitness Coach**

  * Provides workout suggestions, fitness guidance, recovery tips, and healthy habits.

* **Coding Mentor**

  * Helps with programming concepts, debugging, projects, and coding best practices.

* **Health Partner**

  * Gives general wellness advice, healthy lifestyle recommendations, and productivity tips.

---

### Smart Response Formatting

* Cleans AI-generated responses.
* Improves readability and structure.
* Handles headings, lists, spacing, and formatting issues.
* Displays responses in a user-friendly format.

---

### Chat History Management

* Stores conversation history during the session.
* Allows users to clear conversations.
* Supports saving chat history to local storage.

---

### Chat Export

* Export conversations as text files.
* Useful for future reference and documentation.

---

### Modern Streamlit Interface

* Clean and responsive design.
* Sidebar controls for chatbot management.
* Interactive chat experience similar to modern AI assistants.

---

## Project Structure

```text
custom-ai-chatbot/
│
├── app.py
│
├── modules/
│   ├── chatbot.py
│   ├── helpers.py
│   └── styles.py
│
├── templates/
│   └── prompts.json
│
├── storage/
│
├── .env
├── requirements.txt
└── README.md
```

---

## Technologies Used

* Python
* Streamlit
* Google Gemini API
* JSON
* Regular Expressions (Regex)
* Prompt Engineering

---

## How It Works

1. User selects a chatbot personality.
2. User enters a question.
3. The selected personality prompt is loaded.
4. User input is combined with the personality instructions.
5. Gemini generates a response.
6. The response is cleaned and formatted.
7. The final answer is displayed in the chat interface.
8. Conversations can be saved or exported.

---

## Example Use Cases

### Study Teacher

**User:** Explain machine learning.

**Response:** Provides a beginner-friendly explanation with examples and key concepts.

---

### Coding Mentor

**User:** Explain Python lists.

**Response:** Gives code examples, explanations, and best practices.

---

### Career Assistant

**User:** How can I become a Data Analyst?

**Response:** Suggests skills, tools, projects, and a learning roadmap.

---

### Fitness Coach

**User:** Create a shoulder workout plan.

**Response:** Provides exercises, workout structure, and recovery guidance.

---

### Health Partner

**User:** How can I improve my sleep schedule?

**Response:** Suggests healthy habits and practical wellness tips.

---

## Learning Outcomes

Through this project, I learned:

* Building AI-powered applications using LLMs
* Prompt engineering techniques
* Streamlit application development
* API integration
* Session state management
* Response formatting using Regex
* Modular project architecture
* Chat history and file handling

---

## Future Improvements

* Voice-based interaction
* PDF document chat
* User authentication
* Multiple conversation sessions
* Conversation search
* Database integration
* Dark/Light theme switch
* Chat analytics dashboard

---

## Author

**Rajesh Jella**

Built as part of an AI and Generative AI internship project to demonstrate practical implementation of Large Language Models, prompt engineering, and Streamlit application development.
