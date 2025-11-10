#!/usr/bin/env python3
"""
generate_svg_4level.py - Enhanced taxonomy generator with 4-level hierarchy

Supports nested card structure:
# Title
## Central Question
### Category (colored box)
#### Subcategory (card inside category)
##### Item (bullet in card)
"""

import sys
import re
from pathlib import Path
from datetime import datetime

if len(sys.argv) < 2:
    print("Usage: python generate_svg_4level.py outline.md")
    sys.exit(1)

infile = Path(sys.argv[1])
if not infile.exists():
    print(f"File not found: {infile}")
    sys.exit(1)

text = infile.read_text(encoding="utf-8").splitlines()

# Layout constants
CANVAS_W = 2000
START_X = 100
TOP_ROW_Y = 280
DEFAULT_CATEGORY_HEIGHT = 320  # Increased for nested cards
CARD_W = 170  # Width of nested cards
CARD_H = 190  # Height of nested cards
CARD_GAP = 10
CARD_PAD = 20
ROW_GAP = 60
CARD_VERTICAL_OFFSET = 90
CATEGORIES_PER_ROW = 3

# Parse markdown - 4 level structure
title = "Diagram"
central = "WHAT ARE YOU TRYING TO DO?"
categories = []
current_cat = None
current_subcat = None

i = 0
n = len(text)

def parse_metadata(header):
    parts = [p.strip() for p in header.split("|")]
    name = parts[0]
    meta = {}
    for p in parts[1:]:
        for kv in p.split():
            if '=' in kv:
                k,v = kv.split('=',1)
                try:
                    meta[k.strip()] = int(v.strip())
                except:
                    meta[k.strip()] = v.strip()
    return name, meta

while i < n:
    line = text[i].rstrip()
    
    # H1: Title
    if line.startswith("# ") and not line.startswith("##"):
        title = line[2:].strip()
    
    # H2: Central Question
    elif line.startswith("## ") and not line.startswith("###"):
        central = line[3:].strip()
    
    # H3: Category
    elif line.startswith("### ") and not line.startswith("####"):
        header = line[4:].strip()
        name, meta = parse_metadata(header)
        row = meta.get('row', None)
        height = meta.get('height', DEFAULT_CATEGORY_HEIGHT)
        current_cat = {"name": name, "row": row, "height": height, "desc": "", "subcategories": []}
        categories.append(current_cat)
        
        # Check for description on next line
        j = i+1
        while j < n and text[j].strip()=="":
            j += 1
        if j < n and not text[j].startswith("#"):
            current_cat["desc"] = text[j].strip()
            i = j
        current_subcat = None
    
    # H4: Subcategory (nested card)
    elif line.startswith("#### ") and not line.startswith("#####"):
        if current_cat:
            subcat_title = line[5:].strip()
            current_subcat = {"title": subcat_title, "items": []}
            current_cat["subcategories"].append(current_subcat)
    
    # H5: Item
    elif line.startswith("##### "):
        if current_subcat:
            item_text = line[6:].strip()
            current_subcat["items"].append(item_text)
    
    # Dash bullet: Item (backward compatibility with 3-level format)
    elif line.startswith("- "):
        if current_subcat:
            item_text = line[2:].strip()
            current_subcat["items"].append(item_text)
    
    i += 1

# Assign rows automatically
for idx, cat in enumerate(categories):
    if cat["row"] is None:
        cat["row"] = (idx // CATEGORIES_PER_ROW) + 1

# Group by row
rows = {}
for cat in categories:
    r = cat["row"]
    if r not in rows:
        rows[r] = []
    rows[r].append(cat)

# Calculate positions
for row_num in sorted(rows.keys()):
    row_cats = rows[row_num]
    num_in_row = len(row_cats)
    
    # Calculate widths based on number of subcategories
    for cat in row_cats:
        num_subcats = len(cat["subcategories"])
        if num_subcats == 0:
            num_subcats = 1
        cat_width = CARD_PAD + (CARD_W + CARD_GAP) * num_subcats + CARD_PAD
        cat["width"] = cat_width
    
    # Total width of this row
    total_w = sum(c["width"] for c in row_cats) + CARD_GAP * (num_in_row - 1)
    start_x = (CANVAS_W - total_w) / 2
    
    # Position categories
    x = start_x
    y = TOP_ROW_Y + (row_num - 1) * (DEFAULT_CATEGORY_HEIGHT + ROW_GAP)
    
    for cat in row_cats:
        cat["x"] = x
        cat["y"] = y
        cat["center_x"] = x + cat["width"] / 2
        x += cat["width"] + CARD_GAP

# Calculate canvas height
max_y = max(cat["y"] + cat.get("height", DEFAULT_CATEGORY_HEIGHT) for cat in categories)
CANVAS_H = max_y + 100

# SVG Generation
out = []

def svg_header():
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{CANVAS_W}" height="{CANVAS_H}" viewBox="0 0 {CANVAS_W} {CANVAS_H}">
  <defs>
    <filter id="shadow" x="-50%" y="-50%" width="200%" height="200%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-opacity="0.15"/>
    </filter>

    <linearGradient id="blueGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#1e40af;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#93c5fd;stop-opacity:1" />
    </linearGradient>

    <linearGradient id="greenGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#15803d;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#86efac;stop-opacity:1" />
    </linearGradient>

    <linearGradient id="purpleGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#7e22ce;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#c084fc;stop-opacity:1" />
    </linearGradient>

    <linearGradient id="redGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#b91c1c;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#f87171;stop-opacity:1" />
    </linearGradient>
  </defs>

  <style>
    .title {{ font-family: Arial, sans-serif; font-size: 32px; font-weight: bold; fill: #1f2937; }}
    .main-box {{ font-family: Arial, sans-serif; font-size: 18px; font-weight: 600; fill: #374151; }}
    .cat-title {{ font-family: Arial, sans-serif; font-size: 18px; font-weight: bold; fill: white; }}
    .cat-desc {{ font-family: Arial, sans-serif; font-size: 12px; fill: white; opacity: 0.9; }}
    .card-title {{ font-family: Arial, sans-serif; font-size: 13px; font-weight: bold; fill: #1f2937; }}
    .card-item {{ font-family: Arial, sans-serif; font-size: 11px; fill: #4b5563; }}
    .connector {{ stroke: #9ca3af; stroke-width: 2.5; stroke-linecap: round; stroke-linejoin: round; fill: none; }}
  </style>
'''

out.append(svg_header())

# Title + central box
out.append(f'  <text x="1000" y="80" class="title" text-anchor="middle">{title}</text>')
out.append('  <!-- Central Question -->')
out.append('  <rect x="700" y="120" width="600" height="80" fill="#f3f4f6" stroke="#d1d5db" stroke-width="3" rx="15" filter="url(#shadow)"/>')
out.append(f'  <text x="1000" y="170" class="main-box" text-anchor="middle">{central}</text>')
out.append('')

# Arrow routing
central_x = 1000
central_y = 200
LINE_SPACING = 10
TRUNK_COLOR = "6b7280"

arrow_paths = []
arrow_endpoints = []

for row_num in sorted(rows.keys()):
    row_cats = rows[row_num]
    num_in_row = len(row_cats)
    first_box_y = row_cats[0]['y']
    trunk_y = first_box_y - 40

    for pos_in_row, cat in enumerate(row_cats):
        idx = categories.index(cat)
        tx = cat['center_x']
        ty = cat['y']
        cat_left = cat['x']
        cat_right = cat['x'] + cat['width']
        cat_height = cat.get('height', DEFAULT_CATEGORY_HEIGHT)
        
        colors = ["blue", "purple", "green", "red"]
        arrow_color = colors[idx % len(colors)]
        color_map = {"blue": "1e3a8a", "green": "166534", "purple": "6b21a8", "red": "991b1b"}
        stroke_color = color_map[arrow_color]
        
        if num_in_row == 1:
            entry_x = tx
            entry_y = ty - LINE_SPACING
            path = f'M{central_x},{central_y} L{central_x},{trunk_y} L{entry_x},{trunk_y} L{entry_x},{entry_y}'
        elif pos_in_row == 0:
            entry_x = cat_left - LINE_SPACING
            entry_y = ty + (cat_height / 3)
            path = f'M{central_x},{central_y} L{central_x},{trunk_y} L{entry_x},{trunk_y} L{entry_x},{entry_y}'
        elif pos_in_row == num_in_row - 1:
            entry_x = cat_right + LINE_SPACING
            entry_y = ty + (cat_height / 3)
            path = f'M{central_x},{central_y} L{central_x},{trunk_y} L{entry_x},{trunk_y} L{entry_x},{entry_y}'
        else:
            entry_x = tx
            entry_y = ty - LINE_SPACING
            path = f'M{central_x},{central_y} L{central_x},{trunk_y} L{entry_x},{trunk_y} L{entry_x},{entry_y}'
        
        arrow_paths.append((path, stroke_color, arrow_color))
        arrow_endpoints.append((entry_x, entry_y, stroke_color))

# Draw arrows behind boxes
out.append('  <!-- Connectors -->')
for path, stroke_color, arrow_color in arrow_paths:
    out.append(f'  <path class="connector" d="{path}" stroke="#{stroke_color}" stroke-width="2.5" stroke-linecap="round"/>')

# Draw endpoint dots
out.append('  <!-- Endpoint dots -->')
for end_x, end_y, color in arrow_endpoints:
    out.append(f'  <circle cx="{end_x}" cy="{end_y}" r="3.5" fill="#{color}"/>')
out.append('')

# Draw categories with nested cards
for idx, cat in enumerate(categories):
    cx = cat['x']
    cy = cat['y']
    cw = cat['width']
    ch = cat.get('height', DEFAULT_CATEGORY_HEIGHT)
    
    cat_name = cat["name"].replace("&", "&amp;")
    colors = ["blue", "purple", "green", "red"]
    cat_color = colors[idx % len(colors)]
    
    out.append(f'  <!-- CATEGORY: {cat_name} -->')
    out.append('  <g transform="translate({},{})">'.format(int(cx), int(cy)))
    out.append(f'    <rect x="0" y="0" width="{cw}" height="{ch}" fill="url(#{cat_color}Grad)" rx="15" filter="url(#shadow)"/>')
    out.append(f'    <text x="{int(cw/2)}" y="30" text-anchor="middle" class="cat-title">{cat_name}</text>')
    
    if cat["desc"]:
        desc = cat["desc"].replace("&", "&amp;")
        out.append(f'    <text x="{int(cw/2)}" y="50" text-anchor="middle" class="cat-desc">{desc}</text>')
    
    # Draw nested subcategory cards
    card_x = CARD_PAD
    for subcat in cat["subcategories"]:
        out.append(f'    <!-- Subcategory Card: {subcat["title"]} -->')
        out.append(f'    <g transform="translate({card_x},{CARD_VERTICAL_OFFSET})">')
        out.append(f'      <rect x="0" y="0" width="{CARD_W}" height="{CARD_H}" fill="white" rx="8" filter="url(#shadow)"/>')
        
        subcat_title = subcat["title"].replace("&", "&amp;")
        out.append(f'      <text x="{int(CARD_W/2)}" y="20" text-anchor="middle" class="card-title">{subcat_title}</text>')
        
        # Items
        out.append(f'      <text x="10" y="40" class="card-item">')
        for item_idx, item in enumerate(subcat['items']):
            dy = "0" if item_idx==0 else "17"
            item_escaped = item.replace("&", "&amp;")
            out.append(f'        <tspan x="10" dy="{dy}">• {item_escaped}</tspan>')
        out.append('      </text>')
        out.append('    </g>')
        
        card_x += CARD_W + CARD_GAP
    
    out.append('  </g>')
    out.append('')

# Add footer with date and attribution
footer_date = datetime.now().strftime('%A, %b %d, %Y')
footer_y = CANVAS_H - 30
out.append('  <!-- Footer -->')
out.append(f'  <text x="1000" y="{footer_y}" text-anchor="middle" style="font-family: Arial, sans-serif; font-size: 10px; fill: #9ca3af;">')
out.append(f'    {footer_date}  |  Crafted by Varada with help from intelligence (the real, artificial, and somewhere in the kind)')
out.append('  </text>')
out.append('')

out.append('</svg>')

svg_content = "\n".join(out)
outfile = infile.parent / "ai-taxonomy-from-md.svg"
outfile.write_text(svg_content, encoding="utf-8")
print(f"Wrote {outfile.name}")
