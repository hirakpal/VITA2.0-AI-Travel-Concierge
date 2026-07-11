import re

DESTINATIONS = [
    "Switzerland",
    "Kerala",
    "Goa",
    "Paris",
    "Italy",
    "Spain",
    "Japan",
    "Dubai",
    "Bali",
    "Delhi",
    "Kashmir",
    "Munnar",
]

MONTHS = [
    "January","February","March","April","May","June",
    "July","August","September","October","November","December"
]


def extract_profile(message: str, profile: dict):

    text = message.lower()

    # --------------------
    # Destination
    # --------------------

    for place in DESTINATIONS:

        if place.lower() in text:
            profile["destination"] = place

    # --------------------
    # Budget
    # --------------------

    budget = re.search(r'(\d+)\s*lakh', text)

    if budget:

        value = int(budget.group(1))

        profile["budget"] = f"₹{value:,} Lakh"

    # --------------------
    # Days
    # --------------------

    days = re.search(r'(\d+)\s*day', text)

    if days:

        profile["duration"] = f"{days.group(1)} Days"

    # --------------------
    # Travellers
    # --------------------

    if "wife" in text or "husband" in text:

        profile["travellers"] = "2 Adults"

    elif "family" in text:

        profile["travellers"] = "Family"

    elif "friends" in text:

        profile["travellers"] = "Friends"

    elif "solo" in text:

        profile["travellers"] = "Solo"

    # --------------------
    # Month
    # --------------------

    for month in MONTHS:

        if month.lower() in text:

            profile["travel_month"] = month

    return profile
