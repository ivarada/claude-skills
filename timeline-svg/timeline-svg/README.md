# Timeline SVG Generator Skill

Generate professional vertical timeline visualizations from YAML configuration files.

## Quick Start

### 1. Create Your Configuration

Create a `timeline.yaml` file:

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
```

### 2. Generate Timeline

```bash
python3 generate_timeline.py timeline.yaml
```

### 3. Get Your SVG

Output file: `timeline-2020-2026-2025-11-13.svg`

## Features

✅ **Professional styling** with green years, gray months, black events
✅ **Dotted event lines** for clear visual distinction
✅ **Mixed text styling** (bold/regular/italic)
✅ **Scalable SVG** output for any use case
✅ **Automatic filename** with date range and generation date

## Visual Style

```
━━━━━━━━━━━━━━━━━━━━  Year (Green, Bold, 18px)
━━━━━━━━━━━━━━━━      Month (Gray, 14px)
• • • • • • • • • •   Event (Black, 14px, dotted)
                       Date (bold) - Title (regular) - Notes (italic)
```

## Files

- `SKILL.md` - Complete documentation
- `generate_timeline.py` - Main generator script
- `example_timeline.yaml` - Example configuration
- `README.md` - This file

## Requirements

- Python 3.6+
- PyYAML (`pip install pyyaml`)

## Version

5.0 - Enhanced readability with dotted events

## License

Free to use for timeline visualization projects.
