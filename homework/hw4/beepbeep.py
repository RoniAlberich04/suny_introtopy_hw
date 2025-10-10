vehicles = {}

while True:
    print("\n1. Add Vehicle")
    print("2. View Vehicles")
    print("3. Add km")
    print("0. Exit")
    choice = input("Choose: ")
    
    if choice == "1":
        plate = input("Plate: ")
        if plate in vehicles:
            print("This plate already exists!")
            continue
        km = int(input("Km: "))
        vehicles[plate] = km
        print("Added.")
        
    elif choice == "2":
        for plate, km in vehicles.items():
            print(f"{plate}: {km} km")
    
    elif choice == "3":
        plate = input("Plate: ")
        if plate not in vehicles:
            print("Plate not found.")
            continue
        new_km = int(input(f"New km (old: {vehicles[plate]}): "))
        if new_km < vehicles[plate]:
            print("Cannot decrease km.")
            continue
        vehicles[plate] = new_km
        print("Updated.")
        
    elif choice == "0":
        print("Exit.")
        break

    else:
        print("Invalid choice.")