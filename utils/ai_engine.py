def ai_response(query):
    q = query.lower()

    if "max" in q or "highest" in q:
        return "The highest value is shown in the dashboard chart."

    elif "city" in q:
        return "Cities like Mumbai and Delhi show highest sales."

    elif "profit" in q:
        return "Profit is highest in Mumbai due to higher sales."

    else:
        return "I can analyze sales, profit, cities, and trends from your data."