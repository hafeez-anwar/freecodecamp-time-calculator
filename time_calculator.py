#********DESCRIPTION******#
#  ------   BY ------------
#    Dr. Hafeez Anwar
#    Date: 22-06-2022
#---------------------------

# Following are the steps of the solution
# 1. START TIME is parsed into START_HOURS, START_MINUTES and START_MERIDIEM
# 2. TIME_TO_ADD is parsed into HOURS_TO_ADD and MINUTES_TO_ADD
# 3. Both the START_MINUTES and MINUTES_TO_ADD are added. The sum is then checked if it exceeds 60. If that is TRUE, then an hour is added to HOURS_TO_ADD, and the remaing minutes are stored in the RES_MINUTES which are the resultant minutes
# 4. The START_HOURS and HOURS_TO_ADD are then added to get RES_HOURS.
# 5. If RES_HOURS is less than 12, that means, both the MERIDIEM and DAY remains UNCHANGED, and we get the solution. Just one last inspection is done, it the DAY is required in the call to the function, if that is the case, DAY is also returned, otherwise, RES_MINUTES, RES_HOURS and START_MERIDIEM are returned.
# 6. If RES_HOURS is greater than 12, we need to do the following two things.
#     a. How many times RES_HOURS is greater than 12. In other words, how many   
#        meridiems are passed since the start time? For this, we divide RES_HOURS 
#        by 12 to know the FACTOR by which RES_HOURS is greater than 12.
#     b. We need to round the time to the 12-hours format as well. For this, we  
#        perform the remainder operation and this is the resultant RES_HOURS.
#7. Now, with the help of the FACTOR, we will calculate the RESULTANT MERIDIEM, NEXT DAY or NUMBER OF DAYS. The solution is based on 12-hours meridium. Following are the rules
#     a. If the FACTOR is ODD. 
#        i. If it is ONE? means, the current meridiem changes to the next meridiem #           AM Changes to PM with no change in the day, However, PM changes to AM #           with an increment to the NEXT DAY. Returning 0 from the function  
#           MERIDIEM_CALCULATE means no change in the DAY, and returning 1 means 
#           NEXT DAY
#       ii. If greater than ONE? means more than one meridiem have passed, but 
#           their number is ODD e.g. 3, 5, 7, etc. In this case, FACTOR/2 gives
#           number of DAYS, as there are TWO meridiems in a day. If the current # #           meridiem is AM, MERIDIEM_CALCULATE returns PM and NUM_DAYS. If the   
#           current meridiem is PM, MERIDIEM_CALCULATE returns AM and NUM_DAYS+1, #           as the it goes to the next day.
#     a. If the FACTOR is EVEN. MERIDIEM remains unchanged
#        i. If it is TWO? same time next day. 
#           MERIDIEM_CALCULATE returns MERIDEIM and 1 which means NEXT DAY. 
#       ii. If greater than TWO? means more than two meridiems have passed, but 
#           their number is EVEN e.g. 4, 6, 8, etc. In this case, FACTOR/2 gives
#           number of DAYS. MERIDIEM_CALCULATE returns MERIDIEM and NUM_DAYS. 

def meridiem_calculate(factor,meridiem):
  if factor%2!=0:
    if factor==1:
      if meridiem=='AM':
        return 'PM', 0
      else:
        return 'AM', 1
    else:
      num_days = int(factor/2)
      if meridiem=='AM':
        return 'PM', num_days
      else:
        return 'AM', num_days+1

  elif factor%2==0:
    if(factor==2):
      return meridiem, 1
    else:
      num_days = int(factor/2)
      return meridiem, num_days

def add_time(start, duration,day = ''):

  # -------------------------
  #     PARSE START TIME
  # -------------------------
  start = start.split()
  # start hours
  start_hours   = int(start[0].split(':')[0])
  # start minutes
  start_minutes = int(start[0].split(':')[1])
  # start meridiem
  meridiem =start[1]

  # -------------------------
  #   PARSE THE TIME TO ADD
  # -------------------------
  # getting hours to add
  hours_to_add = int(duration.split(':')[0])
  # getting minutes to add
  minutes_to_add = int(duration.split(':')[1])

  # -------------------------
  # To return the week day if 
  #   required in the input
  # -------------------------
  # List of week days
  week_days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"
                ,"Sunday"]
  # capitalize the day that is input by the user, just in case, the case of letters
  # are not compatible
  day = day.capitalize()

  # -----------------------------
  # GETTING the resultant minutes 
  # after adding the start and 
  #       to_add minutes
  # -----------------------------
  # add both the minutes
  res_minutes = start_minutes + minutes_to_add
  # Check if the res_minutes are greater than 60
  if res_minutes>=60:
    # add, one hour to the hours_to_add
    hours_to_add += 1
    # calculate resultant minutes
    res_minutes = res_minutes-60
  # append a zero with the UNIT ONLY minutes 0, 1, 2, ... 9
  if res_minutes<10:
    res_minutes = '0'+str(res_minutes)
  else:
    res_minutes = str(res_minutes)

  # -----------------------------
  # GETTING the resultant hours 
  # after adding the start and 
  #          to_add hours
  # -----------------------------
  res_hours = start_hours+hours_to_add

  # If we stay in the same meridiem and day
  if res_hours<12:
    # if day is asked, append it to the returning time
    if day in week_days:
      return str(res_hours)+':'+res_minutes+' '+meridiem+','+' '+day
    else:
      return str(res_hours)+':'+res_minutes+' '+meridiem

  # If do not stay in the same meridiem, then, we will have to calculate the 
  # resultant meridiem and day (SAME DAY, NEXT DAY, NUMBER OF DAYS)
  elif res_hours>=12:
    # How many meridiems are passed? divide the res_hours by 12
    fact = int(res_hours/12)
    # What will be the resultant time in 12-hours format?
    res_hours = res_hours%12
    # If the res_hours is 0, make it 12
    if(res_hours==0):
      res_hours = 12
    
    meridiem, day_info = meridiem_calculate(fact,meridiem)
    # If day_info is ZERO: Day remains unchanged
    # If day_info is 1: DAY goes to NEXT DAY
    # If day_info is more than 1: DAY goes to NUMBER_DAYS Later
    if day in week_days:
      if day_info==0:
        return str(res_hours)+':'+res_minutes+' '+meridiem+' ' + day
      elif day_info==1:
        day_index = week_days.index(day)
        day = week_days[day_index+1]
        return str(res_hours)+':'+res_minutes+' '+meridiem+', ' + day +' '+'(next day)'
      else:
          day_index = week_days.index(day)
          day = week_days[(day_index+day_info)%7]
          return str(res_hours)+':'+res_minutes+' '+meridiem+', '+day+" ("+str(day_info)+" days later)"

    else:
      if day_info==0:
        return str(res_hours)+':'+res_minutes+' '+meridiem
      elif day_info==1:
          return str(res_hours)+':'+res_minutes+' '+meridiem+' '+'(next day)'
      else:
          return str(res_hours)+':'+res_minutes+' '+meridiem+' '+"("+str(day_info)+" days later)"
