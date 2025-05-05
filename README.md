# Discord-Automation-Tool
AutoScriptApp provides a desktop GUI tool for automating tasks involving Discord message parsing and automated input simulation. It is designed to extract Discord messages containing server credentials (e.g., server names and passwords) and automatically input them into another interface.
**AutoScriptApp – Discord Automation Tool Documentation**

---

## Table of Contents

1. Project Overview
2. Key Features
3. Technology Stack & Dependencies
4. Environment Setup
5. Directory & Configuration Files
6. GUI Structure & Design
7. Core Components & Workflow

   * 7.1 Profile Detection
   * 7.2 Auto-Typing Module
   * 7.3 Browser Automation Module
8. Class & Function Descriptions

   * `AutoScriptApp` Class
   * `update_position()`
   * `select_position()`
   * `start_typing()`
   * `start_browser()`
   * `extract_matches()`
9. Regex-Based Discord Data Extraction
10. Data Flow & Event Loop
11. Error Handling & Logging
12. Security Considerations
13. Customization & Extensibility
14. Troubleshooting & FAQs
15. SEO Keywords
16. Author & License

---

## 1. Project Overview

**AutoScriptApp** provides a desktop GUI tool for automating tasks involving **Discord message parsing** and **automated input simulation**. It is designed to extract Discord messages containing server credentials (e.g., server names and passwords) and automatically input them into another interface.

The application uses **Tkinter** and **ttkbootstrap** for GUI, **Selenium** to scrape Discord web content, and **PyAutoGUI** to simulate mouse and keyboard actions.

---

## 2. Key Features

* **Tabbed Interface**: Separate tabs for browser-based Discord scraping, auto-typing configuration, and a control panel.
* **Mouse Position Tracker**: Live display and selection of screen coordinates for auto input.
* **Regex Extraction**: Extracts relevant data (e.g., server name and password) from Discord messages using regex.
* **Uses Chrome Profile**: Loads existing Chrome session to avoid re-login.
* **Custom Regex Input**: User-defined pattern for credential extraction.
* **Automation Loop**: Continuous monitoring of Discord messages.

---

## 3. Technology Stack & Dependencies

* **Python 3.8+**
* **Tkinter** – Built-in Python GUI toolkit
* **ttkbootstrap** – Enhanced theming for Tkinter widgets
* **Selenium** – Web scraping and browser control
* **PyAutoGUI** – Input simulation (keyboard/mouse)
* **Regex** – Credential matching

Install dependencies:

```bash
pip install selenium pyautogui ttkbootstrap
```

---

## 4. Environment Setup

1. **Chrome**: Latest Chrome installed.
2. **Chromedriver**: Compatible version with Chrome browser.
3. **Install Libraries**: As shown above.
4. **Run**:

```bash
python automation_control_panel.py
```

---

## 5. Directory & Configuration Files

```
/AutoScriptApp/
├── automation_control_panel.py   # Main script
├── requirements.txt              # pip dependencies
└── README.md                     # Documentation
```

No external config files required; Chrome user profile is auto-detected.

---

## 6. GUI Structure & Design

* **Window**: 600×600 fixed-size window using the "superhero" theme.
* **Notebook Tabs**:

  * **Browser Automation**: Inputs for Discord URL and regex pattern.
  * **Auto Typing**: Mouse position tracking, click location selection, and text input.
  * **Control Panel**: Table for displaying extracted Discord credentials.

---

## 7. Core Components & Workflow

### 7.1 Profile Detection

Auto-detects user profile to reuse Chrome sessions:

```python
username = getpass.getuser()
profile_path = os.path.join("C:\\Users", username, "AppData\\Local\\Google\\Chrome\\User Data")
```

### 7.2 Auto-Typing Module

* `select_position()` stores X/Y mouse coordinates.
* `start_typing(server_name, password)` automates typing into target fields.

### 7.3 Browser Automation Module

* Launches Chrome via Selenium.
* Loads the specified Discord web URL.
* Applies regex to extract credentials from message content.
* Calls typing function to enter extracted data.

---

## 8. Class & Function Descriptions

### `class AutoScriptApp`

GUI controller class for event handling.

#### `update_position(self)`

Displays real-time mouse coordinates.

#### `select_position(self)`

Captures mouse location and confirms selected position.

#### `start_typing(self, server_name, password)`

Clicks stored location, types server name, tabs, submits, then types password.

#### `start_browser(self)`

Loads Discord, scans message logs, and extracts server credentials using regex.

#### `extract_matches(self, page_source, pattern)`

Uses regex to locate and return matched credential pairs.

---

## 9. Regex-Based Discord Data Extraction

Example regex for Discord messages:

```
Server: (?P<server>[A-Za-z0-9_-]{16})\s+Password: (?P<pass>[A-Za-z0-9@#$%]{8,})
```

This captures messages such as:

```
Server: myDiscordServer1234  Password: sTr0ngP@ss
```

Matches are extracted as `(server_name, password)` and passed to the input automation.

---

## 10. Data Flow & Event Loop

1. User inputs Discord URL and regex.
2. Clicks **Start Browser Automation**.
3. Browser opens and loads Discord.
4. Regex matches credentials from messages.
5. Credentials are typed into the selected input location.
6. Process repeats every 2 seconds.

---

## 11. Error Handling & Logging

* **Missing Input**: Alerts on empty URL or regex.
* **Exceptions**: Displayed using message boxes.
* **Driver Crash**: ChromeDriver gracefully closed after session.
* **Logging**: Add `logging` module for file-based logs if needed.

---

## 12. Security Considerations

* **Regex Safety**: Sanitize patterns to avoid excessive computation.
* **Browser Profile Use**: May expose cookies or tokens.
* **Discord Authentication**: Ensure session is secure.

---

## 13. Customization & Extensibility

* **Control Panel**: Display extracted credentials in a table (code available but commented).
* **Auto Input Logic**: Modify `start_typing()` to fit new workflows.
* **Loop Enhancements**: Add stop/start controls, timeouts, or dynamic intervals.
* **Discord API Support**: Optionally switch to using Discord's API for structured access.

---

## 14. Troubleshooting & FAQs

* **Discord Not Loading**: Ensure user is logged in through Chrome profile.
* **Regex Issues**: Use regex tester tools to verify pattern.
* **Mouse Coordinates**: Use on standard DPI displays for best results.
* **ChromeDriver Mismatch**: Ensure correct version is downloaded.

---

## 15. SEO Keywords

```
Discord automation tool
Extract Discord messages
Python Discord scraper
Discord server credential extractor
GUI Discord bot
regex Discord extractor
selenium Discord automation
pyautogui Discord input
Discord automation tool
Extract Discord messages
Python Discord scraper
Discord server credential extractor
GUI Discord bot
regex Discord extractor
selenium Discord automation
pyautogui Discord input
```

---

## 16. Author & License

**Author:** Smaron Biswas
**Date:** 2025
**License:** MIT License

This tool is intended for ethical and legitimate use only. Modify and expand it as per your Discord automation needs.
