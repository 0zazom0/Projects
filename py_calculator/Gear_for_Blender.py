import os
def Gear_for_Blender():

    # Definition
    print("""
    edendum changes the actual radius
    regardless of the addendum and dedendum.
    Addendum is added to the actual dedendum.
    Radius pulls both the addendum and dedendum.
    ↑Diff↑ → ↓actual radius and dedendum↓ ↑Addendum↑.
    ↑DiffR↑ → ↓smaller actual radius↓\n
    """)
    print("Enter 'q' to quit\n")
    
    while True:
        # Input
        # teeth
        teeth = input("teeth: ").strip()
        if teeth.lower() == 'q':
            return
        try:
            teeth = int(teeth)
            if teeth <= 0:
                print("Invalid input")
                print("Input shall not be lower than 0\n")
                continue
        except ValueError:
            print("Invalid input\n")
            continue
        # hole
        hole = input("hole: ").strip()
        if hole.lower() == 'q':
            return
        try:
            hole = float(hole)
            if hole <= 0:
                print("Invalid input")
                print("Input shall not be lower than 0\n")
                continue
        except ValueError:
            print("Invalid input\n")
            continue
        # diameter
        diameter = input("Ø: ").strip()
        if diameter.lower() == 'q':
            return
        try:
            diameter = float(diameter)
            if diameter <= 0:
                print("Invalid input")
                print("Input shall not be lower than 0\n")
                continue
            if diameter <= hole:
                print("Invalid input")
                print("Input shall not be lower or equal to hole\n")
                continue
        except ValueError:
            print("Invalid input\n")
            continue
        # Gear
        Gear = input("Gear: ").strip()
        if Gear.lower() == 'q':
            return
        try:
            Gear = float(Gear)
            if Gear <= 0 :
                print("Invalid input")
                print("Input shall not be lower than 0\n")
                continue
            if Gear <= hole:
                print("Invalid input")
                print("Input shall not be lower or equal to hole\n")
                continue
            if Gear <= diameter:
                print("Invalid input")
                print("Input shall not be lower or equal to diameter\n")
                continue
        except ValueError:
            print("Invalid input\n")
            continue
        # Diffr
        DiffR = input("DiffR: ").strip()
        if DiffR.lower() == 'q':
            return
        try:
            DiffR = float(DiffR)
        except ValueError:
            print("Invalid input\n")
            continue
        # Diff
        Diff = input("Diff: ")
        if Diff.lower() == 'q':
            return
        try:
            Diff = float(Diff)
        except ValueError:
            print("Invalid input\n")
            continue


        # Calculations
        Base =( diameter - hole) / 2
        Addendum = diameter / teeth
        Dedendum = Addendum * 1.25 + DiffR if DiffR != 0 else Addendum * 1.25
        Radius = (diameter / 2) + Dedendum

        if Diff > 0:
            Addendum += (Diff)
            Radius -= (Diff)
        elif Diff < 0:
            Addendum -= abs(Diff)
            Radius += abs(Diff)
        else:
            Addendum += (Diff)
            Radius += (Diff)

        # Results
        print("\nResults:\n")
        print(f"Number of teeth → {teeth:}")
        print(f"Radius → {Radius:.3f}")
        print(f"Base → {Base:.3f}")
        print(f"Dedendum → {Dedendum:.3f}")
        print(f"Addendum → {Addendum:.3f}\n")
if __name__ == "__main__":
    Gear_for_Blender()