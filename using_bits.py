def check_bit4(input):
  mask = 0b1000
  desired = input & mask
  if desired > 0:
    return "on"
  else:
    return "off"

#check the third bit from the right of a is turned on
a = 0b10111011
mask = 0b101111
desired = a | mask
print bin(desired)

#all of the bits in a are flipped
a = 0b11101110
mask = 0b11111111
desired = mask ^ a
print bin(desired)
