import PyInstaller.__main__

PyInstaller.__main__.run([
    'Clicker.py',  # Replace with your main script filename
    '--onefile',  # Generate a single executable
    '--windowed',  # Hide console (useful for GUI apps)
    '--name=Clicker',  # Set the name of the executable
    '--clean',  # Clean the cache before building
    '--noconfirm',  # Skip confirmation prompts
    '--hidden-import=tkinter',  # Ensure tkinter is bundled
    '--hidden-import=ttkbootstrap',  # Include ttkbootstrap
    '--hidden-import=pyautogui',  # Include pyautogui
    '--hidden-import=selenium',  # Ensure selenium is included
    '--hidden-import=bs4',  # Include BeautifulSoup (bs4)
    '--hidden-import=re',  # Include regex module
    '--hidden-import=os',  # Include os module
    '--hidden-import=getpass',  # Include getpass module
    '--hidden-import=time',  # Include time module
    '--hidden-import=tkinter.ttk',  # Ensure ttk is included
    '--hidden-import=selenium.webdriver.common.by',  
    '--hidden-import=selenium.webdriver.common.keys',  
    '--hidden-import=selenium.webdriver.support.ui',  
    '--hidden-import=selenium.webdriver.support.expected_conditions',  
    '--hidden-import=selenium.webdriver.chrome.options',
])
