import sys
#defines a "repeat" function that takes 2 arguments
def repeat(s, exclaim):
  """
  Returns the string 's' repeated 3 times
  """
  
  result = s * 3
  if exclaim:
    result = result + '!!!'
  return(result)

def main():
  print(repeat('Yay', False))
  print(repeat('Woo Hoo', True))
  
if __name__ == '__main__':
  main()