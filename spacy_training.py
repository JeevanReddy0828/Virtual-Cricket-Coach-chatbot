# spacy_training.py
import spacy
import random

nlp = spacy.load("en_core_web_sm")

training_modules = {
    "beginner": {
        "batsman": ["Grip and stance basics", "Front foot defense", "Back foot shots", "Running between wickets"],
        "bowler": ["Grip types", "Bowling action basics", "Line and length drill", "Follow-through"],
        "allrounder": ["Basic fielding", "Fitness drills", "Batting basics", "Bowling accuracy"]
    },
    "intermediate": {
        "batsman": ["Shot selection", "Playing spin", "Power hitting", "Strike rotation"],
        "bowler": ["Swing bowling", "Variation drills", "Death overs", "Pace control"],
        "allrounder": ["Agility training", "Net practice", "Advanced fielding", "Role balancing"]
    },
    "advanced": {
        "batsman": ["Match simulation", "Helicopter shot", "Pressure handling", "Video analysis"],
        "bowler": ["Reverse swing", "Mental focus", "Match strategies", "Data-driven tactics"],
        "allrounder": ["Scenario practice", "Intense fitness", "Tactical drills", "Leadership exercises"]
    }
}

skill_map = {"beginner": "beginner", "new": "beginner", "intermediate": "intermediate", "advanced": "advanced"}
role_map = {"batsman": "batsman", "bowler": "bowler", "allrounder": "allrounder"}

def extract_training_profile(text):
    doc = nlp(text.lower())
    skill_level = None
    role = None
    goal = None

    for token in doc:
        if token.text in skill_map:
            skill_level = skill_map[token.text]
        if token.text in role_map:
            role = role_map[token.text]

    # Try extracting a noun chunk as the goal (if present)
    for chunk in doc.noun_chunks:
        if chunk.root.text not in skill_map and chunk.root.text not in role_map:
            goal = chunk.text.strip()

    return skill_level, role, goal

def generate_training_plan(user_input):
    skill, role, goal = extract_training_profile(user_input)
    if not skill or not role:
        return "Sorry, I couldn't understand your skill level and role. Please say something like 'I'm an advanced batsman.'"

    modules = training_modules[skill][role]
    plan = random.sample(modules, min(4, len(modules)))
    if goal:
        plan.append(f"Goal-specific drill: {goal.title()}")
    return "\n".join([f"{i+1}. {step}" for i, step in enumerate(plan)])
