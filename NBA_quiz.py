from question import question

print("**THESE ARE RANDOM QUESTIONS TESTING YOU ON PROFFESIONAL BASKETBALL FACTS! THIS PROGRAM WILL KEEP TRACK OF THE ONES YOU GET RIGHT AND WRONG. TRY TO GET A PERFECT SCORE! GOOD LUCK AND ENJOY :)**")

question_prompts = [
	"\n1. What team did Michael Jordan win 6 championships with?\n(a) Los Angeles Lakers\n(b) San Antonio Spurs\n(c) Chicago Bulls\n(d) Utah Jazz\n",
	"\n2. What state was Lebron James born and raised from?\n(a) Ohio\n(b) Illinois\n(c) California\n(d) Georgia\n(e) Oregon\n",
	"\n3. What color is a Basketball?\n(a) Hazel\n(b) Orange\n(c) Brown\n(d) Grey\n(e) White\n",
	"\n4. What team did Kobe Bryant score 81 points against?\n(a) New York Knicks\n(b) Detroit Pistons\n(c) Toronto Raptors\n(d) Indiana Pacers\n(e) Miami Heat\n",
	"\n5. What state do the Pacers in the NBA represent?\n(a) California\n(b) Tennessee\n(c) Indiana\n(d) Florida\n(e) South Carolina\n",
	"\n6. What NBA player won the most championships?\n(a) Larry Bird\n(b) Magic Johnson\n(c) Michael Jordan\n(d) Kobe Bryant\n(e) Bill Russel\n(f) Jerry West\n",
	"\n7. What state do the Thunder in the NBA represent?\n(a) Washington\n(b) New Orleans\n(c) New York\n(d) Oklahoma\n",
	"\n8. Who is the all time leader in assists in the NBA?\n(a) Jason Kidd\n(b) John Stockton\n(c) Allen Iverson\n(d) Magic Johnson\n(e) Karl Malone\n",
	"\n9. What NBA team has the longest win streak record?\n(a) Miami Heat\n(b) Los Angeles Lakers\n(c) Golden State Warriors\n(d) Chicago Bulls\n(e) Los Angeles Clippers\n",
	"\n10. What NBA player has won the most valuable player award or 'MVP' the most?\n(a) Kareem Abdul-Jabbar\n(b) Bill Walton\n(c) Bill Russell\n(d) Wilt Chamberlain\n(e) Michael Jordan\n",
	"\n11. What NBA player has won the most dunk contests to date?\n(a) Vince Carter\n(b) Julius Erving\n(c) Nate Robinson\n(d) Michael Jordan\n(e) Dwight Howard\n",
	"\n12. How many NBA teams are their currently?\n(a) 30\n(b) 27\n(c) 28\n(d) 32\n(e) 35\n",
	"\n13. What NBA player scored the most points in a single game?\n(a) Michael Jordan\n(b) Bill Russel\n(c) Kobe Bryant\n(d) Lebron James\n(e) Wilt Chamberlain\n(f) Kareem Abdul-Jabbar\n",
	"\n14. What NBA player has made the most three pointers in a single game?\n(a) Allen Iverson\n(b) Ray Allen\n(c) Steph Curry\n(d) Klay Thompson\n(e) Larry Bird\n",
	"\n15. What NBA coach has won the most championships?\n(a) Gregg Popovich\n(b) Phil Jackson\n(c) Pat Riley\n(d) Red Auerbach\n(e) John Kundla\n",
	"\n16. What NBA player has the record for most seasons played?\n(a) Kevin Willis\n(b) Kevin Garnett\n(c) Robert Parish\n(d) Dirk Nowitzki\n(e) Vince Carter\n(f) All the above\n",
	"\n17. What NBA player has won the most 6th Man Of The Year award the most?\n(a) Lamar Odom\n(b) Manu Ginobili\n(c) Jamal Crawford\n(d) Lou Williams\n(e) c and d\n",
	"\n18. Who is the all time leader in blocks in the NBA currently?\n(a) Ben Wallace\n(b) Shaquille O'neal\n(c) Hakeem Olajuwon\n(d) Dikembe Mutombo\n(e) David Robinson\n",
	"\n19. What NBA player has the most career points?\n(a) Kobe Bryant\n(b) Michael Jordan\n(c) Lebron James\n(d) Karl Malone\n(e) Kareem Abdul-Jabbar\n",
	"\n20. What NBA player played for the Houston Rockets and scored 13 points in 35 seconds to comeback and beat the San Antonio Spurs?\n(a) Allen Iverson\n(b) Kobe Bryant\n(c) Tracy Mcgrady\n(d) Lebron James\n(e) Kevin Garnett\n",
	"\n21. What two NBA players started a brawl that is well known today as 'Malice at the Palace'?\n(a) Kevin Garnett vs. Kendrick Perkins\n(b) Rasheed Wallace vs. Kobe Bryant\n(c) Josh Smith vs. Andrew Bynum\n(d) Ben Wallace vs. Metta World Peace\n",
	"\n22. In 1997 game 5 of the NBA finals in the chase for his fifth ring what NBA player scored 38 points in what was called the flu game?\n(a) Scottie Pippen\n(b) Michael Jordan\n(c) Karl Malone\n(d) John Stockton\n(e) Jeff Hornacek\n",
	
	
	
	
	 
	
	
	
]

questions = [
	question(question_prompts[0], "c"),
	question(question_prompts[1], "a"),
	question(question_prompts[2], "b"),
	question(question_prompts[3], "c"),
	question(question_prompts[4], "c"),
	question(question_prompts[7], "b"),
	question(question_prompts[8], "b"),
	question(question_prompts[9], "a"),
	question(question_prompts[10], "c"),
	question(question_prompts[11], "a"),
	question(question_prompts[12], "e"),
	question(question_prompts[13], "d"),
	question(question_prompts[14], "b"),
	question(question_prompts[15], "f"),
	question(question_prompts[16], "e"),
	question(question_prompts[17], "c"),
	question(question_prompts[18], "e"),
	question(question_prompts[19], "c"),
	question(question_prompts[20], "d"),
	question(question_prompts[21], "b"),
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
