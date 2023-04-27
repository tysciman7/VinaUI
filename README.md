# VINA UI
## A desktop UI for AutoDock Vina

#### This UI was developed to make running AutoDock Vina a seamless process for anyone wishing to simulate receptor/ ligand binding
### Notes:
- This Application requires AutoDock Vina installed on the device. To install AutoDock Vina, see [Installing Vina](https://vina.scripps.edu/downloads/)
- An executable/ script is provided to eliminate the need for the terminal
  - This application can still be run via an IDE or terminal by running main.py

### Running VinaUI for the First Time
#### Initializing your Paths
- A dialog window will appear prompting you to initialize your paths
- {Image of Initialize Path Dialog Goes Here}
1. Designate the location of vina
   - Windows: C:\Program Files (x86)\The Scripps Research Institute\Vina\Vina.exe
   - Mac/ Linux: 
2. Designate a directory/ folder for your data to be accessed/ stored
   - You may designate where each component of your data goes with the "Sub Paths" option
   - Notes: 
     - The configuration file will be created and stored in the parent Data directory
     - You must specify your data directory before continuing/ changing your Sub Paths
3. Once you have designated your paths, click "Ok"
- Note: You will have the option to change any directory you wish later (Config Menu -> Reconfigure Paths)
###### Go to where your designated your data directories and add in your receptors and ligands
:heavy_exclamation_mark: Make sure each receptor and ligand is in a *.pdbqt format
#### Setting up your Configuration File
###### Here your will designate the parameters for vina to run
- {Image of Main VinaUI Window Goes Here}
1. Select a receptor
2. Select a ligand (if you are running only one)
3. Fill in the GridBox parameters: Center X,Y,Z ; Size X,Y,Z ; Exhaustiveness
4. Fill in a seed or check the "random seed"
   - Note: If "Random Seed" is selected, each ligand run on vina will use a randomized seed (Including when running All ligands)
5. Determine if you would like to run the "Selected Ligand" or "Run All Ligands" within a desired ligand directory (Click respective button)
###### If "Run Selected Ligand" was chosen then vina will run with the given GridBox, Exhaustiveness, and Seed parameters
###### If "Run All Ligands" was chosen a new dialog will appear
#### Running All Ligands
- A dialog window will appear with the option to change your ligand directory (for this run only)
- {Image of Run All Ligands Dialog Goes Here}
- You are given the option to sort the output by binding affinity
  - If you choose to sort, you must designate a directory for the output files to go
    - Once you begin the run, a new directory will be made with the name "RUN_All_Ligands..." followed by the date and time
    - Once the run is complete a "SORTED_LIST" follow by the date and time will be created and the file will contain all ligands ran along with their respective binding affinities (In order of best to worst binding)
  - If sort is not selected, then all ligand output and log files will be placed in their previously initialized directories
- Click "Ok" to run all the ligands with the configuration data you specified on the previous window
  - Note: If you selected "Randomized Seed" each ligand will be run with a different randomized seed
