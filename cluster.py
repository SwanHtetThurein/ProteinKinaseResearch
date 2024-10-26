from collections import defaultdict

# Initialize a dictionary to store clusters
clusters = defaultdict(list)

# Read the file and organize sequences
with open("/Users/swanthurein/Desktop/ProteinKinaseResearch/mmseq-0.3/DB_clu_30.tsv", "r") as file:
    for line in file:
        primary, associated = line.strip().split("\t")
        clusters[primary].append(associated)

# Write output with each cluster on a new line
with open("formatted_clusters.txt", "w") as output:
    for primary, associated_list in clusters.items():
        # Join associated sequences by commas
        associated_str = ",".join(associated_list)
        output.write(f"{primary}: {associated_str}\n")

print("Clusters have been written to formatted_clusters.txt")
