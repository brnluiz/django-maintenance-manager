from api.models import Location, Flat, Room

Location.objects.all()
l = Location(postal='E14PE', city='London', address='Mile End Road 432', building='Lindop House')
l.save()

f1 = Flat(identificator='1', location=l)
f1.save()

f10 = Flat(identificator='10', location=l)
f10.save()

r1 = Room(identificator='A', flat=f10)
r1.save()

r2 = Room(identificator='B', flat=f10)
r2.save()
