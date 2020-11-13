def add_time(start, duration, day = "Noday"):

  # convert start time to hours, minutes and time of day
  x = start.split()
  tod = x[1]

  begin_time = x[0].split(":")
  begin_hour = begin_time[0]
  begin_min = begin_time[1]
  
  # convert duration to hours and minutes
  d = duration.split(":")
  hour_added = d[0]
  min_added = d[1]

  # calculate totals in minutes
  begin_total = int(begin_hour) * 60 + int(begin_min)
  duration_total = int(hour_added) * 60 + int(min_added)
  new_total = begin_total + duration_total

  newh = new_total // 60

  # calculate new hour value
  new_hour = newh % 12
  if new_hour == 0:
    new_hour += 12
  
  # calculate new minute value
  new_min = new_total % 60
  if new_min < 10:
    new_min = "0" + str(new_min)

  # check if AM or PM
  new_tod = ""
  y = newh // 12

  if y % 2 == 0:
    new_tod = tod.upper()
  else: 
    if tod.casefold() == "am":
      new_tod = "PM"
    else:
      new_tod = "AM"

  if tod.casefold() == "pm": 
    left_today = 720 - begin_total
  else: 
    left_today = 1440 - begin_total     

  days_lapsed = 0
  if duration_total >= left_today:
    z = duration_total - left_today
    if z % 1440 == 0:
      days_lapsed += z / 1440
    else:
      days_lapsed += z // 1440 + 1    

  # Get the correct day of the week, if required
  if day != "Noday":
    today = day.title()
    dow = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    m = dow.index(today)

    r = m + days_lapsed
    s = r % 7

    if s <= 6:
      new_day = dow[s]
    else:
      s -=6
      new_day = dow[s]

  if days_lapsed == 1:
    day_out = "(next day)"
  else:
    day_out = "(" + str(days_lapsed) + " days later)"    

  if day != "Noday":
    if int(days_lapsed) == 0:
      new_time = str(new_hour) + ":" + str(new_min) + " " + str(new_tod) + ", " + str(new_day)
    else:  
      new_time = str(new_hour) + ":" + str(new_min) + " " + str(new_tod) + ", " + str(new_day) + " " + day_out
  else:
    if int(days_lapsed) == 0:
      new_time = str(new_hour) + ":" + str(new_min) + " " + str(new_tod)
    else:  
      new_time = str(new_hour) + ":" + str(new_min) + " " + str(new_tod) + " " + day_out     


  return new_time