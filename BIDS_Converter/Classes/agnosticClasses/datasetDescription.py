import os
from BIDS_Converter.util.queryASPEN import queryASPEN
from BIDS_Converter.util.util import popDicts

import sys
if "BIDS_Converter.Classes.datasetModule.DatasetModule" not in sys.modules:
    print(sys.modules)
    from BIDS_Converter.Classes.datasetModule import DatasetModule
    print("it wasn't there")
else:
    print("it was already there")
from typing import TYPE_CHECKING
 
if TYPE_CHECKING:
    from BIDS_Converter.Classes.bidsDataset import BidsDataset

class DatasetDescription(DatasetModule):
    def __init__(self, parent:"BidsDataset"):
        super().__init__(parent)
        self.JSONpath = os.path.join(parent.root, "dataset_description.json")
        
        #TO IMPLEMENT: KEY "DatasetLinks" IS REQUIRED IF URI's are used  

        reqs = ["Name", "BIDSVersion"]

        #TO IMPLEMENT: KEY "Authors" is RECOMMENDED if Citation.cff is not present 
        #SEE NOTE BELOW for GeneratedBy   

        reco = ["HEDVersion", "DatasetType", "License", "GeneratedBy", "SourceDatasets"]

        opts = ["Acknowledgements", "HowToAcknowledge", "Funding", "EthicsApprovals", "ReferencesAndLinks", "DatasetDOI"] 

        popDicts((self.required, reqs),(self.recommended, reco),(self.optional, opts))

    def query(self):
        self.query = ""
        return self.query

    def setup(self):
        pass

    def createBIDS(self):

        for child in self.children:
            child.createBIDS()
        return


def getGeneratedBy():
    from checks.checks import checkValidURI

    container = {
       "Type":None,
       "Tag":None,
       "URI":None,
    } 
    checkValidURI(container["URI"])

    generatedByDict = {
       "Name":None,
       "Version":None,
       "Description":None,
       "CodeURL":None,
       "Container":container
    } 
    return generatedByDict

"""
    # Hardcoded metadata
    description_data = {
        "Name": "iEEG Dataset 24H for Graz",
        "BIDSVersion": "1.6.0",
        "Authors": ["Hugo Sturkenboom, etc."],

    }

    # If the file already exists, merge with existing content
    if description_file.exists():
        print(f"Updating existing dataset_description.json: {description_file}")
        with open(description_file, "r") as f:
            existing_data = json.load(f)
        description_data = {**existing_data, **description_data}  # Merge existing and new data

    # Write to the dataset_description.json file
    with open(description_file, "w") as f:
        json.dump(description_data, f, indent=4)

    print(f"Dataset description saved at {description_file}")

"""

