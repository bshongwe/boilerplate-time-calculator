import datetime

def add_time(start_time, duration, start_day_of_week=None):
  """Adds the duration time to the start time and returns the result.

  Args:
    start_time: A string representing the start time in the 12-hour clock format,
      ending in AM or PM.
    duration: A string representing the duration time in the format "HH:MM",
      where HH is the number of hours and MM is the number of minutes.
    start_day_of_week: An optional string representing the starting day of the week,
      case insensitive.

  Returns:
    A string representing the end time, following the rules specified in the
    question.
  """

  # Parse the start time and duration time.
  start_time = datetime.datetime.strptime(start_time, "%I:%M %p")
  duration = datetime.timedelta(hours=int(duration[:2]), minutes=int(duration[3:]))

  # Calculate the end time.
  end_time = start_time + duration

  # If the end time is the next day, add "(next day)" to the output.
  if end_time.day != start_time.day:
    end_time_str = end_time.strftime("%I:%M %p (next day)")
  else:
    end_time_str = end_time.strftime("%I:%M %p")

  # If the optional start day of the week parameter is given, add the day of the
  # week to the output.
  if start_day_of_week is not None:
    start_day_of_week = start_day_of_week.lower()
    weekdays = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday",
                "sunday"]
    end_time_str += f", {weekdays[end_time.weekday()]} "

  # If the end time is more than one day later, add "(n days later)" to the output.
  if end_time.day - start_time.day > 1:
    end_time_str += f"({end_time.day - start_time.day} days later)"

  return end_time_str
