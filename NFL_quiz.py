from question import question

print("**THESE ARE QUESTIONS TESTING YOU ON RANDOM FACTS ABOUT THE NATIONAL FOOTBALL LEAGUE! THIS PROGRAM WILL KEEP TRACK OF THE ONES YOU GET RIGHT AND WRONG. TRY TO GET A PERFECT SCORE! GOOD LUCK AND ENJOY :)**")

question_prompts = [
	"\n1. How many teams are there currently in the NFL?\n(a) 27\n(b) 28\n(c) 30\n(d) 32\n",
	"\n2. What NFL team won the very first superbowl?\n(a) Dallas Cowboys\n(b) New England Patriots\n(c) Green Bay Packers\n(d) San Francisco 49ers\n",
	"\n3. What NFL team has won the most superbowls in franchise history?\n(a) New York Giants\n(b) Pittsburg Steelers\n(c) Dallas Cowboys\n(d) New England Patriots\n(e) b and d\n",
	"\n4. What Running Back in the NFL is the all-time leading rusher currently?\n(a) Walter Payton\n(b) Jim Brown\n(c) Tony Dorsett\n(d) Adrian Peterson\n(e) Emmitt Smith\n",
	"\n5. What Wide Reciever in the NFL is the all-time leader in total yards?\n(a) Jerry Rice\n(b) Randy Moss\n(c) Terrell Owens\n(d) Larry Fitzgerald Jr\n(e) Michael Irving\n",
	"\n6. What coach has won the most regular season games in NFL history?\n(a) George Halas\n(b) Don Shula\n(c) Bill Belichick\n(d) Tom Landry\n",
	"\n7. What player in the NFL is the all-time leader in total tackles?\n(a) Derrick Brooks\n(b) London Fletcher\n(c) Ray Lewis\n(d) Ronde Barber\n(e) Charles Woodson\n",
	"\n8. What NFL player has the most receptions all-time currently?\n(a) Tony Gonzalez\n(b) Larry Fitzgerald\n(c) Cris Carter\n(d) Jerry Rice\n(e) Marvin Harrison\n",
	"\n9. What NFL player is the all-time leader in most Kick Returns?\n(a) Josh Cribbs\n(b) Gale Sayers\n(c) Leon Washington\n(d) a and c\n(e) Cordarrelle Patterson\n",
	"\n10. What NFL player is the all-time leader in most Punt Returns all-time?\n(a) Brian Mitchell\n(b) Darren Sproles\n(c) Tim Brown\n(d) Devin Hester\n(e) Antwaan Randle El\n",
	"\n11. What NFL Quarter Back is the all-time leader in passing yards?\n(a) Drew Brees\n(b) Dan Marino\n(c) Tom Brady\n(d) Peyton Manning\n(e) Brett Favre\n",
	"\n12. What NFL player holds the record for most defensive touchdowns?\n(a) Deion Sanders\n(b) Darren Sharper\n(c) Charles Woodson\n(d) Rod Woodson\n(e) b,c,and d\n",
	"\n13. What NFL player has the most interceptions currently in their career?\n(a) Rod Woodson\n(b) Ed Reed\n(c) Champ Bailey\n(d) Paul Krause\n(e) Emlen Tunnell\n",
	"\n14. What NFL Quarterback has the most career interceptions thrown?\n(a) Peyton Manning\n(b) George Blanda\n(c) Brett Favre\n(d) Vinny Testaverde\n(e) Dan Marino\n",
	"\n15. What NFL Running Back has the record for most yards in a single season?\n(a) Adrian Peterson\n(b) Eric Dickerson\n(c) Emmitt Smith\n(d) Walter Payton\n(e) Jim Brown\n",
	"\n16. What NFL Quarterback has the most rushing yards in a career currently?\n(a) Randall Cunningham\n(b) Michael Vick\n(c) Donovan McNabb\n(d) Steve Young\n(e) Cam Newton\n",
	"\n17. What NFL player has the most touchdowns in their career?\n(a) LaDainian Tomlinson\n(b) Randy Moss\n(c) Jerry Rice\n(d) Terrell Owens\n(e) Marshall Faulk\n",
	"\n18. What NFL player has the most points in NFL history?\n(a) Sebastian Janikowski\n(b) Adam Vinatieri\n(c) Morten Anderson\n(d) Gary Anderson\n(e) Jason Hanson\n",
	"\n19. What NFL Running Back played for the Seattle Seahawks and broke 8 tackles to beat the New Orleans Saints in 2011 playoffs?\n(a) Adrian Peterson\n(b) Marshawn Lynch\n(c) Stephen Jackson\n(d) Chris Johnson\n(e) Jamaal Charles\n",
	"\n20. What year did Quarterback Peyton Manning win his first superbowl?\n(a) 2003\n(b) 2010\n(c) 2006\n(d) 2005\n(e) 2008\n",
	
	
	
	
	
	
	
	
]

questions = [
	question(question_prompts[0], "d"),
	question(question_prompts[1], "c"),
	question(question_prompts[2], "e"),
	question(question_prompts[3], "e"),
	question(question_prompts[4], "a"),
	question(question_prompts[5], "b"),
	question(question_prompts[6], "c"),
	question(question_prompts[7], "d"),
	question(question_prompts[8], "d"),
	question(question_prompts[9], "a"),
	question(question_prompts[10], "a"),
	question(question_prompts[11], "e"),
	question(question_prompts[12], "d"),
	question(question_prompts[13], "c"),
	question(question_prompts[14], "b"),
	question(question_prompts[15], "b"),
	question(question_prompts[16], "c"),
	question(question_prompts[17], "b"),
	question(question_prompts[18], "b"),
	question(question_prompts[19], "c"),
	
	
	
]

def run_test(questions):
	score = 0
	for question in questions:
		answer = input(question.prompt)
		if answer == question.answer:
			score += 1
	print("You got " + str(score) + "/" + str(len(questions)) + " correct")
	
run_test(questions)
		
# Using a class to immulate a real world test or quiz.
