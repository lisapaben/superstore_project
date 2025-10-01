# scripts/download_dataset.py
"""
Download and prepare the Superstore dataset from Kaggle.

What it does:
1. Creates a `data/` folder if it doesn't exist.
2. Downloads dataset from Kaggle.
3. Unzips contents into `data/superstore_data/`.
4. Looks for the first Excel OR CSV file and moves it up to `data/`.
5. Renames it to a clean name: Superstore.xls or Superstore.csv
"""

from kaggle.api.kaggle_api_extended import KaggleApi
import os
import zipfile
import shutil

def download_superstore(output_dir="data", dataset_slug="vivek468/superstore-dataset-final"):
    os.makedirs(output_dir, exist_ok=True)

    api = KaggleApi()
    api.authenticate()

    zip_name = dataset_slug.split("/")[-1] + ".zip"
    zip_path = os.path.join(output_dir, zip_name)

    print(f"Downloading dataset '{dataset_slug}' to {output_dir} ...")
    api.dataset_download_files(dataset_slug, path=output_dir, unzip=False, force=False)

    if os.path.exists(zip_path):
        extracted_dir = os.path.join(output_dir, "superstore_data")
        print("Unzipping to", extracted_dir)
        with zipfile.ZipFile(zip_path, 'r') as z:
            z.extractall(extracted_dir)
        print("Unzip complete.")

        # Look for Excel or CSV
        data_found = None
        for root, _, files in os.walk(extracted_dir):
            for fname in files:
                if fname.lower().endswith((".xls", ".xlsx", ".csv")):
                    source_path = os.path.join(root, fname)
                    ext = os.path.splitext(fname)[1].lower()
                    dest_name = "Superstore" + ext  # standardize name
                    dest_path = os.path.join(output_dir, dest_name)
                    if os.path.exists(dest_path):
                        os.remove(dest_path)
                    shutil.move(source_path, dest_path)
                    data_found = dest_path
                    print(f"Moved file to: {dest_path}")
                    break
            if data_found:
                break

        if not data_found:
            print("No Excel/CSV file found. Check folder:", extracted_dir)
        else:
            print("Dataset ready at:", data_found)

    else:
        print("Download finished but zip not found at", zip_path)


if __name__ == "__main__":
    download_superstore()
