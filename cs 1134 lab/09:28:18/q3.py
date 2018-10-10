def reverse_vowels(input_str):
  s = [0] * len(input_str)
  index = 0
  new_str = [0] * len(input_str)

  for i in range(len(input_str)):
    new_str[i] = input_str[i]
  for i in range(len(input_str)):
    if(input_str[i] == 'a' or
       input_str[i] == 'e' or
       input_str[i] == 'i' or
       input_str[i] == 'o' or
       input_str[i] == 'u' or
            input_str[i] == 'y'):
      s[index] = i
      index += 1
  # for i in range(index+1):
 # s[i], s[index-i] = s[index-i], s[i]
  print(index)
  print(s)
  count = 0
  for i in range(index // 2):
    new_str[s[i]], new_str[s[index - 1 - i]] = new_str[s[index - 1 - i]], new_str[s[i]]
    print("i", i, "is swapped with", index - 1 - i)
    print(s[i], s[index - 1 - i])
    print(new_str)
  return "".join(new_str)

  # if lst[left] in vowels
  #vowels = "aeiouy"
  # left and right and swap them.
  while(left < right):
    if(lst left not in vowels)
    if(lst right not in vowels)
    elif(left in vowels)
    swap left and right


print(reverse_vowels("mexico"))
