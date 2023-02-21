
def add_time(start, duration):
  
  new_time = ''
  
  time =  start.split(' ')
  hours = time[0].split(':')[0]
  minutes = time[0].split(':')[1]
  am_pm = time[1]

  duration_hours = duration.split(':')[0]
  duration_minutes = duration.split(':')[1]
      
  sum_hours = ''
  sum_minutes = ''
  #Calculate the hours in 24-hour format 
  hours24 = ''
  if am_pm == 'PM':
    hours24 = str(int(hours) + 12)
  else:
    hours24 = hours

  
  #Adding minutes and calculating extra hours (if needed)
  extraDays = 0 
  extraHours = 0
  
  if int(minutes) + int(duration_minutes) >= 60:
    extraHours += 1
    sum_minutes = str(int(minutes) + int(duration_minutes) - 60)
  else:
    sum_minutes = str(int(minutes) + int(duration_minutes))
    
  #Adding hours and calculating extra days 
  hour_counter = 0
  total_hours = int(hours24) + int(duration_hours) + int(extraHours)
  if total_hours >= 24:
    while total_hours%24 != 0:
      hour_counter += 1
      total_hours = total_hours - 1
    extraDays = (total_hours/24)
    sum_hours = str(hour_counter)
  else:
    sum_hours = str(total_hours)

  #Turning the 24-hour formatted sum into 12 hour format 
  timeOfDay = ''
  hours12 = ''
  
  if int(sum_hours) > 12:
    hours12 = str(int(sum_hours)-12)
    timeOfDay = 'PM'
  else:
    print(sum_hours)
    hours12 = sum_hours
    timeOfDay = 'AM'

  #Formatting the new time in a string 

  new_time = hours12 + ':' + sum_minutes.zfill(2) + ' ' + timeOfDay 

  #Formatting the extra days on the new_time string
  if extraDays == 0:
    new_time = new_time
  elif extraDays == 1:
    new_time = new_time + ' (next day)'
  else:
    new_time = new_time + ' (' + str(int(extraDays)) + ' days later)'
  print(new_time)
  return new_time


#TESTING
add_time('3:00 PM', '3:10')