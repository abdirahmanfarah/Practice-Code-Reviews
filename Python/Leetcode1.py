# class Solution:
def createTargetArray(nums, index):
    target = [None] * len(nums)

    for i in range(len(index)):
        for j in range(len(nums)):
            for t in range(len(target)):
                if i == j:
                    x = index[i]
                    if t == x:
                        if target[t] == None:
                            target[t] = nums[j]

                        else:
                            target.insert(t, nums[j])

    for b in range(len(target)):

        if target[b] != None:
            result.append(target[b])
    return result


x = [1, 2, 3, 4, 0]
y = [0, 1, 2, 3, 0]
print(createTargetArray(x, y))


def function flattenDictionary(dict):
    flatDictionary = {}
    flattenDictionaryHelper("", dict, flatDictionary)

    return flatDictionary


function flattenDictionaryHelper(initialKey, dict, flatDictionary):
    for (key: dict.keyset()):
        value = dict.get(key)

        if (!isDictionary(value)):  # the value is of a primitive type
            if (initialKey == null | | initialKey == ""):
                flatDictionary.put(key, value)
            else:
                flatDictionary.put(initialKey + "." + key, value)
        else:
            if (initialKey == null | | initialKey == "")
            flattenDictionaryHelper(key, value, flatDictionary)
            else:
                flattenDictionaryHelper(
                    initialKey + "." + key, value, flatDictionary)
