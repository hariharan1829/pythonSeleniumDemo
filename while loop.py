#while loops are used to check the condition, it keeps on literate until the condition becomes false
      # only if the condition is true it goes into the loop
      # make sure the way to make the condition false

# break -- Cuts the loop
# continue -- breaks the iteration and keeps on the above steps

loop = 11

while loop>10:
   loop = loop + 1
   if loop < 15:
       print(loop)
       continue
   if loop == 20:
       print(loop)
       break
   print(f"loop break completed {loop}")
