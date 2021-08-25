# Function
- Align (translate and rotate) the GLYCAM_06j-generated glycan to the relative protein ASN site. 
- Delete the terminal OH or OMe from the glycan and save the coordinates of protein and glycans in a single PDB file.

# Usage
## Create a virtual environment
`conda create --name transrot python=3.8`

## Activate virtual environment
`conda activate transrot`

## Deactivate
`conda deactivate`

## Install bentdna package
`pip install -e .`

## Upgrade package
`pip install -e . --upgrade`
