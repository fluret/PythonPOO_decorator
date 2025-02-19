import pint
ureg = pint.UnitRegistry()
vol = volume(3, 5) * ureg(volume.unit)

print(vol)

print(vol.to("cubic inches"))

print(vol.to("gallons").m)