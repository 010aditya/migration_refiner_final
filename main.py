import json
import os
from agents.metadata_agent import MetadataAgent
from agents.mapping_verifier import MappingVerifierAgent
from agents.mapping_collapser import MappingCollapserAgent
from agents.coordinator import CoordinatorAgent

if __name__ == "__main__":
    MetadataAgent().parse()
    MappingVerifierAgent().verify("mapping.json")
    MappingCollapserAgent("mapping.verified.json").collapse()

    with open("mapping.grouped.json") as f:
        verified_mapping = json.load(f)

    CoordinatorAgent(verified_mapping).run()
