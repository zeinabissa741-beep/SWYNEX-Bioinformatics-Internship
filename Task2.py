import requests
import time
from Bio.Blast import NCBIXML

rid = "F665558Z014"

url = "https://blast.ncbi.nlm.nih.gov/Blast.cgi"

params = {
    "CMD": "Get",
    "RID": rid,
    "FORMAT_TYPE": "XML"
}

while True:
    response = requests.get(url, params=params)

    if "Status=WAITING" in response.text:
        print("BLAST is still running. Checking again in 60 seconds...")
        time.sleep(60)

    elif "Status=FAILED" in response.text:
        print("BLAST search failed.")
        break

    elif "Status=READY" in response.text:
        if "ThereAreHits=no" in response.text:
            print("No hits found.")
            break

        print("BLAST search completed!")
        with open("blast_results.xml", "w") as file:
            file.write(response.text)
        break
with open("blast_results.xml") as result_handle:
    blast = NCBIXML.read(result_handle)

for alignment in blast.alignments:
    print(alignment.title)