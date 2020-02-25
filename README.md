**Build scripts**
==================

Scripts to manage the application.

 Build (*build.py*): 
 ===============
 
 Build the application. 
 
 This script assumes that you have already built the frontend application (*morpheus-frontend*). In order to build the application you must:
 
  1) Specify the location of the source folders (both API and frontend) in the following lines

   ```
   # Input folders
   api_folder = "/path/to/backend/morpheus-api"
   frontend_folder = "/path/to/frontend/morpheus-frontend"
   ```
   
  2) Specify the destination folder.

	```
    # Destination folder
    dest_folder = "/path/to/destination/<build folder name>"
	```
 
  3) Run the build script

    ```
    python3 build.py
	```
