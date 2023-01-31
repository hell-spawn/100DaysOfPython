# break loops
sample_1 = "some_name = the_value"
for position in range(len(sample_1)):
    if sample_1[position] in '=:':
        break
    print( f"name={sample_1[:position]!r}",
            f"value={sample_1[position+1:]!r}")


sample_2 = "name_only"
print(len(sample_2))
for position in range(len(sample_2)):
    print(sample_2[position])
    if sample_2[position] in '=:':
        break
    print( f"name={sample_2[:position]!r}",
            f"value={sample_2[position+1:]!r}")
    
position = -1
for position in range(len(sample_2)):
    print(position)
    if sample_2[position] in '=:':
        break

if position == -1:
    print(f"name=None value=None")
elif not(sample_2[position] == ':' or sample_2[position] == '='):
    print(f"name={sample_2!r} value=None")
else:
    print( f"name={sample_2[:position]!r}",
            f"value={sample_2[position+1:]!r}")

# Leveraging exception matching rules

