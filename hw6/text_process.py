import string

# Download file from https://snap.stanford.edu/data/finefoods.txt.gz        
# Remember to gunzip before using
review_file = "foods.txt"

f_out = open("finefoods_cleaned.txt","w")

with open(review_file, encoding='LATIN-1') as f:
    lines = f.readlines()
    idx = 0
    num_lines = len(lines) - 2
    while idx < num_lines:
        while not lines[idx].startswith("review/score"):
            idx = idx + 1

        # Jump through hoops to satisfy the Unicode encodings and extract rating
        l = lines[idx].encode('ascii', 'ignore').decode('ascii')
        rating = int(float(l.strip().split(":")[1].strip()))

        while not lines[idx].startswith("review/text"):
            idx = idx + 1
            
        l = lines[idx].encode('ascii', 'ignore').decode('ascii').strip().lower()
        text = l.split(":")[1].strip()
        text = text.translate(str.maketrans("","", string.punctuation))

        f_out.write(str(rating)+": "+text+"\n")