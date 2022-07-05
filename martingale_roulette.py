import random
import matplotlib.pyplot as plt

def game(money, initial_bet=1, num_games=100):
  history = [money,]
  bet = initial_bet
  n=0

  while money > bet and n <= num_games:
    number = random.randint(0,37)
    if number % 2 ==1 and number != 0:
      money += bet
      bet = initial_bet
      history.append(money)
    else:
      money -= bet
      bet *= 2
      history.append(money)
    n += 1

  return history

for i in range(10):
  game_result = game(money=10000,num_games=2000)
  plt.figure(figsize=(17,9))
  plt.axhline(y = 10000, color = 'r', linestyle = '-')
  plt.plot(game_result)
  plt.show()