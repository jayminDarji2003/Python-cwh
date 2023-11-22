# Desktop notification applicaiton. Drink Water Reminder.
# NOTE : Windows only

from plyer import notification
import time
import pyttsx3


def show_notification():
    title = "Reminder"
    message = "Hey Jaymin, drink water!"

    # Display notification
    notification.notify(
        title=title,
        message=message,
        timeout=2,  # Notification will be visible for 10 seconds
    )

    # Speak the message
    speak_message(message)


def speak_message(message):
    engine = pyttsx3.init()
    engine.say(message)
    engine.runAndWait()


interval_minutes = 60  # Set the interval in minutes
while True:
    show_notification()
    time.sleep(interval_minutes * 60)  # Convert minutes to seconds
