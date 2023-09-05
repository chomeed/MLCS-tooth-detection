from pycocotools.coco import COCO
import numpy as np
from scipy.spatial import distance
from scipy.sparse.csgraph import minimum_spanning_tree
import matplotlib.pyplot as plt

# Specify the path to the COCO dataset annotations file and the category name
dataDir = '/home/summer23_intern1/workspace/MLCS-tooth-detection/mmdetection/data/tooth_detection/sample'
annFile = '/home/summer23_intern1/workspace/MLCS-tooth-detection/mmdetection/data/tooth_detection/annotations/tooth_only_clean.json'

'''
10954372최현경_최현경_000_intraoral_lower.jpg 498616
10955662신경원_신경원_000_intraoral_upper.jpg 498633
10955717김신_김신_000_intraoral_upper.jpg 498643
'''

# Initialize COCO API for instance annotations
coco = COCO(annFile)

# Get the category ID for the specified category name
# cat_ids = coco.getCatIds(catNms=[category_name])

# Get image ID 
img_id = 498616 

# Extract center coordinates
center_coords = []

# Get all the annotations for the specified category
ann_ids = coco.getAnnIds(img_id)
anns = coco.loadAnns(ann_ids)

for ann in anns:
    x, y, w, h = ann['bbox']
    center_x = x + (w / 2)
    center_y = y + (h / 2)
    center_coords.append([center_x, center_y])

center_coords = np.array(center_coords)

# Compute pairwise distances between center coordinates
pairwise_distances = distance.pdist(center_coords)

# Compute the MST
mst = minimum_spanning_tree(distance.squareform(pairwise_distances))

# Find the root node (you can choose any node as the root)
root = 0  # Change this if needed

def depth_first_traversal(node, parent, adjacency_list, result):
    result.append(node)
    for neighbor in adjacency_list[node]:
        if neighbor != parent:
            depth_first_traversal(neighbor, node, adjacency_list, result)

# Create an adjacency list representation of the MST
adjacency_list = {}
edges = np.transpose(mst.nonzero())
for edge in edges:
    u, v = edge
    if u not in adjacency_list:
        adjacency_list[u] = []
    if v not in adjacency_list:
        adjacency_list[v] = []
    adjacency_list[u].append(v)
    adjacency_list[v].append(u)

# Initialize the result list
ordered_points = []

# Start the depth-first traversal from the root node
depth_first_traversal(root, None, adjacency_list, ordered_points)

# Extract the center coordinates of the nodes in the order they were visited
ordered_center_coords = [center_coords[node] for node in ordered_points]

# Plot the center coordinates
plt.scatter(center_coords[:, 0], center_coords[:, 1], c='blue', marker='o', label='Center Coords')

# Plot the MST edges
for edge in edges:
    plt.plot(center_coords[edge, 0], center_coords[edge, 1], c='red', linewidth=0.5)

plt.xlabel('X-coordinate')
plt.ylabel('Y-coordinate')
plt.title('Minimum Spanning Tree')
plt.legend(loc='upper right')
plt.show()
