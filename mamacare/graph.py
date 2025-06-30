from langgraph.graph import StateGraph
from typing import TypedDict
from agents.qa_agent import qa_agent
from agents.health_agent import health_agent
from agents.reminder_agent import reminder_agent
from agents.mood_agent import mood_agent

class MamaCareState(TypedDict, total=False):
    user_input: str
    qa_answer: str
    daily_tip: str
    reminders: list
    time: str
    mood: str
    mood_response: str
    trimester: str
    diet: str

graph = StateGraph(MamaCareState)

graph.add_node("qa", qa_agent)
graph.add_node("health", health_agent)
graph.add_node("reminder", reminder_agent)
graph.add_node("mood", mood_agent)

graph.set_entry_point("qa")
graph.add_edge("qa", "health")
graph.add_edge("health", "reminder")
graph.add_edge("reminder", "mood")
graph.set_finish_point("mood")

app = graph.compile()
