from rich import print
from rich.console import Console
from rich.text import Text
from rich.theme import Theme
from rich.markdown import Markdown
from rich.prompt import Prompt

import os
import subprocess
import time
import re
import platform
import struct
import jdk

#* IMPORTS

os.system('cls' if os.name == 'nt' else 'clear')
system = platform.system()

customTheme = Theme({
    "success": "green bold italic",
    "error": "red bold italic",
})

MARKDOWN = """
# Kxffie's Github Compiler

## Please make sure you put this EXE in a directory so you can keep track of where the compiled files are.
"""

console = Console(theme=customTheme)
md = Markdown(MARKDOWN)
console.print(md)

#* SETUP

GithubURL = input("Please paste the github link below\n-> ")

# TODO: check if java 17 is installed

console.print("Checking if Java is installed...")
installed = None

#? DOES CORRECT JAVA VERSION EXIST?
try:
    output = subprocess.check_output(['java', '-version'], stderr=subprocess.STDOUT)
    output_str = output.decode()
    version_match = re.search(r'version "(.*?)"', output_str)

    if version_match:
        version = version_match.group(1)
        console.print(f"\nA successful version of Java is present. ([success]{version}[/success])")
        installed = True

        if "17" not in version:
            console.print("\nPlease install Java [success]17[/success] for this program to work.")
            installed = False
    else:
        console.print("\nNo Java Version Found!", style="error")
        console.print("Please install Java [success]17[/success] for this program to work.")
        console.print("[link=https://www.youtube.com/watch?v=-WpG5O9iLtA]YouTube tutorial[/link] for more help.")
        installed = False
except Exception as e:
    console.print("\nNo Java Version Found!", style="error")
    console.print("Please install Java [success]17[/success] for this program to work.")
    console.print("[link=https://www.youtube.com/watch?v=-WpG5O9iLtA]YouTube tutorial[/link] for more help.")
    installed = False
    

#? CHECK IF COMPUTER IS MAC OR LINUX

answer = None
if installed == False:
    if system == 'Darwin':
        print("\nSorry, you are using a [success]MacOS[/success] system. This OS is not supported.")
    elif system == 'Linux':
        print("\nSorry, you are using a [success]Linux[/success] system. This OS is not supported.")
    else:
        print("\nYou might be using Windows.")
        
        if installed == False:
            if struct.calcsize("P") == 4:
                answer = Prompt.ask("I noticed your System is [success]32-bit[/success]. Would you like to semi-automatically install Java 17? [Y/N]")
            elif struct.calcsize("P") == 8:
                answer = Prompt.ask("I noticed your System is [success]64-bit[/success]. Would you like to semi-automatically install Java 17? [Y/N]")
            else:
                print("Unknown system architecture")

#? DOWNLOAD 17JDK

if installed == False:
    if answer.lower() == "y":
        jdk.install('17', path="C:\Program Files\Java")
        console.print("\nJava 17 has been installed.")
        time.sleep(1)
        console.print("Please restart the program to use the new version of Java.")
    else:
        console.print("\nJava 17 was not been installed. Goodbye!")
        input("\nPress any key to exit...")

# TODO: compile the code

def compile_github_link(github_link):
    repo_name = github_link.split('/')[-1].split('.')[0]

    if os.path.exists(repo_name):
        print(f"{repo_name} already exists, skipping clone")
    else:
        try:
            os.system(f"git clone {github_link}")
        except FileNotFoundError:
            print(f"Error: Could not find git command. Make sure Git is installed and in the PATH.")
            return
        except:
            print(f"Error: Could not clone {github_link}")
            return

    os.chdir(repo_name)

    try:
        os.system("gradlew build")
    except FileNotFoundError:
        print(f"Error: Could not find gradlew command. Make sure Gradle is installed and in the PATH.")
        return
    except:
        try:
            os.system("./gradlew build")
        except FileNotFoundError:
            print(f"Error: Could not find gradlew command. Make sure Gradle is installed and in the PATH.")
            return
        except:
            print(f"Error: Could not compile {repo_name}")
            return
    finally:
        print("Compiled successfully! Check the build/libs folder for the jar file. Install it into your Mods folder.")

if installed == True:
    compile_github_link(GithubURL)
    
#* THANKS

MARKDOWN_THANKS = """
# Thanks for using Kxffie's Github Compiler! Checkout my Youtube (https://www.youtube.com/Kxffie) to support me!
"""
thanks = Markdown(MARKDOWN_THANKS)

console.print(thanks)
input("\nPress any key to exit...")