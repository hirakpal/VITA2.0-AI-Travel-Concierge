from datetime import datetime

REQUIRED_FIELDS = [
    "destination",
    "budget",
    "duration",
    "travellers",
    "travel_month",
    "travel_style"
]


def log(message):

    return f"{datetime.now().strftime('%H:%M:%S')} {message}"


def get_next_question(profile):

    if not profile["destination"]:
        return (
            "📍 Where would you like to travel?",
            "⚠ Destination missing"
        )

    if not profile["budget"]:
        return (
            "💰 What's your approximate budget for this trip?",
            "⚠ Budget missing"
        )

    if not profile["duration"]:
        return (
            "📅 How many days are you planning to travel?",
            "⚠ Duration missing"
        )

    if not profile["travellers"]:
        return (
            "👥 Who will be travelling with you?",
            "⚠ Traveller information missing"
        )

    if not profile["travel_month"]:
        return (
            "🗓 Which month are you planning to travel?",
            "⚠ Travel month missing"
        )

    if not profile["travel_style"]:
        return (
            """🎯 What kind of trip are you looking for?

Choose one or more:

• Luxury
• Adventure
• Nature
• Relaxation
• Family
• Honeymoon
• Food
• Culture""",
            "⚠ Travel style missing"
        )

    return (
        """🎉 Perfect!

I now understand your travel requirements.

The next step is to build personalized recommendations for your trip.""",
        "✅ Traveller Profile Complete"
    )
