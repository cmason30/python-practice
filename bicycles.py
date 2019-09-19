bicycles = [ 'trek', 'cannondale','redline', 'specialized']
print(bicycles[0])
message = f"My first bike was a {bicycles[1].title()}"
print(message)
motorcycles = ["honda", "bmw", "jeep"]
motorcycles.append("ducati")
motorcycles.insert(2, "frog")
popped_motorcycles = motorcycles.pop()
first_owned = motorcycles.pop(0)

message2 = f"My first bike was a {first_owned.title()}."
print(message2)
too_expensive = "bmw"
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")