import json
from dpm import DirectPathwayMapping

def analyze(file_name):
    json_file = open('assets/' + file_name)  # Getting fold changes
    json_str = json_file.read() 
    json_file.close()
    fold_changes = json.loads(json_str)  # Processing Fold Change Data
    analysis = DirectPathwayMapping(fold_changes)  # Forming the instance
    analysis.run()  # Making the analysis
    analysis.display_pathway_scores()  # printing pathway scores
    # analysis.display_reaction_scores() Needed to remove comment sign to see reaction scores

# Analyze function needs to get a filename from assets file to make the analysis by Direct Pathway Mapping
analyze('breast_cancer_sample.json')
# analyze('breast_cancer_sample_2.json')