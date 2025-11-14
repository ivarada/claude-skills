---
name: timeline-svg
description: Generate professional vertical timeline visualizations from YAML configuration files. Creates scalable SVG timelines with customizable date ranges, events, and professional styling.
license: MIT
---

# Additional information
metadata:
  version: 5.1
  author: Timeline SVG Skill
  input_format: timeline.yaml
  output_format: timeline-{start_year}-{end_year}-{date}.svg
  tags:
    - visualization
    - timeline
    - svg
    - graphics
    - project-management
  requirements:
    python: ">=3.6"
    pyyaml: ">=5.1"


# Timeline SVG Generator Skill

## Overview
Generate professional vertical timeline visualizations from YAML configuration files. This skill creates scalable SVG timelines with customizable date ranges, events, and styling.

## Skill Metadata
- **Name**: timeline-svg
- **Version**: 5.1
- **Input**: `timeline.yaml` (YAML configuration file)
- **Output**: `timeline-{start_year}-{end_year}-{today}.svg`
- **Format**: Scalable Vector Graphics (SVG)

## When to Use This Skill

Use this skill when you need to:
- Create visual timelines for projects, events, or historical periods
- Generate professional timeline graphics for presentations or reports
- Visualize date-based data with custom styling
- Produce scalable timeline graphics for any date range

**Trigger phrases:**
- "Create a timeline from 2020 to 2026"
- "Generate a timeline visualization"
- "Make a timeline SVG"
- "Build a project timeline"

## Input Format

### YAML Structure
The skill expects a YAML file named `timeline.yaml` with the following structure:

```yaml
timeline:
  start_year: 2020          # Start year of timeline
  end_year: 2026            # End year of timeline
  base_tick_spacing: 25     # Pixels between each tick
  svg_width: 1000           # Canvas width in pixels
  tick_lengths:
    year: 100               # Year tick length (px)
    month: 80               # Month tick length (px)
    event: 120              # Event tick length (px)

events:
  - date: "YYYY.MM.DD"      # ISO date format
    title: "Event Date"     # Displayed in BOLD
    description: "Details"  # Displayed in REGULAR
    notes: "Extra info"     # Displayed in ITALIC (optional)
```

### Event Format
Each event supports three text parts with mixed styling:
- **title**: Date or identifier (displayed in **bold**)
- **description**: Main event description (displayed in regular)
- **notes**: Additional context (displayed in *italic*, optional)

**Display format:** `Date (bold) - Title (regular) - Description (italic)`

## Output Format

### Filename Convention
```
timeline-{start_year}-{end_year}-{date}.svg
```

**Examples:**
- `timeline-2020-2026-2025-11-13.svg`
- `timeline-1970-2070-2025-11-13.svg`
- `timeline-2023-2025-2025-11-13.svg`

### SVG Specifications

**Visual Style:**
```
━━━━━━━━━━━━━━━━━━━━  100px  YEAR   (Green, Bold, 18px)
━━━━━━━━━━━━━━━━      80px   MONTH  (Light Gray, 14px)
• • • • • • • • • •   120px  EVENT  (Black, 14px, dotted line)
```

**Typography:**
- Year labels: 18px green bold
- Month labels: 14px light gray
- Event text: 14px black with mixed styling (bold/regular/italic)
- Font: Arial, sans-serif

**Lines:**
- Axis: 3px solid black
- Year ticks: 2.5px solid green
- Month ticks: 2px solid light gray
- Event ticks: 1.5px dotted black with rounded caps

## Usage Instructions

### Step 1: Prepare Input File
Create a `timeline.yaml` file with your configuration:

```yaml
timeline:
  start_year: 2020
  end_year: 2026
  base_tick_spacing: 25
  svg_width: 1000
  tick_lengths:
    year: 100
    month: 80
    event: 120

events:
  - date: "2025.11.13"
    title: "Nov 13th"
    description: "We are working on a new skill"
    notes: "Timeline project"
  
  - date: "2025.12.01"
    title: "Dec 1st"
    description: "Q4 planning session"
```

### Step 2: Request Generation
Simply say:
- "Generate a timeline from this YAML"
- "Create a timeline visualization"
- "Make me a timeline SVG"

### Step 3: Receive Output
The skill will generate an SVG file with the naming format:
```
timeline-{start_year}-{end_year}-{today}.svg
```

## Features

### Header and Footer (New in v5.1)
Every generated timeline now includes:

**Header:**
- Title showing date range: "Timeline - {START_YEAR} - {END_YEAR}"
- Centered at top in 24px bold font
- Professional styling in dark gray (#1f2937)

**Footer:**
- Current date in format: "Wednesday, Nov 14, 2025"
- Attribution: "Crafted by [Varada](https://www.linkedin.com/in/ivarada/) with help from intelligence (the real, artificial, and somewhere in the middle)"
- Clickable LinkedIn link
- Styled in light gray (#9ca3af) with 16px font

### Visual Hierarchy
1. **Years (Green, 18px)** - Largest, most prominent
2. **Months (Gray, 14px)** - Secondary structure
3. **Events (Black, 14px)** - Content with mixed styling

### Distinctive Event Lines
Events use a dotted line pattern that makes them instantly recognizable:
```css
stroke-dasharray: 1 12;     /* 1px dot, 12px gap */
stroke-linecap: round;      /* Rounded dots */
```

### Mixed Text Styling
Events display with three-part formatting:
- **Bold** text for dates/identifiers
- Regular text for main descriptions
- *Italic* text for additional notes

### Scalable Output
- SVG format scales to any size without quality loss
- Suitable for print and digital use
- Fully compatible with web browsers and design tools

## Examples

### Project Timeline (2023-2025)
**Input:**
```yaml
timeline:
  start_year: 2023
  end_year: 2025
  base_tick_spacing: 25
  svg_width: 1000

events:
  - date: "2023.06.15"
    title: "Q2 2023"
    description: "Project kickoff"
    notes: "Initial planning"
  
  - date: "2024.12.01"
    title: "Q4 2024"
    description: "Product launch"
    notes: "Version 1.0"
```

**Output:**
`timeline-2023-2025-2025-11-13.svg`

### Historical Timeline (1990-2000)
**Input:**
```yaml
timeline:
  start_year: 1990
  end_year: 2000
  base_tick_spacing: 25
  svg_width: 1000

events:
  - date: "1991.08.06"
    title: "Aug 6th"
    description: "World Wide Web announced"
    notes: "Tim Berners-Lee"
```

**Output:**
`timeline-1990-2000-2025-11-13.svg`

## Configuration Options

### Timeline Settings

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `start_year` | integer | required | First year on timeline |
| `end_year` | integer | required | Last year on timeline |
| `base_tick_spacing` | integer | 25 | Pixels between ticks |
| `svg_width` | integer | 1000 | Canvas width in pixels |

### Tick Lengths

| Tick Type | Default | Description |
|-----------|---------|-------------|
| `year` | 100px | Length of year tick marks |
| `month` | 80px | Length of month tick marks |
| `event` | 120px | Length of event tick marks |

### Event Fields

| Field | Required | Display Style | Description |
|-------|----------|---------------|-------------|
| `date` | Yes | (positioning only) | ISO format: YYYY.MM.DD |
| `title` | Yes | **Bold** | Event identifier/date |
| `description` | No | Regular | Main description |
| `notes` | No | *Italic* | Additional context |

## Best Practices

### ✅ Do This
- Use clear, concise event titles (10-25 characters)
- Keep descriptions under 60 characters
- Use notes sparingly for supplementary information
- Space events at least a few days apart
- Use meaningful date formats in titles (e.g., "Nov 13th", "Q4 2025")

### ❌ Avoid This
- Very long text (causes overflow)
- Too many events in same month (creates clutter)
- Spacing less than 20px (text overlap)
- Dates outside the specified year range
- Special characters that break SVG formatting

## Technical Details

### SVG Structure
- **Format**: SVG 1.1 compatible
- **Encoding**: UTF-8
- **Viewport**: Dynamic based on tick count
- **Styling**: Embedded CSS in `<style>` tag

### Performance
- Timelines up to 100 years: Instant generation
- File size: ~2-3 KB per year of timeline
- Browser compatible: All modern browsers

### Color Scheme
- **Green** (`green`): Years - growth and progress
- **Light Gray** (`lightgray`): Months - subtle structure
- **Black** (`black`): Events and axis - high contrast

## Troubleshooting

### Issue: Events not showing
**Solution:** Verify date format is exactly `YYYY.MM.DD` and date is within timeline range

### Issue: Text overlapping
**Solution:** Increase `base_tick_spacing` to 30 or 35 pixels

### Issue: SVG too large
**Solution:** Reduce year range or decrease `base_tick_spacing`

### Issue: Timeline too wide
**Solution:** Adjust `svg_width` setting (minimum 800px recommended)

## Output Examples

### Compact Timeline (7 years)
```
Timeline: 2020-2026
Output: timeline-2020-2026-2025-11-13.svg
Size: ~2,230 pixels height
File: ~30 KB
```

### Full Century Timeline (101 years)
```
Timeline: 1970-2070
Output: timeline-1970-2070-2025-11-13.svg
Size: ~30,430 pixels height
File: ~169 KB
```

## Version History

### v5.1 (Current)
- **Header**: Automatic title showing timeline date range
- **Footer**: Current date and attribution with LinkedIn link
- Professional spacing for header (60px) and footer (80px)
- Clickable attribution link

### v5.0
- Enhanced typography (18px years, 14px events)
- Dotted event lines with rounded caps
- Thicker axis (3px) and month ticks (2px)
- Improved readability and visual hierarchy

### v4.0
- Mixed text styling (bold/regular/italic)
- Three-part event format
- Extended event ticks (120px)

### v3.0
- Green years, gray months, black events
- Single-line event format
- Enhanced color scheme

## Dependencies

**Python packages:**
- `pyyaml` - YAML parsing

**No external dependencies required for SVG generation.**

## License

This skill is provided as-is for creating timeline visualizations.

---

**Skill Type**: File Generation
**Input Format**: YAML
**Output Format**: SVG
**Complexity**: Medium
**Maintenance**: Stable
