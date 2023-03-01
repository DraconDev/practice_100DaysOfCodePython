a1 = ["live", "arp", "strong"]
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]


def in_array(array1, array2):
    result = []
    for v in array1:
        for v2 in array2:
            if v in v2 and v not in result:
                result.append(v)
    result.sort()
    return result


test = in_array(a1, a2)
# test = ['c', 'b', 'a'].sort()

print(test)
