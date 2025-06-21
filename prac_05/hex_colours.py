COLOURS={"alice blue":"#f0f8ff",
         "baby pink":"#f4c2c2",
         "camel":"c19a6b",
         "daffodil":"#ffff31",
         "emerald":"#50c878",
         "fawn":"#e5aa70",
         "ginger":"#b06500",
         "han blue":"#446ccf",
         "indigo":"#4b0082",
         "jade":"#00a86b"}
color_name=input("Enter a color: ").lower()
while color_name != "":
    try:
        print(f"{color_name} is {COLOURS[color_name]}")
    except KeyError:
        print("Invalid color name")
    color_name = input("Enter a color: ").lower()
print("Thanks for playing!")