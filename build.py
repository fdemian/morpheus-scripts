from os.path import join, isdir
from os import makedirs, remove
from shutil import copy2, copytree, rmtree

# Input folders
api_folder = r"path\to\morpheus-api"
frontend_folder = r"path\to\morpheus-frontend"

# Destination folder
dest_folder = r"path\to\build-folder"

def clear_file_structure(files, folders, destination):
    
    # Clear all files.
    for file in files:
        remove(join(destination, file))

    # Copy all folders
    for folder in folders:
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
    ]

    backend_folders = [ "api" ]

    clear_file_structure(backend_files, backend_folders, dest_folder)
    copy_file_structure(backend_files, backend_folders, api_folder, dest_folder)

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
    frontend_dest = join(dest_folder, "static")

    # If static directory does not exist, create it.
    if not isdir(frontend_dest):
        makedirs(frontend_dest)

    clear_file_structure(frontend_files, frontend_folders, frontend_dest)
    copy_file_structure(frontend_files, frontend_folders, frontend_build_folder, frontend_dest, prefix="static")