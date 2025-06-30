from graph import app
from jinja2 import Template

# Load template
with open("templates/response_template.md", "r", encoding="utf-8") as f:
    template_text = f.read()
template = Template(template_text)

if __name__ == "__main__":
    print("Welcome to MamaCare 👶🌸")
    question = input("Ask a pregnancy-related question: ")
    trimester = input("Which trimester are you in? (1st/2nd/3rd): ")
    diet = input("Your diet? (veg/non-veg): ")
    mood = input("How are you feeling today? (happy/sad/anxious): ")

    result = app.invoke({
        "user_input": question,
        "trimester": trimester,
        "diet": diet,
        "mood": mood
    })

    # Render response with the template
    formatted_response = template.render(
        qa_answer=result["qa_answer"],
        daily_tip=result["daily_tip"],
        reminders=result["reminders"],
        mood_response=result["mood_response"],
        time=result.get("time", "N/A")
    )

    print("\n" + formatted_response)
