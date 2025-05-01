"""Handle data downloading and processing."""
import pandas as pd
from hydrotools.nwm_client.FileDownloader import FileDownloader
from .configuration import Config

def load_camels_list(config) -> pd.DataFrame:
    """Load the CAMELS list from the configuration.
    
    Parameters
    ----------
    config : Config
        Configuration object containing file details.
    
    Returns
    -------
    pd.DataFrame
        DataFrame containing the CAMELS list.
    """
    return pd.read_csv(
        config.file_mapping["camels_list"].filepath,
        sep=";",
        dtype=str
        )

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
