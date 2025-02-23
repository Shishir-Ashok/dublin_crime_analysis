import json
import geopandas as gpd
from shapely.geometry import Point, Polygon, MultiPolygon, LineString

# Load the raw Overpass API JSON
with open("all_buildings.json", "r", encoding="utf-8") as f:
    raw_data = json.load(f)

# Extract nodes into a dictionary for reference
node_dict = {node["id"]: (node["lon"], node["lat"]) for node in raw_data["elements"] if node["type"] == "node"}

# Extract ways into a dictionary for relations
way_dict = {way["id"]: way for way in raw_data["elements"] if way["type"] == "way"}

# Prepare GeoJSON features
features = []

for element in raw_data["elements"]:
    if element["type"] == "node":
        # Add nodes as point features
        geom = Point(node_dict[element["id"]])
        features.append({
            "type": "Feature",
            "geometry": geom,
            "properties": element.get("tags", {})
        })
    elif element["type"] == "way":
        # Extract ways as LineString or Polygon
        coords = [node_dict[node_id] for node_id in element["nodes"]]
        if coords[0] == coords[-1]:  # Closed geometry => Polygon
            geom = Polygon(coords)
        else:  # Open geometry => LineString
            geom = LineString(coords)
        features.append({
            "type": "Feature",
            "geometry": geom,
            "properties": element.get("tags", {})
        })
    elif element["type"] == "relation" and element.get("tags", {}).get("type") == "multipolygon":
        # Process multipolygon relations
        outer = []
        inner = []
        for member in element["members"]:
            if member["type"] == "way" and member["ref"] in way_dict:
                coords = [node_dict[node_id] for node_id in way_dict[member["ref"]]["nodes"]]
                if len(coords) >= 4:  # Ensure valid polygon geometry
                    if member["role"] == "outer":
                        outer.append(Polygon(coords))
                    elif member["role"] == "inner":
                        inner.append(Polygon(coords))
                else:
                    print(f"Skipping invalid geometry with less than 4 points: {coords}")
        if outer:
            geom = MultiPolygon(outer) if len(outer) > 1 else outer[0]
            features.append({
                "type": "Feature",
                "geometry": geom,
                "properties": element.get("tags", {})
            })

# Create a GeoDataFrame
gdf = gpd.GeoDataFrame.from_features(features)

# Save to GeoJSON
gdf.to_file("output.geojson", driver="GeoJSON")
print("Converted data saved to 'output.geojson'.")

