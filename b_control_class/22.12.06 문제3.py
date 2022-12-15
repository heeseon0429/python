def count_vowel(x):
    cnt=0
    for char in x:
        if char in ['a','e','i','o','u']:
            cnt+=1
    return cnt

print(count_vowel('pythonian'))