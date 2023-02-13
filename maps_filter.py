menue=["espresoo","mocha","lattie","cappuccino","amrecano","cortado"]

def find_coffe(coffee):
    if coffee[0]=='c':
        return coffee

# map_coffee=map(find_coffe,menue)
# for x in map_coffee:
#     print(x)

filter_coffee=filter(find_coffe,menue)
for x in filter_coffee:
    print(x)


