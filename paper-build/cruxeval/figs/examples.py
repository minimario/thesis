
##################################################
# There are also a few that are not particularly hard but fails consistently on all of (gpt35 and gpt4 and their COT) while passing on the other models

# 1169,48,2	steps: 28.0
def f(text, suffix):
    if text.endswith(suffix):
        return text[0:len(text) - len(suffix)]
    return text
assert f('vasokanam', 'an') == 'vasokanam'

# 1937,37,1	steps: 31.0
def f(num):
    if 0 < num < 1000 and num != 6174:
        return 'Half Life'
    return 'Not found'
assert f(6173) == 'Not found'

# 528,38,0	steps: 37.0
def f(text):
    while len(text) > 0 and text[0] in '0123456789':
        text = text.lstrip('0123456789')
    return text.lstrip('+- i0v')
assert f('i0v0120452v4') == '120452v4'


# Code Llama fails on some simple ones that are completely fixed by GPT3.5

# 1864,20,3	steps: 27.0
def f(text):
    return text.lower().replace('s', 'n')
assert f("snugy") == 'nnugy'

# 768,4,4	steps: 30.0
def f(s):
    return ''.join(map(str.capitalize, s.split()))
assert f('fUn ll Al eng') == 'FunLlAlEng'

# 1302,25,4	steps: 24.0
def f(text):
    return text.strip('x')
assert f("xax16503xax x ax42510ax") == 'ax16503xax x ax42510a'
# also 0 on llama cot


##################################################
# some output examples where all models fail (sorted by number of steps)

# 68,22,1	steps: 25.0
def f(s, n):
    return s.expandtabs(n)
assert f('\tbaky\t bifiw\t mombade\t kibigi\t', 5) == '     baky  bifiw     mombade   kibigi   '

# 1345,27,0	steps: 30.0
def f(letters):
    return ' '.join(letters).replace('', '')
assert f(['ao', 'b', 'u', 'r', 'r', 'e', '', '', '', '', 'e']) == 'ao b u r r e     e'

# 193,34,1	steps: 31.0
def f(t):
    return t.replace('or', t.center(len(t), 'o'))
assert f("pomodoro") == 'pomodpomodoroo'

# 979,28,0	steps: 34.0
def f(text, a, b):
    text = text.replace(a, b)
    return text.replace(b, a)
assert f(' vup a zwwo oihee amuwuuw! ', 'a', 'u') == ' vap a zwwo oihee amawaaw! '

##################################################
# input examples where all models fail
# 910,32,3	steps: 35.0
def f(list, separator):
    text = separator.join(list)
    return separator.join(reversed(text))
assert f(['is', 'it', 'top'], '@') == 'p@o@t@@@t@i@@@s@i'

# 1806,39,3	steps: 37.0
def f(string, sep):
    cnt = string.count(sep)
    return((string+sep) * cnt)[::-1]
assert f('caabcfcabfc', 'ab') == 'bacfbacfcbaacbacfbacfcbaac'


##################################################
# The highest step ones where all models fail are still mostly reasonable ones

# swaps cases of every other letter
# 474,9,0	steps: 862.0
def f(line):
    count = 0
    a = []
    for i in range(len(line)):
        count += 1
        if count%2==0:
            a.append(line[i].swapcase())
        else:
            a.append(line[i])
    return ''.join(a)
assert f("987yhNSHAshd 93275yrgSgbgSshfbsfB") == '987YhnShAShD 93275yRgsgBgssHfBsFB'

# 1727,18,4	steps: 550.0
def f(text):
    pairs = []
    for i in range(1, len(text)):
        if text[i-1:i+1].isalnum() and not text[i:i+2].isalnum():
            pairs.append(text[i-1:i+1])
    result = []
    for p in pairs: result.append(' '.join(p))
    return ' '.join(result)
assert f('qmpts i,rpercentwrong') == 't s'

# 8,0,4	steps: 508.0
def f(lst):
    messages = []
    for el in lst:
        message = ''
        for char in el:
            message += (char.upper() if char.isalpha() else '_')
        messages.append(message)
    return messages
assert f(["Talk@5g", "@#%#", "", "", "Hello", "--- =-__ws"]) == ['TALK__G', '____', '', '', 'HELLO', '________WS']

##################################################
# The one with an outlier number of steps still happens to be reasonable 
# 543,15,2	steps: 3175.0
def f(ints):
    counts = [0] * 301

    for i in ints:
        counts[i] += 1

    r = []
    for i in range(len(counts)):
        if counts[i] >= 3:
            r.append(str(i))
    counts.clear()
    return ' '.join(r)
assert f([2, 3, 5, 2, 4, 5, 2, 89]) == '2'


# The only 7 examples where all models fail on both input and output
# Most are still reasonable, except perhaps 845,6,3 and 1171,31,2 

# 1806,39,3	steps: 37.0
def f(string, sep):
    cnt = string.count(sep)
    return((string+sep) * cnt)[::-1]
assert f('caabcfcabfc', 'ab') == 'bacfbacfcbaacbacfbacfcbaac'

# 1870,2,3	steps: 42.0
def f(text, char):
    head, sep, tail = text.rpartition(char)
    return head + tail[::-1] + sep + head
assert f('pylbtncuetx', 'y') == 'pxteucntblyp'

# 655,10,4	steps: 46.0
def f(s):
    s = s.ljust(len(s) * 3, '~')
    return '{}+++{}'.format(s[::2], s[1::2])
assert f('iabnm') == 'ibm~~~~~+++an~~~~~'

# 1171,31,2	steps: 132.0
def f(text, search_string):
    indexes = []
    while search_string in text:
        indexes.append(text.rindex(search_string))
        text = text[:text.rindex(search_string)]
    return indexes
assert f('ONBPICJOHRHDJOSNCPNJ9ONTHBQCJ', 'J') == [28, 19, 12, 6]

# 642,13,2	steps: 229.0
def f(text, m, n):
    text = "{}{}{}".format(text, text[:m], text[n:])
    result = ""
    for i in range(n, len(text)-m):
        result = text[i] + result
    return result
assert f("abcdefgabc", 1, 2) == 'bagfedcacbagfedc'

# 845,6,3	steps: 376.0
def f(sentence):
    ls = list(sentence)
    for letter in ls:
        if not letter.istitle():
            ls.remove(letter)
    return ''.join(ls)
assert f('XYZ LittleRedRidingHood LiTTleBIGGeXEiT fault') == 'XYZLtRRdnHodLTTBIGGeXET fult'

# 218,45,3	steps: 457.0
def f(text):
    text = list(text)
    for i in range(len(text)):
        if i % 2 == 1:
            text[i] = text[i].swapcase()
    return ''.join(text)
assert f('Hey DUdE THis $nd^ &*&this@#') == 'HEy Dude tHIs $Nd^ &*&tHiS@#'


