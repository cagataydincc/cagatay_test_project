import faker
from faker import Faker

fake = Faker('tr_TR')

print(fake.name())
print(fake.email())
print(fake.country())
print(fake.phone_number())
print(fake.company())

for i in range(5):
    print(fake.email())