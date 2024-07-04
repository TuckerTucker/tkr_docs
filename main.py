from tkr_utils.app_paths import AppPaths
from tkr_utils.config_logging import setup_logging
from tkr_utils.decorators import logs_and_exceptions
from .pydoctor_generator import generate_documentation
from .index_generator import generate_index_html

logger = setup_logging(__file__)

@logs_and_exceptions(logger)
def generate_all_documentation(packages: list[str]) -> None:
    """
    Generate documentation for all specified packages and create an index.html file.

    Args:
        packages (list[str]): List of package names to document.
    """
    AppPaths.check_directories()
    
    successful_packages = []
    for package in packages:
        if generate_documentation(package):
            successful_packages.append(package)
        else:
            logger.warning(f"Skipping {package} due to errors.")
    
    generate_index_html(successful_packages)

if __name__ == "__main__":
    packages_to_document = ["tkr_chat", "tkr_utils", "tkr_simple_rag", "tkr_erm", "tkr_agents", "tkr_save_page", "tkr_searxng"]
    generate_all_documentation(packages_to_document)
    logger.info(f"Documentation generation complete. Files saved in {AppPaths.DOCS_DIR}")