from big_integer import BigInteger


test_1 = BigInteger('101')
test_1_1 = BigInteger('101')
test_2 = BigInteger('102')
test_3 = BigInteger('-103')

print(test_3 < test_2)
print(test_1 < test_1_1)
print(test_1 <= test_1_1)
print(test_2 > test_1)
print(test_1 > test_1)
print(BigInteger('102') >= BigInteger('102'))
print(BigInteger('0') >= BigInteger('0'))
print(BigInteger('111') == BigInteger('111'))
print(BigInteger('-111') == BigInteger('111'))
print(BigInteger('-111') != BigInteger('111'))
print(BigInteger('5') + BigInteger('-20'))
print(BigInteger('10000') + BigInteger('-1'))
print(BigInteger('100') - BigInteger('1'))
print(BigInteger('-100') - BigInteger('-1'))

print(BigInteger('-123') * BigInteger('17'))
print(BigInteger('-5') * BigInteger('5'))

print(BigInteger('5') ** 2)
print(BigInteger('3') ** 3)

print(BigInteger('100') // BigInteger('95'))
print(BigInteger('-100') // BigInteger('95'))
print(BigInteger('100') % BigInteger('-95'))
print(BigInteger('1') % BigInteger('2'))

print(BigInteger('5')._int_to_bin(BigInteger('5')))
print(BigInteger('15')._int_to_bin(BigInteger('15')))  # 1111

print(BigInteger('15') & BigInteger('5'))  # 1011
print(BigInteger('15') ^ BigInteger('5'))  # 0101
print(BigInteger('15') | BigInteger('5'))  # 111

print(BigInteger('15') << BigInteger('2'))  # 111100
print(BigInteger('15') >> BigInteger('2'))  # 11

