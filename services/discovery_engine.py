# services/discovery_engine.py

from services.profile_extractor import extract_profile

DISCOVERY_FLOW = [
    {
        "state": "destination",
        "field": "destination",
        "question": "📍 Where would you like to travel?",
        "placeholder": "Example: Switzerland, Kerala, Japan"
    },
    {
        "state": "travellers",
        "field": "travellers",
        "question": "👥 Who is travelling?",
        "placeholder": "Solo, Couple, Family, Friends"
    },
    {
        "state": "duration",
        "field": "duration",
        "question": "⏳ How many days are you planning?",
        "placeholder": "Example: 7 Days"
    },
    {
        "state": "travel_month",
        "field": "travel_month",
        "question": "📅 Which month are you planning to travel?",
        "placeholder": "Example: December"
    },
    {
        "state": "budget",
        "field": "budget",
        "question": "💰 What's your approximate budget?",
        "placeholder": "Example: 2 lakh"
    },
    {
        "state": "travel_style",
        "field": "travel_style",
        "question": "🎯 What type of trip are you looking for?",
        "placeholder": "Luxury, Adventure, Nature..."
    }
]


class DiscoveryEngine:

    def __init__(self, session):

        self.session = session
        self.profile = session.profile

    def current_step(self):

        for index, step in enumerate(DISCOVERY_FLOW):

            if not self.profile[step["field"]]:
                return index, step

        return None, None

    def current_question(self):

        index, step = self.current_step()

        if step is None:

            return {
                "completed": True,
                "question": "🎉 Traveller Discovery Completed",
                "placeholder": ""
            }

        return {
            "completed": False,
            "step": index + 1,
            "total": len(DISCOVERY_FLOW),
            "question": step["question"],
            "placeholder": step["placeholder"]
        }

    def process_answer(self, answer):

        self.profile = extract_profile(
            answer,
            self.profile
        )

        self.session.profile = self.profile

        return self.current_question()
