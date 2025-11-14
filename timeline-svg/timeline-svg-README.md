# Timeline SVG Generator

> EDITS PENDING

[![Version](https://img.shields.io/badge/version-5.1-blue.svg)](https://github.com/ivarada/claude-skills)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)

Generate professional vertical timeline visualizations from YAML configuration files. Creates scalable SVG timelines with customizable date ranges, events, and professional styling.

## Features

✨ **Professional Design**
- Clean vertical timeline layout with hierarchical visual structure
- Color-coded elements (green years, gray months, black events)
- Distinctive dotted lines for events with rounded caps
- Mixed text styling (bold/regular/italic) for rich formatting

📅 **Flexible Configuration**
- Support for any date range (years, decades, centuries)
- Customizable tick spacing and lengths
- YAML-based configuration for easy editing
- Three-part event format (title, description, notes)

🎨 **Automatic Styling**
- Professional header showing timeline date range
- Footer with generation date and custom attribution
- Scalable vector graphics (SVG) for any size
- Embedded styles for self-contained files

🚀 **Easy to Use**
- Simple YAML input format
- Single Python script execution
- No external dependencies beyond PyYAML
- Instant generation for timelines up to 100 years

## Installation

### Prerequisites
- Python 3.6 or higher
- pip (Python package installer)

### Install Dependencies

```bash
pip install pyyaml
```

Or if you're using system Python:

```bash
pip install pyyaml --break-system-packages
```

### Clone Repository

```bash
git clone https://github.com/yourusername/timeline-svg.git
cd timeline-svg
```

## Quick Start

### 1. Create a YAML Configuration File

Create a file named `timeline.yaml`:

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

### 2. Generate the Timeline

```bash
python generate_timeline.py timeline.yaml
```

### 3. View Your Timeline

The script generates an SVG file with the format:
```
timeline-{start_year}-{end_year}-{date}.svg
```

Example: `timeline-2020-2026-2025-11-13.svg`

## Usage

### YAML Configuration Structure

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
- **description**: Main event description (displayed in regular weight)
- **notes**: Additional context (displayed in *italic*, optional)

**Display format:** `Date (bold) - Title (regular) - Description (italic)`

### Configuration Options

#### Timeline Settings

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `start_year` | integer | required | First year on timeline |
| `end_year` | integer | required | Last year on timeline |
| `base_tick_spacing` | integer | 25 | Pixels between ticks |
| `svg_width` | integer | 1000 | Canvas width in pixels |

#### Tick Lengths

| Tick Type | Default | Description |
|-----------|---------|-------------|
| `year` | 100px | Length of year tick marks |
| `month` | 80px | Length of month tick marks |
| `event` | 120px | Length of event tick marks |

#### Event Fields

| Field | Required | Display Style | Description |
|-------|----------|---------------|-------------|
| `date` | Yes | (positioning only) | ISO format: YYYY.MM.DD |
| `title` | Yes | **Bold** | Event identifier/date |
| `description` | No | Regular | Main description |
| `notes` | No | *Italic* | Additional context |

## Examples

### Project Timeline (2023-2025)

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

**Output:** `timeline-2023-2025-2025-11-13.svg`

### Historical Timeline (1990-2000)

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
  
  - date: "1995.08.24"
    title: "Aug 24th"
    description: "Windows 95 released"
    notes: "Microsoft"
```

**Output:** `timeline-1990-2000-2025-11-13.svg`

## Visual Design

### Visual Hierarchy

```
━━━━━━━━━━━━━━━━━━━━  100px  YEAR   (Green, Bold, 18px)
━━━━━━━━━━━━━━━━      80px   MONTH  (Light Gray, 14px)
• • • • • • • • • •   120px  EVENT  (Black, 14px, dotted line)
```

### Typography

- **Year labels**: 18px green bold
- **Month labels**: 14px light gray
- **Event text**: 14px black with mixed styling (bold/regular/italic)
- **Font**: Arial, sans-serif

### Lines

- **Axis**: 3px solid black
- **Year ticks**: 2.5px solid green
- **Month ticks**: 2px solid light gray
- **Event ticks**: 1.5px dotted black with rounded caps

### Header and Footer (v5.1)

Every generated timeline includes:

**Header:**
- Title showing date range: "Timeline - {START_YEAR} - {END_YEAR}"
- Centered at top in 24px bold font
- Professional styling in dark gray (#1f2937)

**Footer:**
- Current date in format: "Wednesday, Nov 14, 2025"
- Custom attribution (configurable in script)
- Styled in light gray (#9ca3af) with 16px font

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

## Troubleshooting

### Issue: Events not showing
**Solution:** Verify date format is exactly `YYYY.MM.DD` and date is within timeline range

### Issue: Text overlapping
**Solution:** Increase `base_tick_spacing` to 30 or 35 pixels

### Issue: SVG too large
**Solution:** Reduce year range or decrease `base_tick_spacing`

### Issue: Timeline too wide
**Solution:** Adjust `svg_width` setting (minimum 800px recommended)

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

## File Structure

```
timeline-svg/
├── README.md              # This file
├── CHANGELOG.md           # Version history
├── LICENSE                # MIT License
├── generate_timeline.py   # Main script
├── requirements.txt       # Python dependencies
└── example_timeline.yaml  # Example configuration
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Inspired by the need for simple, beautiful timeline visualizations
- Built with Python and PyYAML
- Designed for clarity and professional presentation

## Author

**Varada**
- LinkedIn: [ivarada](https://www.linkedin.com/in/ivarada/)

## Support

If you find this project helpful, please give it a ⭐️ on GitHub!

For issues or questions, please open an issue on the [GitHub repository](https://github.com/yourusername/timeline-svg/issues).

---

*Crafted with help from intelligence (the real, artificial, and somewhere in the middle)*
