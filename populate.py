from api.models import Location
from api.models import Flat
from api.models import Room
from api.models import Role
from api.models import Status
from api.models import Enquire
from api.models import Report

from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission

from api.models import Staff
from api.models import Resident

import datetime

# Populate Location 1
loc1 = Location.objects.create(postal='E14PE', city='London', address='Mile End Road 432', building='Lindop House')

flat1 = Flat.objects.create(identificator='1', location=loc1)
flat2 = Flat.objects.create(identificator='2', location=loc1)

room1 = Room.objects.create(identificator='A', flat=flat1)
room2 = Room.objects.create(identificator='B', flat=flat1)
room3 = Room.objects.create(identificator='A', flat=flat2)
room4 = Room.objects.create(identificator='B', flat=flat2)

# Populate Location 2
loc2 = Location.objects.create(postal='E14PD', city='London', address='Mile End Road 200', building='Sarney House')

flat3 = Flat.objects.create(identificator='1', location=loc2)
flat4 = Flat.objects.create(identificator='2', location=loc2)

room5 = Room.objects.create(identificator='A', flat=flat3)
room6 = Room.objects.create(identificator='B', flat=flat3)
room7 = Room.objects.create(identificator='A', flat=flat4)
room8 = Room.objects.create(identificator='B', flat=flat4)

# Role.objects.creates
role1 = Role.objects.create(title='Electrictrician', level=0)
role2 = Role.objects.create(title='Bricklayer', level=0)
role3 = Role.objects.create(title='General Technician', level=0)
role4 = Role.objects.create(title='Mechanic', level=0)

# Create Group and Permissions
managerGroup  = Group.objects.create(name='manager')
residentGroup = Group.objects.create(name='resident')
staffGroup    = Group.objects.create(name='staff')

# Create Users:
user1 = User.objects.create_user(username='lula', email='lula@staff.com', password='1234', 
    first_name='Luiz Inácio', last_name='Silva', 
    is_staff=True)
user1.groups.add(managerGroup)

user2 = User.objects.create_user(username='brunoluiz', email='bruno@student.com', password='1234', 
    first_name='Bruno Luiz', last_name='Silva', 
    is_staff=True)
user2.groups.add(residentGroup)

user3 = User.objects.create_user(username='admin', email='admin@admin.com', password='1234', 
    first_name='Bruno Luiz', last_name='Silva', 
    is_staff=True)
user3.groups.add(managerGroup)

# Staff.objects.create
staff1 = Staff.objects.create(phone='+44171990090', user=user1, role=role4)

# User
resident1 = Resident.objects.create(phone='+44332708329', user=user2, room=room1)

# Status.objects.create
status7 = Status.objects.create(title='Waiting work', urgency=3)
status2 = Status.objects.create(title='Work in Progress', urgency=1)
status3 = Status.objects.create(title='Awaiting delivery of materials', urgency=1)
status4 = Status.objects.create(title='Passed to specialist contractor', urgency=2)
status6 = Status.objects.create(title='Could not access area', urgency=3)
status5 = Status.objects.create(title='No fault could be found', urgency=-1)
status1 = Status.objects.create(title='Work Completed', urgency=0)

# Enquire
enquire1 = Enquire.objects.create(reference='339894', title='Replace Tubes Ceiling Lights', 
    status=status7, resident=resident1, location=loc1)

# Report
report1 = Report.objects.create(enquire=enquire1, staff=staff1, status=status7, reference='12354')
