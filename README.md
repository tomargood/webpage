# Flask Webpage
#### Video Demo:  https://youtu.be/P7F8MVHU0TY

# Aviation Weather Tool (Flask Project)
This project was built to accomplish two primary goals:
1. Learn Python and web scraping
2. Create a useful, personal tool I could use and improve over time

## Overview
2
The application is a Flask-based web program featuring several static pages and one dynamic tool: an aviation weather checker. This project serves as a personal portfolio to document my journey in learning technology, with the aviation weather tool being the centerpiece of this particular project and this course.

Throughout development, I gained foundational knowledge in:

- Python
- Flask
- HTML
- CSS

## Features

The main tool allows users to input an airport identifier and receive real-time weather data built for pilots. The results are color-coded based on FAA flight conditions:

- **Green**: VFR (Visual Flight Rules). Safe for visual flying.
- **Red**: IFR (Instrument Flight Rules). Low ceilings or poor visibility.
- **Blue**: Marginal VFR, not quite IFR, but not good enough for VFR either.

### Intelligent Ceiling Detection

Not all low clouds constitute a "ceiling." The program intelligently determines when conditions truly impact flight safety by filtering out scattered or few clouds that don’t restrict visual navigation.  Broken or Overcast layers, do, however restrict visual flying

## Purpose

The design and decisions behind this tool were focused on usability for aircrew members needing a quick weather reference when planning flights.

## Future Improvements

Planned features include:

- Ability to check multiple airports at once
- Validation of airport codes and inteligent suggestions on better weather around the location
- Searching for nearby alternate airports based on radius
