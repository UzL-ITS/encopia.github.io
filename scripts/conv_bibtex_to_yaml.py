# Adapted from https://github.com/antoniosgeme/antoniosgeme.github.io/blob/master/assets/python/bib_to_yml.py

import bibtexparser
import yaml
import requests

def load_bibtex(source, target, entries):
    # Load the BibTeX file
    with open(source, 'r', encoding='utf-8') as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)

    # Convert each entry to a dictionary
    entries[target] = []

    for (i,entry) in enumerate(bib_database.entries):
        print("Processing entry " + str(i+1) + " of "+str(len(bib_database.entries)))

        entry_dict = {
            'title': entry.get('title', ''),
            'author': entry.get('author', ''),
            'journal': entry.get('journal', ''),
            'volume': entry.get('volume', ''),
            'number': entry.get('number', ''),
            'pages': entry.get('pages', ''),
            'year': entry.get('year', ''),
            'publisher': entry.get('publisher', ''),
            'doi': entry.get('DOI', ''),
            'type': None,
        }
        
        if entry['ENTRYTYPE'] == 'article':
            if entry.get('keywords', '') == 'abstract':
                entry_dict['type'] = 'abstract'
            else:
                entry_dict['type'] = 'journal'
        else:
            if entry.get('keywords', '') == 'abstract':
                entry_dict['type'] = 'abstract'
            else:
                entry_dict['type'] = 'conference'
        
        # Remove empty fields
        entry_dict = {k: v for k, v in entry_dict.items() if v}

        entries[target].append(entry_dict)

    

def main():
    entries = {}

    load_bibtex('_bibliography/bibliography.bib', 'publications', entries)
    load_bibtex('_bibliography/references.bib', 'previous_work', entries)
    
    # Write the YAML file
    with open('_data/bib.yml', 'w', encoding='utf-8') as yaml_file:
        yaml.dump(entries, yaml_file, default_flow_style=False, allow_unicode=True)
        #yaml_file.write("\n")  # Add an empty line between entries

    print('BibTeX to YAML conversion complete. Output saved as publications.yml.')


if __name__ == "__main__":
    main()
