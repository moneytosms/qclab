import glob
import re
import nbformat

# Find all Activity_*.ipynb files
files = glob.glob("Activity_*.ipynb")

# Sort numerically: Activity_1, Activity_2, ...
files.sort(key=lambda x: int(re.search(r"Activity_(\d+)\.ipynb", x).group(1)))

# Create a new notebook
merged = nbformat.v4.new_notebook()
merged.cells = []

for file in files:
    nb = nbformat.read(file, as_version=4)

    # Optional: add a markdown heading before each notebook's content
    merged.cells.append(nbformat.v4.new_markdown_cell(f"# {file}"))

    merged.cells.extend(nb.cells)

# Save merged notebook
output_file = "2024BCS0055_Lab_Activity_1.ipynb"
nbformat.write(merged, output_file)

print(f"Merged {len(files)} notebooks into '{output_file}'")
