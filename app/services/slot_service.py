from datetime import datetime, timedelta

def generate_slots(start_hour=9, end_hour=17, slot_minutes=30):
    slots = []

    current = datetime.strptime(f"{start_hour}:00", "%H:%M")
    end = datetime.strptime(f"{end_hour}:00", "%H:%M")

    while current < end:
        slots.append(current.strftime("%H:%M"))
        current += timedelta(minutes=slot_minutes)

    return slots