def groupAnagrams(strs):
    unique = []
    result = []
    uniqueCounter = 0
    for i in strs:
        wordList = list(i)
        wordList.sort()
        word = ''.join(wordList)
        if word not in unique:
            unique.append(word)
            result.append([])
            result[uniqueCounter].append(i)
            uniqueCounter += 1
        else:
            result[unique.index(word)].append(i)
    return result


if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = groupAnagrams(strs)
    print(result)
