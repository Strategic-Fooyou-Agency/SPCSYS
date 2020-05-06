from django.test import TestCase

# Create your tests here.
a={
    '1': 1,
    '2': 2,

}
b=a.pop('1')
print(a,b)