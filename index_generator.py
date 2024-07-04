from tkr_utils.app_paths import AppPaths
from tkr_utils.config_logging import setup_logging
from tkr_utils.decorators import logs_and_exceptions

logger = setup_logging(__file__)

@logs_and_exceptions(logger)
def generate_index_html(packages: list[str]) -> None:
    """
    Generate an index.html file with tabs for each package's documentation.

    Args:
        packages (list[str]): List of package names.
    """
    nav_tabs = ""
    tab_content = ""

    for i, package in enumerate(packages):
        active = "active" if i == 0 else ""
        show = "show" if i == 0 else ""
        selected = "true" if i == 0 else "false"
        
        display_name = package.replace('tkr_', '').replace('_', ' ').capitalize()

        nav_tabs += f"""
        <button class="nav-link {active}" id="nav-{package}-tab" data-bs-toggle="tab" 
                data-bs-target="#nav-{package}" type="button" role="tab" 
                aria-controls="nav-{package}" aria-selected="{selected}">{display_name}</button>
        """

        tab_content += f"""
        <div class="tab-pane fade {show} {active}" id="nav-{package}" role="tabpanel" aria-labelledby="nav-{package}-tab">
            <iframe src="{package}/index.html"></iframe>
        </div>
        """

    index_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Package Documentation</title>
        <!-- Bootstrap CSS -->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body {{
                background-color: rgba(0,0,0,0.05);
                color: rgb(64, 64, 64);
                font-family: Lato, proxima-nova, "Helvetica Neue", Arial, sans-serif;
                font-size: 16px;
                margin: 0;
                min-height: 100vh;
                overflow-x: hidden;
                word-break: break-word;
            }}
            .container-fluid {{
                max-width: 960px;
            }}
            .nav-tabs {{
                background-color: rgb(52, 49, 49);
            }}
            .nav-link {{
                color: #D2EFFF !important;
            }}
            .nav-link:hover, .nav-link.active {{
                background-color: rgba(255, 255, 255, 0.1) !important;
                color: #fff !important;
            }}
            .tab-content {{
                background-color: rgb(252, 252, 252);
                padding: 20px;
                height: calc(100vh - 42px);
            }}
            .tab-pane {{
                height: 100%;
            }}
            iframe {{
                width: 100%;
                height: 100%;
                border: none;
            }}
            h1, h2, h3, h4, h5, h6 {{
                font-weight: bold;
                font-family: "Roboto Slab", Georgia, Arial, sans-serif;
            }}
            a, a:visited {{
                text-decoration: none;
                color: #337ab7;
            }}
            a:hover {{
                text-decoration: underline;
                color: #23527c;
            }}
            ::-webkit-scrollbar {{
                width: 0;
            }}
        </style>
    </head>
    <body>
        <nav>
            <div class="nav nav-tabs" id="nav-tab" role="tablist">
                {nav_tabs}
            </div>
        </nav>
        <div class="tab-content" id="nav-tabContent">
            {tab_content}
        </div>

        <!-- Bootstrap JS -->
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    </body>
    </html>
    """
    
    index_path = AppPaths.DOCS_DIR / "index.html"
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(index_content)
    
    logger.info(f"Index file generated at {index_path}")