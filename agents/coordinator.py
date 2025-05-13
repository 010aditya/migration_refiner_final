import os
from agents.embedding_indexer import EmbeddingIndexerAgent
from agents.context_stitcher import ContextStitcherAgent
from agents.fix_and_complete import FixAndCompleteAgent
from agents.build_validator import BuildValidatorAgent
from agents.retry_agent import RetryAgent
from agents.test_generator import TestGeneratorAgent
from agents.package_structure_normalizer import PackageStructureNormalizerAgent
from agents.migrated_file_stitcher import MigratedFileStitcherAgent

class CoordinatorAgent:
    def __init__(self, mapping):
        self.mapping = mapping
        self.embedding_agent = EmbeddingIndexerAgent()
        self.context_agent = ContextStitcherAgent(self.embedding_agent)
        self.fix_agent = FixAndCompleteAgent()
        self.retry_agent = RetryAgent()
        self.test_agent = TestGeneratorAgent()
        self.build_agent = BuildValidatorAgent()
        self.package_normalizer = PackageStructureNormalizerAgent()
        self.stitcher = MigratedFileStitcherAgent()

    def run(self):
        self.embedding_agent.index_all_code()

        for entry in self.mapping:
            src = entry['sourcePath']
            target_paths = entry.get('targetPaths', [entry.get('targetPath')])
            if not target_paths: continue

            context = self.context_agent.build_context(src)
            migrated_code = self.stitcher.stitch(target_paths)
            fixed_code = self.fix_agent.fix(None, context + "\n\n" + migrated_code)

            final_target = target_paths[0]
            with open(final_target, 'w') as f:
                f.write(fixed_code)

            self.test_agent.generate(final_target)

        self.package_normalizer.normalize()
        if not self.build_agent.validate():
            self.retry_agent.retry_failed()
