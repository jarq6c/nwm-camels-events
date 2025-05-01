from hydrotools.nwis_client.iv import IVDataService

def main():
    # Create an instance of the IVDataService class
    client = IVDataService()

    # Retrieve data
    data = client.get(
        sites=["01013500"]
    )

    print(data)

if __name__ == '__main__':
    # Call the main function to execute the script
    main()
