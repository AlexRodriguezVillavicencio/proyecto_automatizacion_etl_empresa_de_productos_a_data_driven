def sep_detected(path):
    import csv 

    with open(path, 'r', errors='ignore') as csvfile:
        dialect = csv.Sniffer().sniff(csvfile.readline(), [',',';','|'])
        csvfile.seek(0)  
        data = csv.reader(csvfile, dialect)
    return data.dialect.delimiter

def encoding_detected(path):
    from charset_normalizer import detect

    with open(path, 'rb') as f:
        bytestring = f.read()
    result = detect(bytestring)

    if result['encoding'] is not None:
        encoding = result['encoding']
    return encoding



