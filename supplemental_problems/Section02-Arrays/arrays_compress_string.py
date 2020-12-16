def compress_string(string):
    count = 1
    compressed_result = ''
    for i in range(1,len(string)):
        if string[i] == string[i-1]:
            count += 1
        else:
            compressed_result += string[i-1] + str(count)
            count = 1
    return compressed_result

print(compress_string('AAABBBaaaeeggyyUUU'))