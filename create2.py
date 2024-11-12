#Generate all combinations of violated sequence according to the available reaction time obtained from non-violated sequence

def wrap_around(value):
    """Wraps the given value to fit within the range 1-10."""
    return (value - 1) % 10 + 1

def wrap_values_in_combos(combos):
    """Wraps integer values in the combos to fit within the range 1-10."""
    wrapped_combos = []
    for combo in combos:
        wrapped_combo = []
        for val in combo:
            if isinstance(val, int):  # Only wrap integers
                wrapped_val = wrap_around(val)
                wrapped_combo.append(wrapped_val)
            else:  # For non-integer values (like strings), just append them as is
                wrapped_combo.append(val)
        wrapped_combos.append(wrapped_combo)
    return wrapped_combos

# Open a file to store results
with open("output_combos.txt", "w") as file:
    # Iterate over all possible selected keys from 1 to 10
    for selected_key in range(1, 11):
        # Generate sets for the selected key
        set1 = [selected_key - 2, selected_key - 1, "Violation_Image"]
        set2 = [selected_key - 3, selected_key - 2, selected_key - 1, "Violation_Image"]
        set3 = [selected_key - 4, selected_key - 3, selected_key - 2, selected_key - 1, "Violation_Image"]

        # Ensure the sets contain no negative indices by wrapping the values
        set1 = [wrap_around(val) if isinstance(val, int) else val for val in set1]
        set2 = [wrap_around(val) if isinstance(val, int) else val for val in set2]
        set3 = [wrap_around(val) if isinstance(val, int) else val for val in set3]

        # Generate the predictable sequence for List_B in Forward direction
        List_B_forward = [selected_key + i for i in range(2, 7)]  # key +2 to key +6

        # Generate the predictable sequence for List_B in Backward direction
        List_B_backward = [selected_key + i for i in range(1, 6)]  # key +1 to key +5

        # Create the new lists for forward combinations
        new_lists_set1_forward = [[element, element + 1, element + 2] for element in List_B_forward]
        new_lists_set2_forward = [[element, element + 1] for element in List_B_forward]
        new_lists_set3_forward = [[element] for element in List_B_forward]

        # Generate Combos for set1 in forward
        Combos_set1_forward = [set1 + new_list for new_list in new_lists_set1_forward]
        wrapped_Combos_set1_forward = wrap_values_in_combos(Combos_set1_forward)

        # Generate Combos for set2 in forward
        Combos_set2_forward = [set2 + new_list for new_list in new_lists_set2_forward]
        wrapped_Combos_set2_forward = wrap_values_in_combos(Combos_set2_forward)

        # Generate Combos for set3 in forward
        Combos_set3_forward = [set3 + new_list for new_list in new_lists_set3_forward]
        wrapped_Combos_set3_forward = wrap_values_in_combos(Combos_set3_forward)

        # Create the new lists for backward combinations
        new_lists_set1_backward = [[element, element + 1, element + 2] for element in List_B_backward]
        new_lists_set2_backward = [[element, element + 1] for element in List_B_backward]
        new_lists_set3_backward = [[element] for element in List_B_backward]

        # Generate Combos for set1 in backward
        Combos_set1_backward = [set1 + new_list for new_list in new_lists_set1_backward]
        wrapped_Combos_set1_backward = wrap_values_in_combos(Combos_set1_backward)

        # Generate Combos for set2 in backward
        Combos_set2_backward = [set2 + new_list for new_list in new_lists_set2_backward]
        wrapped_Combos_set2_backward = wrap_values_in_combos(Combos_set2_backward)

        # Generate Combos for set3 in backward
        Combos_set3_backward = [set3 + new_list for new_list in new_lists_set3_backward]
        wrapped_Combos_set3_backward = wrap_values_in_combos(Combos_set3_backward)

        # Write to the file for Forward combos
        file.write(f"Selected Key: {selected_key} (Forward)\n")
        #file.write(f"Set1: {set1}\n")
        #file.write(f"Set2: {set2}\n")
        #file.write(f"Set3: {set3}\n")
        file.write("Combos for Set1:\n")
        for combo in wrapped_Combos_set1_forward:
            file.write(f"{combo}\n")
        file.write("Combos for Set2:\n")
        for combo in wrapped_Combos_set2_forward:
            file.write(f"{combo}\n")
        file.write("Combos for Set3:\n")
        for combo in wrapped_Combos_set3_forward:
            file.write(f"{combo}\n")

        # Write to the file for Backward combos
        file.write(f"Selected Key: {selected_key} (Backward)\n")
        file.write(f"Set1: {set1}\n")
        file.write(f"Set2: {set2}\n")
        file.write(f"Set3: {set3}\n")
        file.write("Combos for Set1:\n")
        for combo in wrapped_Combos_set1_backward:
            file.write(f"{combo}\n")
        file.write("Combos for Set2:\n")
        for combo in wrapped_Combos_set2_backward:
            file.write(f"{combo}\n")
        file.write("Combos for Set3:\n")
        for combo in wrapped_Combos_set3_backward:
            file.write(f"{combo}\n")
        
        file.write("\n")  # Add a newline to separate entries for each selected_key

print("Results have been written to output_combos.txt.")