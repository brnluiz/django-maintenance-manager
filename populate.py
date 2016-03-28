from api.models import Location
from api.models import Flat
from api.models import Room
from api.models import Role
from api.models import Employee
import datetime

# Populate Location 1
l = Location(postal='E14PE', city='London', address='Mile End Road 432', building='Lindop House')
l.save()

f1 = Flat(identificator='1', location=l)
f1.save()
f2 = Flat(identificator='2', location=l)
f2.save()

r1 = Room(identificator='A', flat=f1)
r1 = Room(identificator='B', flat=f1)
r3 = Room(identificator='A', flat=f2)
r4 = Room(identificator='B', flat=f2)
r1.save()
r2.save()
r3.save()
r4.save()

# Populate Location 2
l = Location(postal='E14PD', city='London', address='Mile End Road 200', building='Sarney House')
l.save()

f1 = Flat(identificator='1', location=l)
f1.save()
f2 = Flat(identificator='2', location=l)
f2.save()

r1 = Room(identificator='A', flat=f1)
r1 = Room(identificator='B', flat=f1)
r3 = Room(identificator='A', flat=f2)
r4 = Room(identificator='B', flat=f2)
r1.save()
r2.save()
r3.save()
r4.save()

# Roles
r1 = Role(title='Electrictrician', level=0)
r1.save()
r2 = Role(title='Bricklayer', level=0)
r2.save()
r3 = Role(title='General Technician', level=0)
r3.save()
r4 = Role(title='Mechanic', level=0)
r4.save()

# Employee
e = Employee(name='Luiz', surname='Silva', email='lula@qm.ac.uk', phone='+44171990090', 
    created_at=datetime.datetime.now(), role=r4)
e.save()
