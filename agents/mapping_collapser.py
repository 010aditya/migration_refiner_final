from collections import defaultdict
import json

class MappingCollapserAgent:
    def __init__(self, mapping_file="mapping.verified.json"):
        self.mapping_file = mapping_file

    def collapse(self, output_file="mapping.grouped.json"):
        with open(self.mapping_file) as f:
            raw_mappings = json.load(f)

        grouped = defaultdict(list)
        for entry in raw_mappings:
            grouped[entry["sourcePath"]].append(entry["targetPath"])

        collapsed = [
            {
                "sourcePath": source,
                "targetPaths": paths
            }
            for source, paths in grouped.items()
        ]

        with open(output_file, "w") as f:
            json.dump(collapsed, f, indent=2)

        print(f"✅ Grouped mappings written to {output_file}")
