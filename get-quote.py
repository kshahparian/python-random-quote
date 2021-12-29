import random
def main():
  #print("Keep it logically awesome. kourosh.s")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = 13
  rnd = random.randint(0, last)
  print(quotes[rnd])

if __name__== "__main__":
  main()
