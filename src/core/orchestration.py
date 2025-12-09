import json
import os
import logging
from typing import Dict, Any
from ..agents.data_parser_agent import DataParserAgent
from ..agents.question_generator_agent import QuestionGeneratorAgent
from ..agents.content_logic_agent import ContentLogicAgent
from ..agents.competitor_agent import CompetitorGenerationAgent
from ..agents.page_assembler_agent import PageAssemblerAgent
from ..agents.validation_agent import ValidationAgent

logger = logging.getLogger(__name__)

class Orchestrator:
    """
    Manages the workflow of agents to generate content.
    
    Attributes:
        data_parser (DataParserAgent): Agent to parse input data.
        question_generator (QuestionGeneratorAgent): Agent to generate questions.
        competitor_generator (CompetitorGenerationAgent): Agent to generate competitor analysis.
        content_logic (ContentLogicAgent): Agent to generate content logic.
        page_assembler (PageAssemblerAgent): Agent to assemble final pages.
        validator (ValidationAgent): Agent to validate generated pages.
    """
    def __init__(self):
        self.data_parser = DataParserAgent()
        self.question_generator = QuestionGeneratorAgent()
        self.competitor_generator = CompetitorGenerationAgent()
        self.content_logic = ContentLogicAgent()
        self.page_assembler = PageAssemblerAgent()
        self.validator = ValidationAgent()

    def run(self, input_file_path: str, output_dir: str) -> None:
        """
        Executes the content generation workflow.

        Args:
            input_file_path (str): Path to the input JSON file.
            output_dir (str): Directory to save the generated output.
        """
        logger.info(f"Starting orchestration with input: {input_file_path}")
        
        try:
            # 1. Load Input
            if not os.path.exists(input_file_path):
                logger.error(f"Input file not found: {input_file_path}")
                return

            with open(input_file_path, 'r') as f:
                raw_data = json.load(f)
                
            # 2. Parse Data
            logger.info("Agent: DataParserAgent working...")
            product_model = self.data_parser.run(raw_data)
            logger.info("Data parsed successfully.")
            
            # 3. Generate Questions
            logger.info("Agent: QuestionGeneratorAgent working...")
            questions = self.question_generator.run(product_model)
            logger.info(f"Generated {len(questions)} questions.")
            
            # 4. Generate Competitor
            logger.info("Agent: CompetitorGenerationAgent working...")
            competitor = self.competitor_generator.run(product_model)
            logger.info("Competitor generated.")

            # 5. Generate Content Logic
            logger.info("Agent: ContentLogicAgent working...")
            # ContentLogicAgent now takes both product and competitor
            content_blocks = self.content_logic.run(product_model, competitor)
            logger.info("Content logic blocks generated.")
            
            # 6. Assemble Pages
            logger.info("Agent: PageAssemblerAgent working...")
            assembly_data = {
                "product": product_model,
                "questions": questions,
                "content_blocks": content_blocks,
                "competitor": competitor
            }
            final_pages = self.page_assembler.run(assembly_data)
            logger.info("Pages assembled.")
            
            # 7. Validate Pages
            self.validator.run(final_pages)
            
            # 8. Save Output
            self._save_output(final_pages, output_dir)
            logger.info(f"All outputs saved to {output_dir}")

        except Exception as e:
            logger.exception(f"An error occurred during orchestration: {e}")
            raise

    def _save_output(self, pages: Dict[str, Any], output_dir: str) -> None:
        """
        Saves the generated pages to the output directory.

        Args:
            pages (Dict[str, Any]): Dictionary of generated pages.
            output_dir (str): Directory to save the files.
        """
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            
        for name, content in pages.items():
            filename = f"{name}.json"
            path = os.path.join(output_dir, filename)
            try:
                with open(path, 'w') as f:
                    json.dump(content, f, indent=2)
                logger.info(f"Saved {filename}")
            except IOError as e:
                logger.error(f"Failed to save {filename}: {e}")
