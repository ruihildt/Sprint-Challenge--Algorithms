'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word, count = 0):
    if len(word) < 2:
        return count

    if word[0] + word[1] == str('th'):
        count += 1

    word = word[1:]

    return count_th(word, count)