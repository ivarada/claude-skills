#!/usr/bin/env python3
"""
Timeline SVG Generator
Generates professional vertical timeline visualizations from YAML configuration

Input: timeline.yaml
Output: timeline-{start_year}-{end_year}-{date}.svg
"""

import yaml
import sys
from datetime import datetime
from pathlib import Path

# Month names
MONTH_NAMES = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
               'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

def load_config(yaml_file):
    """Load configuration and events from YAML file"""
    try:
        with open(yaml_file, 'r') as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        print(f"Error: {yaml_file} not found.")
        return None
    except Exception as e:
        print(f"Error loading YAML: {e}")
        return None

def calculate_tick_position(date_str, start_year):
    """Calculate tick position for a date"""
    try:
        year, month, day = map(int, date_str.split('.'))
        months_from_start = (year - start_year) * 12 + (month - 1)
        day_fraction = (day - 1) / 30.0
        return months_from_start, day_fraction
    except Exception as e:
        print(f"Error parsing date {date_str}: {e}")
        return None, None

def generate_timeline(yaml_file, output_dir='.'):
    """Generate timeline SVG from YAML configuration"""
    
    # Load configuration
    config_data = load_config(yaml_file)
    if not config_data:
        return None
    
    # Extract configuration
    timeline_config = config_data.get('timeline', {})
    START_YEAR = timeline_config.get('start_year', 1970)
    END_YEAR = timeline_config.get('end_year', 2070)
    BASE_TICK_SPACING = timeline_config.get('base_tick_spacing', 25)
    SVG_WIDTH = timeline_config.get('svg_width', 1000)
    
    tick_lengths = timeline_config.get('tick_lengths', {})
    YEAR_TICK_LENGTH = tick_lengths.get('year', 100)
    MONTH_TICK_LENGTH = tick_lengths.get('month', 80)
    EVENT_TICK_LENGTH = tick_lengths.get('event', 120)
    
    AXIS_X = 50
    HEADER_HEIGHT = 60  # Space for header
    STARTING_Y = HEADER_HEIGHT + 15  # Start after header
    FOOTER_HEIGHT = 80  # Space for footer
    
    events = config_data.get('events', [])
    
    print(f"Timeline Generator v5.1")
    print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"Configuration loaded:")
    print(f"  Years: {START_YEAR} to {END_YEAR}")
    print(f"  Events: {len(events)}")
    print(f"  Spacing: {BASE_TICK_SPACING}px")
    print(f"  Width: {SVG_WIDTH}px")
    
    # Build timeline items
    total_years = END_YEAR - START_YEAR + 1
    timeline_items = []
    
    # Add year and month markers
    for year in range(START_YEAR, END_YEAR + 1):
        for month in range(1, 13):
            month_idx = month - 1
            if month == 1:
                timeline_items.append({
                    'type': 'year',
                    'year': year,
                    'month': month,
                    'month_name': MONTH_NAMES[month_idx],
                    'sort_key': (year - START_YEAR) * 12 + month_idx
                })
            else:
                timeline_items.append({
                    'type': 'month',
                    'year': year,
                    'month': month,
                    'month_name': MONTH_NAMES[month_idx],
                    'sort_key': (year - START_YEAR) * 12 + month_idx
                })
    
    # Add events
    for event in events:
        date_str = event.get('date', '')
        month_tick_index, day_fraction = calculate_tick_position(date_str, START_YEAR)
        
        if month_tick_index is not None:
            timeline_items.append({
                'type': 'event',
                'date': date_str,
                'title': event.get('title', ''),
                'description': event.get('description', ''),
                'notes': event.get('notes', ''),
                'sort_key': month_tick_index + day_fraction
            })
    
    # Sort all items
    timeline_items.sort(key=lambda x: x['sort_key'])
    
    # Calculate dimensions
    total_ticks = len(timeline_items)
    total_height = HEADER_HEIGHT + (total_ticks * BASE_TICK_SPACING) + FOOTER_HEIGHT
    
    # Build SVG
    svg_lines = []
    svg_lines.append(f'<svg width="{SVG_WIDTH}" height="{total_height}" xmlns="http://www.w3.org/2000/svg">')
    svg_lines.append(f'  <!-- Timeline: {START_YEAR} to {END_YEAR} -->')
    svg_lines.append(f'  <!-- Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")} -->')
    svg_lines.append(f'  <!-- Total ticks: {total_ticks} -->')
    svg_lines.append('')
    svg_lines.append('  <!-- Background -->')
    svg_lines.append(f'  <rect width="{SVG_WIDTH}" height="{total_height}" fill="white"/>')
    svg_lines.append('')
    svg_lines.append('  <!-- Styles -->')
    svg_lines.append('  <style>')
    svg_lines.append('    .title { font-family: Arial, sans-serif; font-size: 32px; fill: #1f2937; font-weight: bold; }')
    svg_lines.append('    .footer { font-family: Arial, sans-serif; font-size: 16px; fill: #9ca3af; }')
    svg_lines.append('    .footer a { fill: #3b82f6; text-decoration: underline; }')
    svg_lines.append('    .year-label { font-family: Arial, sans-serif; font-size: 18px; fill: green; font-weight: bold; }')
    svg_lines.append('    .month-label { font-family: Arial, sans-serif; font-size: 14px; fill: lightgray; }')
    svg_lines.append('    .event-date { font-family: Arial, sans-serif; font-size: 14px; fill: black; font-weight: bold; }')
    svg_lines.append('    .event-title { font-family: Arial, sans-serif; font-size: 14px; fill: black; font-weight: normal; }')
    svg_lines.append('    .event-desc { font-family: Arial, sans-serif; font-size: 14px; fill: black; font-style: italic; }')
    svg_lines.append('    .year-tick { stroke: green; stroke-width: 2.5; }')
    svg_lines.append('    .month-tick { stroke: lightgray; stroke-width: 2; }')
    svg_lines.append('    .event-tick { stroke: black; stroke-width: 1.5; stroke-dasharray: 1 12; stroke-linecap: round; fill: none; }')
    svg_lines.append('    .axis { stroke: black; stroke-width: 3; }')
    svg_lines.append('  </style>')
    svg_lines.append('')
    
    # Add header
    title_x = SVG_WIDTH / 2
    title_y = 35
    svg_lines.append('  <!-- Header -->')
    svg_lines.append(f'  <text x="{title_x}" y="{title_y}" class="title" text-anchor="middle">Timeline - {START_YEAR} - {END_YEAR}</text>')
    svg_lines.append('')
    
    # Add axis
    axis_end_y = STARTING_Y + (total_ticks * BASE_TICK_SPACING)
    svg_lines.append('  <!-- Main vertical axis -->')
    svg_lines.append(f'  <line x1="{AXIS_X}" y1="{STARTING_Y}" x2="{AXIS_X}" y2="{axis_end_y}" class="axis"/>')
    svg_lines.append('')
    
    # Generate ticks
    svg_lines.append('  <!-- Timeline Ticks -->')
    current_y = STARTING_Y
    
    for item in timeline_items:
        item_type = item['type']
        
        if item_type == 'year':
            year = item['year']
            month_name = item['month_name']
            year_tick_x2 = AXIS_X + YEAR_TICK_LENGTH
            year_label_x = year_tick_x2 + 15
            month_label_x = year_tick_x2 + 70
            
            svg_lines.append(f'  <!-- Year {year} -->')
            svg_lines.append(f'  <line x1="{AXIS_X}" y1="{current_y}" x2="{year_tick_x2}" y2="{current_y}" class="year-tick"/>')
            svg_lines.append(f'  <text x="{year_label_x}" y="{current_y + 5}" class="year-label">{year}</text>')
            svg_lines.append(f'  <text x="{month_label_x}" y="{current_y + 4}" class="month-label">{month_name}.{year}</text>')
            
        elif item_type == 'month':
            year = item['year']
            month_name = item['month_name']
            month_tick_x2 = AXIS_X + MONTH_TICK_LENGTH
            month_label_x = month_tick_x2 + 15
            
            svg_lines.append(f'  <line x1="{AXIS_X}" y1="{current_y}" x2="{month_tick_x2}" y2="{current_y}" class="month-tick"/>')
            svg_lines.append(f'  <text x="{month_label_x}" y="{current_y + 4}" class="month-label">{month_name}.{year}</text>')
            
        elif item_type == 'event':
            date_str = item['date']
            title = item['title']
            description = item['description']
            notes = item.get('notes', '')
            
            event_tick_x2 = AXIS_X + EVENT_TICK_LENGTH
            event_text_x = event_tick_x2 + 15
            
            svg_lines.append(f'  <!-- Event: {date_str} -->')
            svg_lines.append(f'  <line x1="{AXIS_X}" y1="{current_y}" x2="{event_tick_x2}" y2="{current_y}" class="event-tick"/>')
            svg_lines.append(f'  <text x="{event_text_x}" y="{current_y + 5}">')
            svg_lines.append(f'    <tspan class="event-date">{title}</tspan>')
            
            if description:
                svg_lines.append(f'    <tspan class="event-title"> - {description}</tspan>')
            
            if notes:
                svg_lines.append(f'    <tspan class="event-desc"> - {notes}</tspan>')
            
            svg_lines.append(f'  </text>')
        
        current_y += BASE_TICK_SPACING
    
    # Add footer
    footer_y = total_height - 40
    footer_x = SVG_WIDTH / 2
    
    # Get current date in format "Wednesday, Nov 12, 2025"
    now = datetime.now()
    day_name = now.strftime("%A")
    month_name = now.strftime("%b")
    day_num = now.strftime("%d").lstrip('0')  # Remove leading zero
    year = now.strftime("%Y")
    date_str = f"{day_name}, {month_name} {day_num}, {year}"
    
    svg_lines.append('')
    svg_lines.append('  <!-- Footer -->')
    svg_lines.append(f'  <text x="{footer_x}" y="{footer_y}" text-anchor="middle" style="font-family: Arial, sans-serif; font-size: 16px; fill: #9ca3af;">')
    svg_lines.append(f'    {date_str}  |  Crafted by ')
    svg_lines.append(f'    <a href="https://www.linkedin.com/in/ivarada/" target="_new" style="fill: #3b82f6; text-decoration: underline;">Varada</a>')
    svg_lines.append('    with help from intelligence (the real, artificial, and somewhere in the middle)')
    svg_lines.append('  </text>')
    
    svg_lines.append('')
    svg_lines.append('</svg>')
    
    # Generate output filename
    today = datetime.now().strftime("%Y-%m-%d")
    output_filename = f"timeline-{START_YEAR}-{END_YEAR}-{today}.svg"
    output_path = Path(output_dir) / output_filename
    
    # Write file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(svg_lines))
    
    print(f"\n✅ Timeline generated successfully!")
    print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"Output: {output_filename}")
    print(f"Dimensions: {SVG_WIDTH}px × {total_height}px")
    print(f"Total ticks: {total_ticks}")
    print(f"File size: {len('\\n'.join(svg_lines))} bytes")
    
    return str(output_path)

if __name__ == "__main__":
    # Get input file and output directory
    yaml_file = sys.argv[1] if len(sys.argv) > 1 else 'timeline.yaml'
    output_dir = sys.argv[2] if len(sys.argv) > 2 else '.'
    
    # Generate timeline
    result = generate_timeline(yaml_file, output_dir)
    
    if result:
        print(f"\n📄 File ready: {result}")
    else:
        print("\n❌ Timeline generation failed")
        sys.exit(1)
