import random

# Task 1: Your Mood Today
def mood_today():
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    moods = ["Happy", "Sad", "Energetic", "Calm"]
    
    print("Task 1: Your Mood Today")
    for day in days_of_week:
        mood = random.choice(moods)
        print(f"On {day}, you were feeling {mood.lower()}.")

# Task 2: Your Mood Tracker
def mood_tracker():
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    times_of_day = ["morning", "afternoon", "evening"]
    moods = ["Happy", "Sad", "Energetic", "Calm"]

    print("\nTask 2: Your Mood Tracker")
    for day in days_of_week:
        for time in times_of_day:
            mood = random.choice(moods)
            print(f"On {day} {time}, you were {mood.lower()}.")

# Run the tasks
if __name__ == "__main__":
    mood_today()
    mood_tracker()
