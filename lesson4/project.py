team1= 23
team2= 13
team3= 9
team4= 35
team5= 89

total= team1 + team2 + team3 + team4 + team5
average= total/5
print("Total points is", total )
print("average points per team is ", average )

star_per_point= 5
total_stars_earned= total * star_per_point
print("The total stars earned is", total_stars_earned)

full_boxes= total_stars_earned//25
leftovers= total_stars_earned%25
print("Full boxes filled:",full_boxes )
print("Leftover of stars:", leftovers)

last_weeks=150
print("Is the equal to last weeks? ", total==last_weeks)
print("Better than last weeks? ", total>last_weeks)
print("Is it atleast better?", total>=last_weeks)

total += 25
print("Points after the bonus:", total)
total -= 20
print("Point after missed task:", total)

reward_stars = total * star_per_point
boxes = reward_stars // 25
 
print("Final boxes packed :", boxes)