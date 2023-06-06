  # libraries
    # from getpass import getpass as input
    
    # Intro and names input
print("Let's play Rock, paper, scissors!")
p1 = input("Player 1 name: ")
p2 = input("Player 2 name: ")
  
rounds_limit = int(input("How many rounds you want to play? "))
score_p1 = 0
score_p2 = 0
round = 0
while round < rounds_limit:
  round = round + 1
  print()
  print("Round:",round)
  print()
  # Player 1 turn  
  def match():
      print()
      print(p1,"it's your turn!")
      print()
      print("Press 'r' for Rock, 'p' for paper and 's' for scissors")
      print()
    
  match()
  p1e = input()
  p1e_len = len(p1e)
  if p1e_len == 1 and (p1e == 'r' or p1e == 'p' or p1e == 's' or p1e == 'R' or p1e == 'S' or p1e == 'P'):
    
    # Assigning emoticons for Player 1
    if p1e == "s" or p1e == "S":
      p1e = "✂️"   
    elif p1e == "p" or p1e == "P":
      p1e = "🧻"
    elif p1e == "r" or p1e == "R":
      p1e = "🗿"
      print()
      print("It's your turn",p2,"!")
      print()
  else:
    print("Press only one of these keys: 'r', 'p' or 's'")
  
  # Player 2 turn
  p2e = input()
  p2e_len = len(p2e)
  if p2e_len == 1 and (p2e == 'r' or p2e == 'p' or p2e == 's' or p2e == 'R' or p2e == 'S' or p2e == 'P'):
    
    # Defining functions    
    def m():
      print()
      print(p1,p1e,"Vs.",p2,p2e)
      print()
    def p1w():
      print()
      print(p1,"wins!🏆")
      print()
    def p2w():
      print()
      print(p2,"wins!🏆")
      print()
      print()
      
    # Assigning emoticons for Player 2
    s = "✂️"
    p = "🧻"
    r = "🗿"
    if p2e == "s" or p2e == "S":
      p2e = "✂️"   
    elif p2e == "p" or p2e == "P":
      p2e = "🧻"
    elif p2e == "r" or p2e == "R":
      p2e = "🗿"
    else:
      print("Error assigning emoticons!")
  
    # Match
    if p1e == p2e:
      m()
      print()
      print("Tied!🙄")
      print()
    elif p1e == p and p2e == s:
      m()
      p2w()
    elif p1e == p and p2e == r:
      m()
      p1w()
    elif p1e == r and p2e == p:
      m()
      p2w()
    elif p1e == r and p2e == s:
      m()
      p1w()
    elif p1e == s and p2e == p:
      m()
      p1w()
    elif p1e == s and p2e == r:
      m()
      p2w()
    else:
      print("Error in match!")
  else:
    print("Press only one of these keys: 'r', 'p' or 's'")

  