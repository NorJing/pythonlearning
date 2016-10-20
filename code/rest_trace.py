import sys

# python -m trace --trace  --timing rest_trace.py

def eggs_generator():
    yield 'eggs'
    yield 'EGGS!'

def spam_generator():
    yield 'spam'
    yield 'spam!'
    yield 'SPAM!'

generator = spam_generator()
print(next(generator))
print(next(generator))
print(next(generator))

# sys.settrace(None)

generator = eggs_generator()
print(next(generator))