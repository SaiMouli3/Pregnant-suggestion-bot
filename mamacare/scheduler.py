from apscheduler.schedulers.blocking import BlockingScheduler
from graph import app

def run_daily():
    result = app.invoke({
        "user_input": "Give today's tip",
        "trimester": "2nd",
        "diet": "vegetarian",
        "mood": "happy"
    })

    print("\n🌅 Good morning from MamaCare!\n")
    print("🩺 Tip of the Day:\n", result["daily_tip"])
    print("🔔 Reminders:\n", "\n".join(result["reminders"]))

scheduler = BlockingScheduler()
scheduler.add_job(run_daily, 'cron', hour=9, minute=0)  # Every day 9:00 AM

if __name__ == "__main__":
    print("📅 Starting daily health tip scheduler...")
    scheduler.start()
