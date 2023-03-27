#!/usr/bin/env python3

from owner import Owner, CONN, CURSOR
from pet import Pet, CONN, CURSOR

# Owner.create_table()
# frank = Owner("frank", "555-555-5555", "frank@gmail.com", "555 Somewhere St.")
# frank.save()

# Class Method
Pet.create_table()

spot = Pet.create("spot", "dog", "chihuahua", "feisty")
bori = Pet.create("Bori", "dog", "Jindo", "Kind")

# Instance Method
# spot.save()
# bori.save()

import ipdb; ipdb.set_trace()
