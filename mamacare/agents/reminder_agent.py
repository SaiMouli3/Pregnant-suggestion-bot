from datetime import datetime

def reminder_agent(state: dict) -> dict:
    now = datetime.now().strftime("%I:%M %p")

    reminders = [
        "⏰ Time to drink water 💧",
        "💊 Take your prenatal vitamins!",
        "🛌 Stretch your legs if sitting too long.",
        "📅 Log your baby's kick count!"
    ]

    return {
        "reminders": reminders[:2],
        "time": now
    }
