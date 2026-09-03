def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))

            if value <= 0:
                print("❌ Please enter a number greater than 0.")
                continue

            return value

        except ValueError:
            print("❌ Please enter a valid number.")


def get_calories():
    while True:
        try:
            calories = int(input("Calories burned: "))

            if calories < 0:
                print("❌ Calories cannot be negative.")
                continue

            return calories

        except ValueError:
            print("❌ Please enter a valid number.")


def collect_activities(days):
    activities = []

    for day in range(1, days + 1):

        print(f"\n---------- Day {day} ----------")

        exercise = input("Exercise: ").strip()

        while not exercise:
            print("❌ Exercise cannot be empty.")
            exercise = input("Exercise: ").strip()

        calories = get_calories()

        activity = {
            "exercise": exercise,
            "calories": calories
        }

        activities.append(activity)

    return activities


def calculate_total(activities):
    total = 0

    for activity in activities:
        total += activity["calories"]

    return total


def calculate_average(activities):
    total = calculate_total(activities)

    return total / len(activities)


def find_most_active_day(activities):
    most_active = activities[0]

    for activity in activities:

        if activity["calories"] > most_active["calories"]:
            most_active = activity

    return most_active


def display_daily_activities(activities):

    print("\n========== DAILY ACTIVITIES ==========")

    for day, activity in enumerate(activities, start=1):

        print(
            f"Day {day}: "
            f"{activity['exercise']} - "
            f"{activity['calories']} calories"
        )


def display_summary(activities):

    total = calculate_total(activities)
    average = calculate_average(activities)
    most_active = find_most_active_day(activities)

    print("\n========== HABIT SUMMARY ==========")

    print(f"Total days       : {len(activities)}")
    print(f"Total calories   : {total}")
    print(f"Average calories : {average:.2f}")

    print("\n---------- Most Active Day ----------")

    print(f"Exercise : {most_active['exercise']}")
    print(f"Calories : {most_active['calories']}")


def main():

    print("🏋️ SMART FITNESS HABIT TRACKER")

    print("\nLet's track your exercise for multiple days.")

    days = get_positive_integer(
        "\nHow many days do you want to track? "
    )

    activities = collect_activities(days)

    display_daily_activities(activities)

    display_summary(activities)

    print("\n=====================================")
    print("       Keep up the great work! 💪")
    print("=====================================")


main()
