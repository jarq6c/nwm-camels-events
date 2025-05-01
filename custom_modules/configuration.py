"""Handle project configuration file."""
from pathlib import Path
from pydantic import BaseModel, HttpUrl
from hydrotools.nwm_client.FileDownloader import FileDownloader

class FileDetails(BaseModel):
    """Details of the file to be downloaded.
    
    Attributes
    ----------
    url : HttpUrl
        URL to download the file from.
    filename : str
        Name of the file to be saved.
    filepath : Path | None
        Path where the file will be saved.
    """
    url: HttpUrl
    filename: str
    filepath: Path | None = None

class Config(BaseModel):
    """Configuration for downloading CAMELS basins data.
    
    Attributes
    ----------
    data_dir : Path
        Directory where the downloaded files will be stored.
    file_mapping : dict[str, FileDetails]
        Mapping of file names to their download URLs and file paths.
    """
    data_dir: Path
    file_mapping: dict[str, FileDetails]

def load_config(config_file: str) -> Config:
    """Load configuration from a JSON file.
    
    Parameters
    ----------
    config_file : str
        Path to the configuration JSON file.
    """
    with open(config_file, "r", encoding="utf-8") as fi:
        config = Config.model_validate_json(fi.read())
    return config

def download_files(config: Config) -> Config:
    """Download files specified in the configuration.
    
    Parameters
    ----------
    config : Config
        Configuration object containing file details and download URLs.
    
    Returns
    -------
    Config
        Updated configuration object with file paths.
    """
    file_list = []
    for k, v in config.file_mapping.items():
        config.file_mapping[k].filepath = config.data_dir / v.filename
        file_list.append((str(v.url), str(v.filepath)))
    downloader = FileDownloader()
    downloader.get(file_list)
    return config
