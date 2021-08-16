def is_match(text, pattern):
    return isMatchHelper(text, pattern, 0, 0)


def isMatchHelper(text, pattern, textIndex, patIndex):
    # base cases - one of the indexes reached the end of text or pattern
    if textIndex >= len(text):
        if patIndex >= len(pattern):
            # Both of them reached the end of the end of the text, so it was a match.
            return True
        else:
            # The text index is complete. Check if the pattern index has a next char. If so, it must
            # have an asterisk after it in order it to be valid (since * can be matched 0 times).
            if (patIndex + 1 < len(pattern)) and (pattern[patIndex + 1] == '*'):
                return isMatchHelper(text, pattern, textIndex, patIndex + 2)
            else:
                # The text index is complete, but not the pattern is not. Not a match!
                return False

        # If pattern index finished before text index
    else if (patIndex >= len(pattern)) and (textIndex < len(text)):
        return false
    # string matching for character followed by '*'

else if (patIndex + 1 < len(pattern)) and (pattern[patIndex + 1] == '*'):
    if (pattern[patIndex] == '.') or (text[textIndex] == pattern[patIndex]):
        return (isMatchHelper(text, pattern, textIndex, patIndex + 2) or
                isMatchHelper(text, pattern, textIndex + 1, patIndex))
    else:
        return isMatchHelper(text, pattern, textIndex, patIndex + 2)

if __name__ == '__main__':
    test_text = "acd"
    test_pattern = "ab*c."
    is_match(test_text, test_pattern)