def check_anagram(self,s,t):
  if len(s)!=len(t):
    return False
  s_sorted ,t_sorted = ''.join(sorted(s)),''.join(sorted(t))
  for i in range(len(s)):
    if s_sorted[i]!=t_sorted[i]:
      return False
  return True

if __name__ == "__main__":
  s = "silent"
  t = "listen"
  is_anagram = check_anagram(s,t)
  
