import subprocess
import sys
from pathlib import Path
from tkr_utils.app_paths import AppPaths
from tkr_utils.config_logging import setup_logging
from tkr_utils.decorators import logs_and_exceptions

logger = setup_logging(__file__)

@logs_and_exceptions(logger)
def generate_documentation(package_name: str) -> bool:
    """
    Generate documentation for the specified package using pydoctor.

    Args:
        package_name (str): The name of the package to document.

    Returns:
        bool: True if documentation was generated successfully, False otherwise.
    """
    try:
        package_docs_dir = AppPaths.DOCS_DIR / package_name
        package_docs_dir.mkdir(parents=True, exist_ok=True)

        package_path = AppPaths.BASE_DIR / package_name

        if not package_path.exists():
            logger.error(f"Package directory not found: {package_path}")
            return False

        cmd = [
            sys.executable, "-m", "pydoctor",
            "--project-name", package_name,
            "--verbose",
            "--html-output", str(package_docs_dir),
            "--theme", "readthedocs",
            "--docformat", "google",
            "--intersphinx", "https://docs.python.org/3/objects.inv",
            str(package_path)
        ]

        logger.info(f"Generating documentation for {package_name}")
        result = subprocess.run(cmd, capture_output=True, text=True)

        if result.returncode == 0:
            logger.info(f"Documentation generated successfully for {package_name}")
            return True
        else:
            logger.error(f"Failed to generate documentation for {package_name}")
            logger.error(f"pydoctor output: {result.stdout}")
            logger.error(f"pydoctor errors: {result.stderr}")
            return False

    except Exception as e:
        logger.error(f"An error occurred while generating documentation for {package_name}: {str(e)}")
        return False