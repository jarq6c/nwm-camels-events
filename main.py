"""Process CAMELS bains."""
from custom_modules.configuration import load_config
from custom_modules.data import load_camels_list, download_files

def main():
    """Main function to process CAMELS basins."""
    # Read configuration file
    config = load_config("config.json")

    # Create the data directory if it doesn't exist
    config.data_dir.mkdir(parents=True, exist_ok=True)

    # Download the CAMELS basins data
    config = download_files(config)

    # Load CAMELS list
    camels_list = load_camels_list(config)

    print(camels_list)

if __name__ == '__main__':
    # Call the main function to execute the script
    main()
