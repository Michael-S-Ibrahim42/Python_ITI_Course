import sys

def foo(grade):
  grade = int(grade)
  if grade > 25:
    result = "pass"
  else:
    result = "fail"
  print(result)
  
if __name__ == '__main__':
  foo(sys.argv[1])