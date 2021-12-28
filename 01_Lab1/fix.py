def fix_start(s,filler):

  s = s[0] + s[1:].replace(s[0], filler)
    # try:
      # if s.find(ch, s.index(ch)+1, len(s)) != -1 :
        # s = s[:s.index(ch)+1] + s[s.index(ch)+1:].replace(ch, filler)
    # except:
      # None
  print(s)
  
if __name__ == "__main__" :
  fix_start("MiMm", '!')