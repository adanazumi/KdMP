def calculate_kd():
    try:
        # Input values
        receptor_total = float(input("Enter the total concentration of receptor: "))
        ligand_total = float(input("Enter the total concentration of ligand: "))
        receptor_bound = float(input("Enter the MP counts of bound receptor: "))
        receptor_unbound = float(input("Enter the MP counts of unbound receptor: "))

        # Calculate the conversion factor (CF)
        CF = receptor_total / (receptor_bound + receptor_unbound)

        # Perform the conversion
        Rbound = receptor_bound * CF
        Runbound = receptor_unbound * CF
        Lunbound = ligand_total - Rbound

        # Calculate the Kd
        Kd = (Lunbound * Runbound) / Rbound

        print("The Kd (microMolar) of the interaction is:", Kd)
    except ValueError:
        print("Invalid input. Please enter numerical values.")

calculate_kd()
