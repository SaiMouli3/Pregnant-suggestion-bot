<!-- Response formatting template for MamaCare bot -->

# 🤖 MamaCare Assistant Response

## 🍼 Answer to Your Question
{{ qa_answer }}

---

## 🩺 Daily Health Tip
{{ daily_tip }}

---

## 🔔 Reminders
{% for reminder in reminders %}
- {{ reminder }}
{% endfor %}

---

## 💖 Mood Support
{{ mood_response }}

---

_🕰️ Time: {{ time }}_
