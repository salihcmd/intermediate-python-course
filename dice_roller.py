def main():
  import random
  dice_roll = 2
  die_sum = 0
  for i in rand (0, dice_roll):
      roll = random.randint(1, 6)
      die_sum += roll
      print(f'You rolled a {roll}')
   print(f"you have rolled a total of {die_sum}")


if __name__== "__main__":
  main()
