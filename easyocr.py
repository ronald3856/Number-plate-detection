import matplotlib.pyplot as plt
import cv2
import easyocr
from IPython.display import Image
Image("plates/scaned_img_0 ")
reader = easyocr.Reader(['en'])
output = reader.readtext('/scaned_img_0.jpg')
# Import necessary libraries
import pandas as pd

# Load the datasets (replace with actual file paths in your Google Drive if needed)
license_plate_df = pd.read_csv('/content/LicensePlate.csv')
emission_details_df = pd.read_csv('/content/EmissionDetails.csv')
fine_details_df = pd.read_csv('/content/FineDetails.csv')


# Function to fetch details based on license plate number
def get_license_plate_details(plate_number):
    # Find the plate ID based on the license plate number
    license_plate = license_plate_df[license_plate_df['plate_number'] == plate_number]

    if license_plate.empty:
        print(f"No details found for license plate: {plate_number}")
        return

    plate_id = license_plate.iloc[0]['plate_id']
    print(f"Details for License Plate: {plate_number}")
    print("\nLicense Plate Information:")
    print(license_plate)

    # Fetch emission details
    emission_details = emission_details_df[emission_details_df['plate_id'] == plate_id]
    print("\nEmission Details:")
    if emission_details.empty:
        print("No emission details available.")
    else:
        print(emission_details)

    # Fetch fine details
    fine_details = fine_details_df[fine_details_df['plate_id'] == plate_id]
    print("\nFine Details:")
    if fine_details.empty:
        print("No fine details available.")
    else:
        print(fine_details)



# Input: License Plate Number
plate_number = output[0][1]
get_license_plate_details(plate_number)
