import phonenumbers
from phonenumbers import geocoder as gd
number = phonenumbers.parse('5585495953')
print(number)
print(gd.description_for_number(number,'it'))