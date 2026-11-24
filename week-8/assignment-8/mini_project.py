import csv

skipped_rows = []

def dirtydata(filename):
    try:
        with open(filename, 'r', newline="") as f:
            reader = csv.DictReader(f)
            return list(reader)
    except FileNotFoundError:
        print(f"Could not find '{filename}'.")
        return []    
    except csv.Error as e:
        print(f"Could not parse '{filename}': {e}")
        return []    
        
        
def floatcheck(listedfile):
    clean_data = []
    rows_attempted = 0
    parsed_row = 0
    rows_skipped = 0        
    for row_num, row in enumerate(listedfile, start=1):
        rows_attempted += 1
        if None in row:
            skipped_rows.append(f"Row {row_num}: Extra Column Detected --> Skipped")
            rows_skipped += 1
            continue
        else:
            try:
                row['amount'] = float(row['amount'])
                clean_data.append(row)
                parsed_row += 1
            except ValueError as e:
                skipped_rows.append(f"Row {row_num}: ValueError -- {e}")
                rows_skipped += 1
            except KeyError as e:
                skipped_rows.append(f"Row {row_num}: KeyError -- {e}")
                rows_skipped += 1
    return clean_data, parsed_row, rows_attempted, rows_skipped

data = dirtydata("week-8/data/messy_data.csv")
clean_data, parsed_row, rows_attempted, rows_skipped = floatcheck(data)

print(f"=== CSV Report ===\nRows attempted: {rows_attempted}\nRows parsed: {parsed_row}\nRows skipped: {rows_skipped}\n")
print(f"\nSkipped rows:")

for row in skipped_rows:
    print(row)

print(f"\nClean data:")

for row in clean_data:
    name = row['name']
    cat = row['category']
    amount = row['amount']
    print(f"{name} | {cat} | ${amount:.2f}")