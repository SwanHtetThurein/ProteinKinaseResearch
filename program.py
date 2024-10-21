import re

def convert_to_dict(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    result_dict = {}
    
    for i in range(len(lines)):
        line = lines[i].strip()
        if line.startswith('>'):
            parts = line.split('|')
            accession_number = parts[1] 

            # Extract the protein name and OX number using regex
            match = re.search(r'OS=.+? OX=(\d+)', parts[2])
            if match:
                ox_number = match.group(1)  # The number after OX=
            else:
                ox_number = ''  # Handle case if OX number is not found

            # Extract the composite identifier and protein name
            composite_identifier = parts[2].split(' ')[0]
            protein_name = ' '.join(parts[2].split(' ')[1:]).split(' OS=')[0].strip()

            sequence = ''
            # Extract the sequence  
            for seq_line in lines[i + 1:]:
                seq_line = seq_line.strip()
                # Stop capturing sequence when a new identifier is encountered
                if seq_line.startswith('>'):
                    break
                sequence += seq_line
            
            # Combine uniprot id, protein name, and OX number in the key
            key = f"{accession_number}_{protein_name}_{ox_number}"
            result_dict[key] = sequence
        
        i += 1
    return result_dict

# Example usage
file_path = 'full_data.txt'  # Replace with your file path
protein_dict = convert_to_dict(file_path)

# Save the output to a new text file
with open('full_output.txt', 'w') as output_file:
    for key, value in protein_dict.items():
        output_file.write(f'{key}: {value}\n\n')
