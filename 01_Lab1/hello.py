# import modules used here -- sys is a very standard one
import sys

# Gather our code in a main() fn
def main():
  print("Hello there", sys.argv[1])

# Standard boilerplate to call the main() fn to begin
if __name__ == "__main__":
  main()