samples = {
    "sample_01":{
        "gene":"BRCA1",
        "organism":"Human"
    }, 
    "sample_02":{
        "gene":"TP53",
        "organism":"Human"
    }
}
print(samples["sample_01"]["gene"])
samples["sample_01"]["function"] = "DNA repair"
print(samples)
for sample_id, detail in samples.items():
    print("Sample:", sample_id)
    for key, value in detail.items():
        print(key, value, sep=": ")
    print()