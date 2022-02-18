word = input()
dic = {3: ['A', "B", "C"], 4: ["D", "E", 'F'], 5: ['G', 'H', 'I'], 6: ['J', 'K', 'L'],
       7: ['M', 'N', 'O'], 8: ['P', 'Q', 'R', 'S'], 9: ['T', 'U', 'V'], 10: ['W', 'X', 'Y', 'Z']}
print(sum([key for key, value in dic.items()
      for i in range(len(word)) if word[i] in value]))
