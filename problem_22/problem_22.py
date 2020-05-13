def original_sentence(dictionary, string):
    return generate_list(dictionary, string, len(string), [])


def generate_list(dictionary, string, length, results):
    for i in range(length + 1):
        prefix = string[0:i]
        if dictionary_contains(dictionary, prefix):
            if i == length:
                results.append(prefix)
                # should be checked for returning the values of every scenario
                print(results)
            results.append(prefix)
            generate_list(dictionary, string[i:length], length-i, results)


def dictionary_contains(dictionary, string):
    for value in range(len(dictionary)):
        if dictionary[value] == string:
            return True

    return False
