import array
# Creating a new list with value starting from the next element
# if found the value in string, then add it
# if not found and the length is still lower than k than add it again
# otherwise break from cycle
# since we are using at most k means that if k is bigger than length of string
# will return string


# this is costly function, will be refactored
def longest_substr(s, k):
    if k == 0:
        return None
    elif k == 1:
        return s[0]
    else:
        substr_dict = list()
        substr_dict_length = array.array('i', [0 for i in range(len(s))])
        for i in range(len(s)):
            substr = list()
            substr.append(s[i])
            for j in range(i + 1, len(s)):
                if s[j] in substr:
                    substr.append(s[j])
                elif s[j] not in substr and len(substr) < k:
                    substr.append(s[j])
                else:
                    break
            substr_dict.insert(i, substr)
            substr_dict_length[i] = len(substr)

        index = substr_dict_length.index(max(substr_dict_length))
        return ''.join(substr_dict[index])

