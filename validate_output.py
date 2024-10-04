import random

def sample_and_verify(input_path, output_path, sample_size=10):
    with open(input_path, 'r') as infile:
        input_lines = infile.readlines()

    
    original_dict = {}
    i = 0
    while i < len(input_lines):
        line = input_lines[i].strip()
        if line.startswith('>'):
            parts = line.split('|')
            accession_number = parts[1]
            protein_name = ' '.join(parts[2].split(' ')[1:]).split(' OS=')[0].strip()
            key = f"{accession_number}_{protein_name}"
            
            sequence = ''
            for seq_line in input_lines[i + 1:]:
                if seq_line.startswith('>'):
                    break
                sequence += seq_line.strip()
            original_dict[key] = sequence
        i += 1

    # Read the output dictionary
    with open(output_path, 'r') as outfile:
        output_lines = outfile.read().split('\n\n')

    # Create dictionary from output file
    output_dict = {}
    for entry in output_lines:
        if entry.strip():
            key, value = entry.split(': ', 1)
            output_dict[key] = value.strip()

    # Randomly sample keys from the original dictionary
    sampled_keys = random.sample(list(original_dict.keys()), sample_size)

    # Compare the sequences in the sample
    for key in sampled_keys:
        if key in output_dict:
            if original_dict[key] != output_dict[key]:
                print(f"Discrepancy found for {key}")
        else:
            print(f"Key missing in output: {key}")

    print("Sample verification complete.")

# Run the sampling verification
input_file = 'full_data.txt' 
output_file = 'full_output.txt'  
sample_and_verify(input_file, output_file)
