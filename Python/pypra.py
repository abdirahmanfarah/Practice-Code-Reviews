def unistring(str):
    hash = {}
    for i in range(len(str)):
        if str[i] in hash:
            return print("String not Unique")

        else:
            hash[str[i]] = str[i]
            # i += 1
    # for i in hash:
    #     if
    # print(hash)
    return print("String is unique!")


unistring('ba56*,<-]')
