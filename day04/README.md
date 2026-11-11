# Day 4 Assignment: p-XRD Bragg Peak Web Application

## Overview
I wrapped my previous crystallographic calculation project (`Bragg.py`) into an interactive web application using **Flask**. I created a server where users can input parameters through a web interface and instantly compute powder X-ray diffraction (PXRD) Bragg peaks.

## What Was Done
1. **Repository Structure:** Created a dedicated `day04` folder, keeping the previous `day03` implementation completely intact.
2. **Backend Logic (`app.py` & `Bragg.py`):** 
   * Adapted the core mathematical functions from the previous script to process inputs dynamically via HTTP requests.
   * Computed crystal lattice parameters, $d$-spacings, and calculated $2\theta$ angles based on Miller indices ($h, k, l$) and experimental values.
3. **Frontend Interface (`templates/index.html`):** 
   * Designed a responsive HTML/CSS form that lets users input custom Miller indices and experimental $2\theta$ values directly in the browser.
   * Integrated Jinja2 templating to render computed results and comparisons dynamically in a clean HTML table.

## How to Run the Application

1. Open your terminal and navigate to the `day04` folder:
   ```bash
   cd day04

## AI prompts:
Ask gemini:
* show steps and codes for assignment day 4. my code from the previous project is called "Bragg.py" and my csv file with the data is called "diffraction_data.csv"
* this is my bragg.py code: (INSERTED COPIED CODE)
* there's a problem in the app.py file (TOLD ME TO INSTALL FLASK IN TERMINAL) [Day 04 Screenshot 1](Picture1.png)
 
* shows the next error:
 [Day 04 Screenshot 2](Picture2.png)
* this is what happened 
* how do i open a new terminal in day04
* this is what it showed: 
* this is what happend (SHARED MY TAB OG THE WEBITE.THERE WAS ERRORTYPE)
* can I change it so instead of using my csv file i can fill my own data trhough the website?
* this is what happened when i clicked calculate (SHARED TAB WITH ASK GEMINI)
* write for the readme what I did
