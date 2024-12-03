# cintel-07-tdash

Penguins Dashboard
This project is an interactive dashboard built using PyShiny to explore the Palmer Penguins dataset.

Instructions to Create the App:
Clone the repository:

bash
Copy code
git clone https://github.com/kersha0530/cintel-07-tdash.git
cd cintel-07-tdash
Install the required Python packages:

bash
Copy code
pip install -r requirements.txt
Launch the app locally:

bash
Copy code
shiny run --reload --launch-browser app/app.py
To deploy the app:

Use shinylive to generate static files:
bash
Copy code
shinylive export app docs
Push the changes to the docs folder in the repository.
Features:
Value Boxes: Summarizes the number of penguins, average bill length, and depth.
Scatterplot Visualization: Displays bill length vs. bill depth.
Interactive DataGrid: View and filter penguin data dynamically.
Resources:
GitHub Source
Issues
PyShiny Documentation
Template: Basic Dashboard
