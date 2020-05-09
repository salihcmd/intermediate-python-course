def main():
  import random
  dice_roll =int(input("how many dice would you like to roll? '"))
  dice_size =int(input("how many sides are the dice? '"))
  die_sum = 0
  for i in rand (0, dice_roll):
      roll = random.randint(1, dice_size)
      die_sum += roll
      if roll == 1:
          print(f"you rolled a {roll}! ,critical fail ! ")
      elif roll == dice_size:
          print(f"you rolled a {roll}! ,critical success !")
      else:
          print(f'You rolled a {roll}')
   print(f"you have rolled a total of {die_sum}")


if __name__== "__main__":
  main()
