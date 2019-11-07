import json
from dpm import DirectPathwayMapping

def getReconAsDict():
    # Convert json to dictionary (RECON2 Data)
    json_file = open('assets/recon2.json')  # Getting RECON Data
    json_str = json_file.read()  # Processing RECON Data
    json_file.close()
    db = json.loads(json_str)  # Processing RECON Data
    return db
    # Convert json to dictionary (RECON2 Data)

def analyze():
    # Convert breast cancer fold change data to dict
    json_file = open('assets/breast_cancer_sample.json')  # Getting RECON Data
    json_str = json_file.read()  # Processing RECON Data
    json_file.close()
    fold_changes = json.loads(json_str)  # Processing RECON Data
    analysis = DirectPathwayMapping(fold_changes)
    analysis.run()
    return analysis.result_pathways
    # return fold_changes
    # Convert breast cancer fold change data to dict

def getMetabolitesByPathway(pathway):
    db = getReconAsDict() # getting recon data
    reactions = db['pathways'][pathway]
    # fold_changes = getSampleFoldChanges()  # get fold changes
    metabolites = []
    for reaction in reactions:
        metabolite_data = db['reactions'][reaction]['metabolites']
        for metabolite in metabolite_data:
            if not metabolite in metabolites:
                metabolites.append(metabolite)
    common_metabolites = []  # this will store the common metabolites with breast cancer sample data
    # for key in fold_changes:
    #     if key in metabolites:
    #         common_metabolites.append(metabolite)
    # If you want to see common metabolites, you may remove the following line's #
    # print(common_metabolites)
    return metabolites

result = analyze()
for pathway, score in result.items():
    print("Pathway: " + pathway + " --- Score: " + str(score))
# print(getMetabolitesByPathway('Aminosugar metabolism'))