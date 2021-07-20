"""
compress a string "aaabbcddd" -> "a3b2c1d3". only compress the string if doing so saves space
characters can be intersperseed
should be case sensitive
other questions to ask:
    does the string fit in memory
    asky = ascii only
    what do I provide/do if the input is not an ascii letter string? how to handle fasley/null values
"""
def char_count_check(currentChar, charCount):
    compressedString = ""
    compressedString += currentChar + str(charCount) if charCount > 1 else currentChar 
    return compressedString

def compress_a_string(string):
    if string == "" or string is None:
        return string 

    compressedString = ""
    currentChar = None
    charCount = 0

    for character in string:
        if character == currentChar:
            charCount += 1
        else:

            compressedString += char_count_check(currentChar, charCount) if currentChar is not None else ""

            currentChar = character
            charCount = 1

    compressedString += char_count_check(currentChar, charCount)

        # if character in compressedString:
        #     pass
        # else:
        #     count = string.count(character)
        #     if count >= 2:
        #         compressedString = compressedString + character + str(count)
        #     elif count == 1:
        #         compressedString = compressedString + character

    return compressedString if len(compressedString) < len(string) else string
    # if len(compressedString) >= len(string):
    #     return string
    # else:
    #     return compressedString

def test_compress():
    assert compress_a_string(None) == None
    assert compress_a_string("") == ""
    assert compress_a_string("aabbcc") == "aabbcc"
    assert compress_a_string("AAABCCDDDDE") == "A3BC2D4E"
    assert compress_a_string("BAAACCDDDD") == "BA3C2D4"
    assert compress_a_string("AAAbaaCCDDDD") == "A3ba2C2D4"
    assert compress_a_string("AAABCCAADDDDE") == "A3BC2A2D4E"

test_compress()
print(compress_a_string("AAABCCAADDDDE"))