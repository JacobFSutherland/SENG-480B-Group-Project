# How to get it all running
## Setting up your device
### Step 1:
- Install VSCode
    - Navigate to [here](https://code.visualstudio.com/download) to install VSCode
    - Follow their install instructions
### Step 2: 
- Have the Jupyter VSCode plugin installed and enabled
    - Open VSCode and use the ```ctrl + shift + x``` hotkey
    - Type in `Jupyter`
    - Click on `Jupyter` and press Install
    - Once Jupyter is installed Click `Enable`
### Step 3:
- Clone the repo then open the repo in VSCode
    - run ```git clone git@github.com:JacobFSutherland/SENG-480B-Group-Project.git```
    - Open VSCode and click File -> Open Folder -> The directory of the repo 

## Setting up the remote jupyter notebook through UVic's syzygy
### Step 1: 
- Navigate to [uvic.syzygy.ca](https://uvic.syzygy.ca/) and login

### Step 2:
- Create a new blank jupyter notebook to act as your server proxy
    - Press the upside down triangle on ```New``` in the top right
    - Press ```Python 3 (ipykernel)```

### Step 3:
- Get your token for that instance
    - Inside of your untitled notebook, press ```Control Panel``` in the top right. If asked to leave, press leave.
    - Press ```Token``` in the navbar at the top
    - Press ```Request New API Token``` and add a note called "SENG 480B API Token"
    - Save the token somewhere, like a blank notepad, or in your clipboard
    
    
## Connecting your device, and the remote jupyter notebook

### Step 1:
- With the API key you got, craft the following URL: ```https://uvic.syzygy.ca/jupyter/user/{{Your netlink ID}}?token={{Step 3 Token}}```
### Step 2:
- Use that connection string in vscode to set up your python kernel
    - In VSCode, open the file called ```main-notebook.ipynb```
    - Click on ```Select Kernel``` in the top right
    - Click ```Existing Jupyter Server```
    - Paste the URL from step 1
    - Select the ```Python3 (ipykernel) (untitled0.ipynb)``` runtime

# Now you are ready to code