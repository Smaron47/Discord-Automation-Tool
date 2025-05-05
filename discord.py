import os
import getpass
import time
import pyautogui
import tkinter as tk
from tkinter import ttk, messagebox
import ttkbootstrap as tb
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import re
from bs4 import BeautifulSoup

pyautogui.FAILSAFE = False

# Auto-detect Chrome user profile path
username = getpass.getuser()
profile_path = os.path.join("C:\\Users", username, "AppData\\Local\\Google\\Chrome\\User Data")

# GUI Class
class AutoScriptApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Automation Control Panel")
        self.root.geometry("600x600")
        self.root.resizable(False, False)
        self.style = tb.Style("superhero")

        # Variables
        self.url_var = tk.StringVar()
        self.format_var = tk.StringVar()
        self.server_name_var = tk.StringVar()
        self.password_var = tk.StringVar()
        self.search_var = tk.StringVar()
        self.selected_x = tk.IntVar(value=0)
        self.selected_y = tk.IntVar(value=0)

        # ---- Title ----
        tb.Label(root, text="Automation Tool", font=("Helvetica", 18, "bold")).pack(pady=10)

        # ---- Tabs ----
        self.tabs = tb.Notebook(root)
        self.browser_tab = tb.Frame(self.tabs)
        self.typing_tab = tb.Frame(self.tabs)
        self.control_tab = tb.Frame(self.tabs)
        self.tabs.add(self.browser_tab, text="Browser Automation")
        self.tabs.add(self.typing_tab, text="Auto Typing")
        self.tabs.add(self.control_tab, text="Control Panel")
        self.tabs.pack(expand=1, fill="both")

        # ---- Browser Automation Tab ----
        tb.Label(self.browser_tab, text="Login URL:", font=("Arial", 11)).pack()
        tb.Entry(self.browser_tab, textvariable=self.url_var, width=50).pack(pady=5)

        tb.Label(self.browser_tab, text="Format for Server Name/Password (Regex):", font=("Arial", 11)).pack()
        tb.Entry(self.browser_tab, textvariable=self.format_var, width=50).pack(pady=5)

        tb.Button(self.browser_tab, text="Start Browser Automation", bootstyle="success", command=self.start_browser).pack(pady=10)


        # ---- Control Panel Tab ----
        self.table_frame = tb.Frame(self.control_tab)
        self.table_frame.pack(pady=10)

        self.table = ttk.Treeview(self.table_frame, columns=("Server Name", "Username", "Password"), show="headings")
        self.table.heading("Server Name", text="Server Name")
        self.table.heading("Username", text="Username")
        self.table.heading("Password", text="Password")
        self.table.pack(fill="both", expand=True)

        tb.Button(self.control_tab, text="Start All", bootstyle="success", command=self.start_all).pack(pady=10)




        # ---- Control Panel Tab ----
        tb.Label(self.typing_tab, text="Move your mouse to track position", font=("Arial", 11)).pack()
        self.position_label = tb.Label(self.typing_tab, text="Current Mouse Position: 0, 0", font=("Arial", 10))
        self.position_label.pack()
        
        self.selected_x1 = tk.IntVar()
        self.selected_y1 = tk.IntVar()
        self.selected_x2 = tk.IntVar()
        self.selected_y2 = tk.IntVar()
        self.selected_x3 = tk.IntVar()
        self.selected_y3 = tk.IntVar()
        
        tb.Button(self.typing_tab, text="Select Click Position 1", bootstyle="primary", command=lambda: self.select_position(1)).pack(pady=2)
        tb.Button(self.typing_tab, text="Select Click Position 2", bootstyle="primary", command=lambda: self.select_position(2)).pack(pady=2)
        tb.Button(self.typing_tab, text="Select Click Position 3", bootstyle="primary", command=lambda: self.select_position(3)).pack(pady=2)
        
        input_frame = tb.Frame(self.typing_tab)
        input_frame.pack(pady=5)
        
        self.create_position_inputs(input_frame, "X1", self.selected_x1, 0, 0)
        self.create_position_inputs(input_frame, "Y1", self.selected_y1, 0, 2)
        self.create_position_inputs(input_frame, "X2", self.selected_x2, 1, 0)
        self.create_position_inputs(input_frame, "Y2", self.selected_y2, 1, 2)
        self.create_position_inputs(input_frame, "X3", self.selected_x3, 2, 0)
        self.create_position_inputs(input_frame, "Y3", self.selected_y3, 2, 2)
        
        tb.Label(self.typing_tab, text="Server Name:", font=("Arial", 11)).pack()
        self.server_name_var = tk.StringVar()
        tb.Entry(self.typing_tab, textvariable=self.server_name_var, width=40).pack(pady=5)
        
        tb.Label(self.typing_tab, text="Password:", font=("Arial", 11)).pack()
        self.password_var = tk.StringVar()
        tb.Entry(self.typing_tab, textvariable=self.password_var, width=40).pack(pady=5)
        
        tb.Button(self.typing_tab, text="Start Typing", bootstyle="success", command=self.start_typing).pack(pady=10)
    
    def create_position_inputs(self, frame, label, var, row, col):
        tb.Label(frame, text=label, width=5).grid(row=row, column=col)
        tb.Entry(frame, textvariable=var, width=10).grid(row=row, column=col+1)
    
    def select_position(self, pos):
        x, y = pyautogui.position()
        if pos == 1:
            self.selected_x1.set(x)
            self.selected_y1.set(y)
        elif pos == 2:
            self.selected_x2.set(x)
            self.selected_y2.set(y)
        elif pos == 3:
            self.selected_x3.set(x)
            self.selected_y3.set(y)
        self.position_label.config(text=f"Current Mouse Position: {x}, {y}")
    # ---- Update Mouse Position Live ----
    def update_position(self):
        x, y = pyautogui.position()
        self.position_label.config(text=f"Current Mouse Position: {x}, {y}")
        self.root.after(100, self.update_position)
    def start_typing(self):
        server_name = self.server_name_var.get()
        password = self.password_var.get()
        
        x1, y1 = self.selected_x1.get(), self.selected_y1.get()
        x2, y2 = self.selected_x2.get(), self.selected_y2.get()
        x3, y3 = self.selected_x3.get(), self.selected_y3.get()
        
        pyautogui.click(x1, y1)
        pyautogui.click(x1, y1)
        pyautogui.write(server_name)
        time.sleep(0.1)
        pyautogui.click(x2, y2)
        pyautogui.write(password)
        pyautogui.click(x3, y3)
        time.sleep(0.1)
        pyautogui.click(x3, y3)
    def start_typing1(self,server_name,password):

        
        x1, y1 = self.selected_x1.get(), self.selected_y1.get()
        x2, y2 = self.selected_x2.get(), self.selected_y2.get()
        x3, y3 = self.selected_x3.get(), self.selected_y3.get()
        
        pyautogui.click(x1, y1)
        pyautogui.click(x1, y1)
        time.sleep(0.1)
        pyautogui.write(server_name)
        time.sleep(0.1)
        pyautogui.click(x2, y2)
        pyautogui.write(password)
        time.sleep(0.1)
        pyautogui.click(x3, y3)
        pyautogui.click(x3, y3)

    # ---- Start Browser Automation ----
    def start_browser(self):
        chrome_options = Options()
        chrome_options.add_argument(f"user-data-dir={profile_path}")  # Use existing Chrome profile
        chrome_options.add_argument("--profile-directory=Default")  # Load Default profile
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])  # Remove bot warning
        chrome_options.add_experimental_option("useAutomationExtension", False)

        driver = webdriver.Chrome(options=chrome_options)
        processed_entries = set()  # Store already processed entries

        try:
            url = self.url_var.get()
            search_format = self.format_var.get()

            if not url or not search_format:
                messagebox.showerror("Error", "Please enter a URL and format")
                return

            driver.get(url)
            time.sleep(5)  # Wait for page to load

            regex = self.detect_regex(search_format)

            # **Initial Scan: Collect all existing matches at start**
            page_source = driver.page_source
            initial_matches = self.extract_matches(page_source, regex)
            processed_entries.update(initial_matches)  # Store all initially found matches

            while True:
                page_source = driver.page_source
                server_name_passwords = self.extract_matches(page_source, regex)

                new_entries = [entry for entry in server_name_passwords if entry not in processed_entries]

                if new_entries:  # If new entries are found, process them
                    for server_name, username, password in new_entries:
                        self.update_table(server_name, username, password)
                        self.start_typing1(server_name, username)
                        processed_entries.add((server_name, username, password))  # Mark as processed

                time.sleep(2)  # Wait before checking again

        except Exception as e:
            messagebox.showerror("Error", str(e))
        finally:
            driver.quit()



    # ---- Detect Regex Automatically Based on Input Format ----
    def detect_regex(self, format_string):
        # Adjust regex based on the input format
        if re.match(r"[a-f0-9\-]+\.nakama-\d+", format_string):
            return r"([a-f0-9\-]+\.nakama-\d+)"
        elif re.match(r"\d{17}", format_string):
            return r"(\d{17})"
        else:
            raise ValueError("Unsupported format")



    # ---- Extract Matches Based on Format ----
    def extract_matches(self, page_source, pattern):
        # Convert the page source to plain text
        plain_text = self.get_plain_text(page_source)
        
        matches = []
        regex = re.compile(pattern)
        found = regex.findall(plain_text)

        for match in found:
            # Extract text after the match to get the next line's username
            next_line = self.get_next_line(plain_text, match)
            matches.append((match, next_line, match))  # Server Name, Username, Password
        return matches

    # ---- Get the Plain Text from HTML ----
    def get_plain_text(self, page_source):
        """
        This function uses BeautifulSoup to convert the page source (HTML) into plain text
        by stripping out all the HTML tags.
        """
        soup = BeautifulSoup(page_source, "html.parser")
        return soup.get_text(separator='\n')  # Using newline as separator to retain line breaks

    # ---- Get the Next Line of Text ----
    def get_next_line(self, plain_text, match):
        """
        This function searches the plain text for the matched text and returns the 
        next line, which is assumed to be the username.
        """

        # Find the position of the match in the plain text
        match_position = plain_text.find(match)

        if match_position == -1:
            return "Username not found"  # If the match is not found

        # Extract the next line after the match
        # We'll extract a chunk of text starting from the match and look for the next line
        next_line_start = plain_text.find('\n', match_position) + 1
        next_line_end = plain_text.find('\n', next_line_start)

        # Get the text in the next line (the username)
        next_line = plain_text[next_line_start:next_line_end].strip()

        # If no username is found, we will return a default message
        return next_line if next_line else "Username not found"


    # ---- Update Table with New Matches ----
    def update_table(self, server_name, username, password):
        self.table.insert('', 'end', values=(server_name, username, password))

    # ---- Start All ----
    def start_all(self):
        self.start_browser()

# ---- Run the Application ----
if __name__ == "__main__":
    root = tb.Window(themename="darkly")
    app = AutoScriptApp(root)
    root.mainloop()
