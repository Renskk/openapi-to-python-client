import os
import yaml
import typer
import shutil
import codecs
import pathlib

from pathlib import Path
from typing import Optional
from typing import List, Optional, Sequence, Union
from openapi_python_client.config import Config
from openapi_python_client.parser import GeneratorData
from openapi_python_client.parser.errors import GeneratorError
from openapi_python_client import cli, MetaType, MetaType, Project, utils, _get_document

current_file = Path(__file__).resolve().parent
temp_path = os.path.join(current_file, "templates")
config_path = os.path.join(current_file, "config.yaml")
config_data = {}

with open(config_path) as f:
    config_data = yaml.safe_load(f)


class OpenapiClientGenerate(Project):
    
    def __init__(self, *, openapi: GeneratorData, meta: MetaType, config: Config, custom_template_path: Optional[Path], file_encoding: str = "utf-8") -> None:
        super().__init__(openapi=openapi, meta=meta, config=config, custom_template_path=custom_template_path, file_encoding=file_encoding)
        
    def build(self) -> Sequence[GeneratorError]:
        """Create the project from templates"""

        if self.meta == MetaType.NONE:
            print(f"Generating {self.package_name}")
        else:
            print(f"Generating {self.project_name}")
            if not self.project_dir.exists():
                self.project_dir.mkdir()
        self._create_package()
        self._build_models()
        self._build_api()
        self._run_post_hooks()
        return self._get_errors()
    
    def update(self) -> Sequence[GeneratorError]:
        """Update an existing project"""

        if not self.package_dir.is_dir():
            return [GeneratorError(detail=f"Directory {self.package_dir} not found")]
        print(f"Updating {self.package_name}")
        shutil.rmtree(self.package_dir)
        self._create_package()
        self._build_models()
        self._build_api()
        self._run_post_hooks()
        return self._get_errors()

    def _build_api(self) -> None:
        imports: List[str] = []
        def_params: List[tuple(str, str)] = []
        # Generate included Errors
        errors_path = self.package_dir / "errors.py"
        errors_template = self.env.get_template("errors.py.jinja")
        errors_path.write_text(errors_template.render(), encoding=self.file_encoding)

        # Generate endpoints
        api_dir = self.package_dir / "api"
        api_dir.mkdir()
        api_init_path = api_dir / "__init__.py"
        api_init_template = self.env.get_template("api_init.py.jinja")
        api_init_path.write_text(api_init_template.render(), encoding=self.file_encoding)

        endpoint_collections_by_tag = self.openapi.endpoint_collections_by_tag
        endpoint_template = self.env.get_template(
            "endpoint_module.py.jinja", globals={"isbool": lambda obj: obj.get_base_type_string() == "bool"}
        )
        for tag, collection in endpoint_collections_by_tag.items():
            tag_dir = api_dir / tag
            tag_dir.mkdir()

            endpoint_init_path = tag_dir / "__init__.py"
            endpoint_init_template = self.env.get_template("endpoint_init.py.jinja")
            endpoint_init_path.write_text(
                endpoint_init_template.render(endpoint_collection=collection),
                encoding=self.file_encoding,
            )

            for endpoint in collection.endpoints:
                save_name = utils.PythonIdentifier(endpoint.name, self.config.field_prefix)
                module_path = tag_dir / f"{save_name}.py"
                module_path.write_text(
                    endpoint_template.render(
                        endpoint=endpoint,
                    ),
                    encoding=self.file_encoding,
                )
                imports.append(f"from {self.project_name}.{self.package_name}.api.{tag}.{save_name} import {endpoint.name.capitalize()}")
                def_params.append((save_name, endpoint.name.capitalize()))
        # from services/api/tag/name import Name
        client_path = self.package_dir / "client.py"
        client_template = self.env.get_template("client.py.jinja")
        client_path.write_text(client_template.render(imports=imports, def_params=def_params), encoding=self.file_encoding)


def get_project_for_url_or_path(
    url: Optional[str],
    path: Optional[Path],
    meta: MetaType,
    config: Config,
    custom_template_path: Optional[Path] = None,
    file_encoding: str = "utf-8",
) -> Union[OpenapiClientGenerate, GeneratorError]:
    data_dict = _get_document(url=url, path=path, timeout=config.http_timeout)
    if isinstance(data_dict, GeneratorError):
        return data_dict
    openapi = GeneratorData.from_dict(data_dict, config=config)
    if isinstance(openapi, GeneratorError):
        return openapi
    return OpenapiClientGenerate(
        openapi=openapi,
        custom_template_path=custom_template_path,
        meta=meta,
        file_encoding=file_encoding,
        config=config,
    )


def create_new_client(
    *,
    url: Optional[str] = None,
    path: Optional[Path] = None,
    config: Config = None,
    meta: MetaType = MetaType.POETRY,
    custom_template_path: Optional[Path] = None,
    file_encoding: str = "utf-8",
) -> Sequence[GeneratorError]:
    """
    Generate the client library

    Returns:
         A list containing any errors encountered when generating.
    """
    project = get_project_for_url_or_path(
        url=url,
        path=path,
        custom_template_path=custom_template_path,
        meta=meta,
        file_encoding=file_encoding,
        config=config,
    )
    if isinstance(project, GeneratorError):
        return [project]
    return project.build()


def update_existing_client(
    *,
    url: Optional[str] = None,
    path: Optional[Path] = None,
    meta: MetaType = MetaType.POETRY,
    config: Config = None,
    custom_template_path: Optional[Path] = None,
    file_encoding: str = "utf-8",
) -> Sequence[GeneratorError]:
    """
    Update an existing client library

    Returns:
         A list containing any errors encountered when generating.
    """
    project = get_project_for_url_or_path(
        url=url,
        path=path,
        custom_template_path=custom_template_path,
        meta=meta,
        file_encoding=file_encoding,
        config=config,
    )
    if isinstance(project, GeneratorError):
        return [project]
    return project.update()


app = typer.Typer()


# pylint: disable=too-many-arguments
@app.command()
def generate(
    url: Optional[str] = typer.Option(None, help="A URL to read the JSON from"),
    path: Optional[pathlib.Path] = typer.Option(None, help="A path to the JSON file"),
    custom_template_path: Optional[pathlib.Path] = typer.Option(None, **cli.custom_template_path_options),  # type: ignore
    meta: MetaType = cli._meta_option,
    file_encoding: str = typer.Option("utf-8", help="Encoding used when writing generated"),
    config_path: Optional[pathlib.Path] = cli.CONFIG_OPTION,
    fail_on_warning: bool = False,
) -> None:
    """Generate a new OpenAPI Client library"""

    if not url and not path and config_data.get('url') and config_data.get('path'):
        typer.secho("You must either provide --url or --path or config.json", fg=typer.colors.RED)
        raise typer.Exit(code=1)
    if url and path:
        typer.secho("Provide either --url or --path, not both", fg=typer.colors.RED)
        raise typer.Exit(code=1)

    try:
        codecs.getencoder(file_encoding)
    except LookupError as err:
        typer.secho(f"Unknown encoding : {file_encoding}", fg=typer.colors.RED)
        raise typer.Exit(code=1) from err

    url = url if url else config_data.get('url')
    path = path if path else Path(config_data.get('path'))
    custom_template_path = Path(temp_path) if custom_template_path is None else custom_template_path
    config = cli._process_config(config_path) if config_path else Config(**config_data.get('config'))
    
    errors = create_new_client(
        url=url,
        path=path,
        meta=meta,
        custom_template_path=custom_template_path,
        file_encoding=file_encoding,
        config=config,
    )
    cli.handle_errors(errors, fail_on_warning)


# pylint: disable=too-many-arguments
@app.command()
def update(
    url: Optional[str] = typer.Option(None, help="A URL to read the JSON from"),
    path: Optional[pathlib.Path] = typer.Option(None, help="A path to the JSON file"),
    custom_template_path: Optional[pathlib.Path] = typer.Option(None, **cli.custom_template_path_options),  # type: ignore
    meta: MetaType = cli._meta_option,
    file_encoding: str = typer.Option("utf-8", help="Encoding used when writing generated"),
    config_path: Optional[pathlib.Path] = cli.CONFIG_OPTION,
    fail_on_warning: bool = False,
) -> None:
    """Update an existing OpenAPI Client library

    The update command performs the same operations as generate except it does not overwrite specific metadata for the
    generated client such as the README.md, .gitignore, and pyproject.toml.
    """
    
    if not url and not path and config_data['url'] and config_data['path']:
        typer.secho("You must either provide --url or --path or config.json", fg=typer.colors.RED)
        raise typer.Exit(code=1)
    if url and path:
        typer.secho("Provide either --url or --path, not both", fg=typer.colors.RED)
        raise typer.Exit(code=1)

    try:
        codecs.getencoder(file_encoding)
    except LookupError as err:
        typer.secho(f"Unknown encoding : {file_encoding}", fg=typer.colors.RED)
        raise typer.Exit(code=1) from err

    url = url if url else config_data.get('url')
    path = Path(path) if path else Path(config_data.get('path'))
    custom_template_path = Path(temp_path) if custom_template_path is None else custom_template_path
    config = cli._process_config(config_path) if config_path else Config(**config_data.get('config'))
    
    errors = update_existing_client(
        url=url,
        path=path,
        meta=meta,
        custom_template_path=custom_template_path,
        file_encoding=file_encoding,
        config=config,
    )
    cli.handle_errors(errors, fail_on_warning)


app()
