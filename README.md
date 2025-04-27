# Mouse Action Recorder and Replayer

## 1. Introduction and Purpose

### Introduction
This program allows users to **record their mouse clicks** and **play them back in an infinite loop**. It captures the mouse click positions and the mouse button used (left or right) during recording, and accurately replays the sequence.

### Purpose & Problem Statement
The code addresses the need for users who want to automate repetitive mouse clicking tasks, such as filling out forms, testing applications, or gaming actions without manual intervention.

### Value Proposition
Users can easily record their actions and automate mouse clicking without writing complex scripts or purchasing expensive automation software.

---

## 2. Dependencies (Required Software/Libraries)

The program requires the following:

### 1. Python

- **Name:** Python  
- **Description:** The programming language used to run the script.
- **Installation Instructions:**  
  Download and install Python from the official website: [https://python.org](https://python.org).

### 2. `pynput` Library

- **Name:** pynput  
- **Description:** Enables programmatic control and monitoring of mouse and keyboard input.
- **Installation Instructions:**  
  Open the terminal or command prompt and run:
  ```bash
  pip install pynput
  ```

> **Note:** If `pip` is not recognized, install it following [these instructions](https://pip.pypa.io/en/stable/installation/).

---

## 3. Getting Started (Installation & Execution)

Follow these simple steps to download and run the program:

### Download the Code

1. Click the green **`<> Code`** button on the GitHub repository page.
2. Select **Download ZIP**.
3. Extract the downloaded ZIP file to a folder of your choice.

### Running the Program

1. Open your terminal (macOS/Linux) or Command Prompt (Windows).
2. Navigate to the folder where you extracted the files using the `cd` command. Example:
   ```bash
   cd path\to\your\folder
   ```
3. Run the program by typing:
   ```bash
   python main.py
   ```
   > Replace `main.py` with the correct filename if it is different.

---

## 4. User Guide (How to Effectively Use the Program)

### How to Record Mouse Actions

- Press **`r`** on your keyboard to start recording.
- Perform the mouse clicks you want to record.
- Press **`Esc`** to stop recording.

### How to Playback Recorded Actions

- After recording, press **`p`** to start an infinite playback loop.
- The mouse will move and click automatically following the recorded sequence.
- Press **`Esc`** to stop the playback loop.

### How to Quit the Program

- Press **`q`** at any time to fully exit the program.

---

## 5. Use Cases and Real-World Examples

### Use Case 1: Form Filling Automation

**Scenario:**  
A user needs to click multiple buttons in a web form repeatedly for testing purposes.

**Example:**  
- Record clicks on each form field.
- Play the sequence back endlessly to test input fields automatically.

---

### Use Case 2: Repetitive Gaming Tasks

**Scenario:**  
A gamer wants to automate resource collection in a click-heavy game.

**Example:**  
- Record mouse clicks where resources appear.
- Enable infinite looping to continuously collect resources.

---

### Use Case 3: Software Testing

**Scenario:**  
A tester needs to simulate user interaction to stress-test an application’s mouse input handling.

**Example:**  
- Record the sequence of mouse clicks on key app areas.
- Replay the recorded actions infinitely to simulate user activity.

---

## 6. Disclaimer & Important Notices

- The repository and its contents may be updated at any time without notice.
- Such updates may render parts of this README file obsolete.
- No commitment is made to maintain or update this README to reflect future changes.
- The provided code is delivered "as-is," without any guarantees regarding functionality, reliability, compatibility, or correctness.
