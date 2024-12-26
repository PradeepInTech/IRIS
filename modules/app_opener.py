import subprocess
import platform

# Get the operating system name in lowercase
Os = platform.system().lower()

# Dictionary mapping common app names to their Linux executable names
linux_app_names = {
    'firefox': 'firefox',
    'chrome': 'google-chrome', 
    'terminal': 'ptyxis',
    'files': 'nautilus',
    'calculator': 'gnome-calculator',
    'settings': 'gnome-control-center',
    'text editor': 'gedit',
    'code': 'code',
    'spotify': 'spotify'
}

# Dictionary mapping common app names to their Windows executable names
windows_map = {
        'firefox': 'firefox',
        'chrome': 'chrome',
        'terminal': 'cmd', 
        'files': 'explorer',
        'calculator': 'calc',
        'settings': 'ms-settings:',
        'text editor': 'notepad',
        'code': 'code',
        'spotify': 'spotify'
    }

def get_app_map(app_name, Os):
    # Get the OS-specific executable name for the given app
    if Os == "windows":
        if app_name in windows_map:
            os_app = windows_map[app_name]
            return os_app
        else:
            print(f"'{app_name}' is not present in your system")
    else:
        if app_name in linux_app_names:
            os_app = linux_app_names[app_name]
            return os_app
        else:
            print(f"'{app_name}' is not present in your system")

def open_App(app_name):
    # Launch the specified application using the OS-appropriate method
    os_app = get_app_map(app_name)
    print(f"Opening {app_name}...")
    subprocess.Popen(os_app)

def windows_kill_app(os_app):
    # Force close an application on Windows using taskkill
    subprocess.run(['taskkill', '/F', '/IM', f'{os_app}.exe'], capture_output=False)

def linux_kill_app(os_app):
    # Force close an application on Linux using pkill
    subprocess.run(['pkill', '-f', os_app])

def close_App(app_name):
    # Close the specified application using OS-appropriate method
    os_app = get_app_map(app_name)
    if Os == "windows":
        windows_kill_app(os_app)
    else:
        linux_kill_app(os_app)
    print(f"Closing {app_name}...")
