 # Step 1: asking the club members their details.
name=input("what is your name, club member: ")
club=input("what is your club name: ")

#Step 2: members details with different data types. 
member_number = 11
points_earned = 89.65
event_count = 27
meeting_hours = 1.30
is_active = True    

#Step 3: print each detail with thier datatypes.
print("Name:", name, "-> type:", type(name))
print("Club:", club, "-> type:", type(club))
print("Member_number:", member_number, "-> type:", type(member_number))
print("points_earned:", points_earned, "-> type:", type(points_earned))
print("Event_count:", event_count, "-> type:", type(event_count))
print("Meeting_hours:", meeting_hours, "-> type:", type(meeting_hours))
print("Is_active:", is_active, "-> type:", type(is_active))

#Step 4: turn them into string.
member_number_text = str(member_number)
points_text = str(points_earned)
events_text = str(event_count)
meeting_hours_text = str(meeting_hours)
status_text = str(is_active)

print("Member number as text:", member_number_text, "-> type:", type(member_number_text))
print("Points as text:", points_text, "-> type:", type(points_text)) 
print("Events as text:", events_text, "-> type:", type(events_text) )
print("Meeting hours as text:"), meeting_hours, "-> type:", type(meeting_hours)
print("Status as text:", status_text, "-> type:", type(status_text))

#Step 5: slice the name to make a badge.
first_three = name[0:3]
last_letter = name[-1]
badge_code = first_three + last_letter

print("First 3 letters of name:", first_three)
print("Last letter of name:", last_letter)
print("Badge Code:", badge_code)

#Step 6: reversing the club name.
inverted_club_name = club[::-1]
print("Reversed club name:", inverted_club_name)

#Step 7: Joining everything to make a proper badge name.
badge_line_1 = "CLUB MEMBER " + badge_code.upper()
badge_line_2 = "ID: " + member_number_text + " | EVENTS: " + events_text
badge_line_3 = "POINTS: " + points_text + " | ACTIVE: " + status_text
badge_line_4 = "SECRET CLUB CODE: " + inverted_club_name.upper()
 
# PART 8: Print the complete school club badge
print("")
print("===== SCHOOL CLUB MEMBER BADGE =====")
print(badge_line_1)
print(badge_line_2)
print(badge_line_3)
print(badge_line_4)
print("====================================")





