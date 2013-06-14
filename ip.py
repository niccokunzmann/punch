

def is_valid_ipv4(s):
    assert isinstance(s, str)
    l = s.split('.')
    if len(l) != 4: return False
    if not all(map(str.isdigit, l)): return False
    l = map(int, l)
    if not all([0 <= i <= 255 for i in l]): return False
    return True

assert is_valid_ipv4('1.2.3.4')
assert not is_valid_ipv4('1.2.3.-4')
assert not is_valid_ipv4('1.2.4')
assert not is_valid_ipv4('')
assert not is_valid_ipv4('1231.2.3.4')
assert not is_valid_ipv4('0.256.3.4')



