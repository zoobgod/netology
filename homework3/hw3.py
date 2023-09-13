#task1
id = {
    'user' : [213, 213, 213, 15, 213],
    'user2' : [54, 54, 119, 119, 119],
    'user3' : [213, 98, 98, 35]
    }
allValues = []
filteredValues = []

for values in id:
    allValues += id[values]

for i in range(len(allValues)):
    if allValues[i] not in filteredValues:
        filteredValues.append(allValues[i])
    else:
        continue

print(filteredValues)
    
#task2 
queries = [
    'watch anime online',
    'watch anime',
    'watch anime free',
    'watch adult anime',
    'watch adult anime',
    'watch adult anime',
    'watch bonsai',
    'watch movies'
]
for i in range(len(queries)):
    queries[i] = queries[i].split(' ')
    
two_word_queries = 0
three_word_queries = 0
total_queries = 0
for i in queries:
    if len(i) == 2:
        two_word_queries += 1
        total_queries += 1
        
    elif len(i) == 3:
        three_word_queries +=1
        total_queries += 1


print(two_word_queries)
print(three_word_queries)
print(total_queries)

percent_two = (two_word_queries / total_queries *100)
print(f"Поисковых запросов, содержащих 2 слов(а): {percent_two}")
percent_three = (three_word_queries / total_queries *100)
print(f"Поисковых запросов, содержащих 3 слов(а): {percent_three}")


