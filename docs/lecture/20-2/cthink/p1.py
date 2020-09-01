def test(s):
    r = 0
    for i, v in enumerate(s[::-1]):
        r += int(v) * (9 ** i)
    return r

r = test('1399')
print(r)