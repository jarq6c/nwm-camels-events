"""Process CAMELS bains."""
from custom_modules.configuration import load_config, download_files

import pandas as pd
# from hydrotools.nwis_client.iv import IVDataService

def main():
    """Main function to process CAMELS basins."""
    # Read configuration file
    config = load_config("config.json")

    # Create the data directory if it doesn't exist
    config.data_dir.mkdir(parents=True, exist_ok=True)

    # Download the CAMELS basins data
    config = download_files(config)

    # Load CAMELS list
    camels_list = pd.read_csv(
        config.file_mapping["camels_list"].filepath,
        sep=";",
        dtype=str
        )

    print(camels_list)

if __name__ == '__main__':
    # Call the main function to execute the script
    main()
