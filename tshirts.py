def size(cms):
    if cms < 38:
        return 'S'
    elif cms >= 38 and cms =< 42:
        return 'M'
    else:
        return 'L'

# Weak tests (all pass, even with bug)
assert(size(37) == 'S')
assert(size(40) == 'M')
assert(size(43) == 'L')

# Strong tests to expose the bug
def test_size():
    assert size(38) == 'M', "38 should be M (not S or L)"  # This will fail
    assert size(42) == 'L', "42 should be L (not M)"       # This will fail if logic is wrong

test_size()
print("All is well (maybe!)")

