"""
Visual and algebraic demonstration of the sum of the first n integers,
which is `n` squared
"""

#  visually:
# Inspired by "Thinking Recursively" by Eric S. Roberts, page 17
for i in range(1, 11):
    print(' ', '-' * (i * 2 - 1))
    print('First', i, 'odd integers', ':')
    print(' + '.join([str(x) for x in range(1, i*2, 2)]), '=', i**2)
    print(i, 'x', i, '=', i**2)
    print('   ', ' '.join(str(y+1) for y in range(i)))
    for j in range(i):
        print(f'{j+1:>3}', '• ' * i)

# algebraically
# at any `n` the average value would be `n` itself, and the sum would be
# multiplying `n` by the number of odd integers, which also happens to be `n`
# hence n-squared
for i in range(1, 10):
    print(' ', '-' * (i * 2 - 1))
    print('First', i, 'odd integers', ':')
    print(' + '.join([str(x) for x in range(1, i*2, 2)]))
    print(' + '.join([str(i) for x in range(1, i*2, 2)]))
    print(i, 'x', i, '=', i**2)


def numeric_square(x):
    """Print a square of integers ranging from 1 to x-squared.
    Demonstrate the `square` shape of the sum of the first n
    odd integers."""
    squared = x ** 2
    for n in range(1, squared + 1, x):
        print(' '.join([f'{str(y):>3}' for y in range(n, n+x)]))


# numerically: simply print the relationship
for i in range(1, 13):
    print(f'{i:>3}: {" + ".join(str(x) for x in range(1, i * 2, 2)):->55} '
          f'= {sum((range(1,i*2, 2))):>4}')

for i in range(1, 11):
    print(' ', '-' * (i * 2 - 1))
    print('First', i, 'odd integers', ':')
    print(' + '.join([str(x) for x in range(1, i*2, 2)]), '=', i**2)
    print(i, 'x', i, '=', i**2)
    numeric_square(i)
