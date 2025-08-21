input = "dev_bag.txt" 
output = "dev_bag_converted.txt"

# converts data from provided format to URLNet accepted format
with open(input, "r") as input_data, open(output, "w") as output_data:
    for line in input_data:
        cleaned_line = line.strip().replace("__label__", "")

        split_line = cleaned_line.split(maxsplit=1)

        if split_line[0] == '0':
            split_line[0] = '-1'
        elif split_line[0] == '1':
            split_line[0] = '+1'
        
        relabelled_line = "\t".join(split_line)
        output_data.write(relabelled_line + "\n")
