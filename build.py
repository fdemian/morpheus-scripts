from os.path import join, isdir, isfile
from os import makedirs, remove
from shutil import copy2, copytree, rmtree
import datetime

# Input folders
api_folder = r"path\to\morpheus-api"
frontend_folder = r"path\to\morpheus-frontend"

# Destination folder
dest_folder = r"path\to\build-folder"


# Generate name of build folder.
def generate_build_name(dest_folder):
    now_date = datetime.datetime.now()
    date_formatted = '{0}-{1}-{2}'.format(now_date.day, now_date.month, now_date.year)

    return dest_folder + "_" + date_formatted


def clear_file_structure(files, folders, destination):
    
    # Clear all files.
    for file in files:
        if isfile(join(destination, file)):
            remove(join(destination, file))

    # Remove all folders
    for folder in folders:
        if isdir(join(destination, folder)):
            rmtree(join(destination, folder))


def copy_file_structure(files, folders, source, destination, prefix=None):

    # Start copying files
    for file in files:       
        copy2(join(source, file), join(destination, file))

    # Copy static folders
    for folder in folders:        
        if prefix is None:
            source_dest=join(source, folder)
        else:
            source_dest=join(source, join(prefix, folder)) 
		        	
        copytree(source_dest, join(destination, folder))


if __name__ == "__main__":

    # Create destination folder if it does not exist.
    destination_folder = generate_build_name(dest_folder)

    if not isdir(destination_folder):
        makedirs(destination_folder)


    """
      ########################### BACKEND ###########################
    
      Copies the backend structure (mainly python files).
      
    """

    backend_files = [
        "LICENSE",
        "README.md",
        "__init__.py",
        "main.py",
        "modcp.py",
        "commonpass.txt",
        "requirements.txt",
        "robots.txt",
        "setup.py",
		"config.ini",
		"Pipfile",
		"Pipfile.lock"
    ]

    backend_folders = [ "api" ]

    clear_file_structure(backend_files, backend_folders, destination_folder)

    copy_file_structure(backend_files, backend_folders, api_folder, destination_folder)

    """    
      ########################### FRONTEND ###########################

      Copies the frontend structure inside a folder named "static".
    """

    frontend_files = [
      "favicon.ico",
      "index.html",
      "asset-manifest.json",	  
      "service-worker.js"
    ]

    frontend_folders = [
	   "css",
	   "js",
       "media"
    ]

    frontend_build_folder = join(frontend_folder, "build")
    frontend_dest = join(destination_folder, "static")

    # If static directory does not exist, create it.
    if not isdir(frontend_dest):
        makedirs(frontend_dest)

    clear_file_structure(frontend_files, frontend_folders, frontend_dest)
    copy_file_structure(frontend_files, frontend_folders, frontend_build_folder, frontend_dest, prefix="static")
