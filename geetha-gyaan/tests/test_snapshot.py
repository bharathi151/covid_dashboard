def my_func():
    return 7

def test_mything(snapshot):
    return_value = my_func()

    snapshot.assert_match(return_value, 'gpg_resonse')

def sum(num1, num2):
    return num1 + num2

def test_integer_sum(snapshot):
    num1 = 2
    num2 = 3
    return_value  = sum(num1, num2)
    snapshot.assert_match(return_value, 'integer_sum')

def test_negative_sum(snapshot):
    num1 = -2
    num2 = -3
    return_value  = sum(num1, num2)
    snapshot.assert_match(return_value, 'negative_sum')

def test_float_sum(snapshot):
    num1 = 2.3
    num2 = 3.2
    return_value  = sum(num1, num2)
    snapshot.assert_match(return_value, 'float_sum')

