## Using Flags with EFPSE

EFPSE can be passed a few different flags to the executable. These flags are as follows:

### Example Flags

1. **Game.exe -console**
    - Command: `"C:/../../Desktop/Projects/Game.exe" -console`
    - Description: Will launch the game with the console open.

2. **Game.exe -data ProjectName**
    - Command: `"C:/../../Desktop/Projects/Game.exe" -data ProjectName`
    - Description: This one works with Game.exe stored in Projects folder. Works the same as "Test Game" function. Preferred method for testing because manual edits of DAT files aren't reset.

3. **Game.exe -map number**
    - Command: `"C:/../../Desktop/Projects/Game.exe" -map 1`
    - Description: Launching your game from exact map number, starts from zero. Same as "Test Current Map".

4. **Multiple Flags**
    - Command: `"C:/../../Desktop/Projects/Game.exe" -console -data ProjectName -map 1`
    - Description: Combining multiple flags in a single command.

## How to Use a Flag: Create a Shortcut

The simplest method to use these flags is to create a shortcut. Follow these step-by-step instructions:

### Step 1: Create a Basic Shortcut

1. **Right-click on the Desktop**: Right-click on any empty space on your desktop.
2. **Select 'New' > 'Shortcut'**: From the context menu, choose "New" and then "Shortcut".
3. **Enter the Path of the Program**: A window will appear asking for the location of the item. Enter the full path of the executable file you want to create a shortcut for. For example:
   ```
   "C:/../../Desktop/Projects/Game.exe"
   ```
4. **Click 'Next'**: After entering the path, click the "Next" button.
5. **Name Your Shortcut**: Enter a name for your shortcut, such as "Launch Game with Console".
6. **Click 'Finish'**: Click the "Finish" button to create the shortcut.

### Step 2: Modify the Shortcut to Accept Command-Line Options

1. **Right-click on the Shortcut**: Locate the shortcut you just created on the desktop, right-click on it, and select "Properties".
2. **Edit the 'Target' Field**: In the "Shortcut" tab, you will see a field labeled "Target". This field will show the path to your program.
3. **Add Command-Line Options**: To pass command-line options, append them to the target path. For example:
   - To open the game with the console:
     ```
     "C:/../../Desktop/Projects/Game.exe" -console
     ```
   - To test with project data:
     ```
     "C:/../../Desktop/Projects/Game.exe" -data ProjectName
     ```
   - To start from a specific map:
     ```
     "C:/../../Desktop/Projects/Game.exe" -map 1
     ```
   - To combine multiple flags:
     ```
     "C:/../../Desktop/Projects/Game.exe" -console -data ProjectName -map 1
     ```
4. **Save Your Changes**: After adding the necessary options, click "Apply" and then "OK" to save your changes.

### Step 3: Using Your Shortcut

1. **Double-click the Shortcut**: Simply double-click the shortcut to run it with the specified command-line options.
2. **Verify the Behavior**: Ensure that the game behaves as expected with the options you provided.

### Additional Tips

- **Environment Variables**: You can use environment variables in the target path, such as `%USERPROFILE%`.
- **Quotes**: If your paths or options contain spaces, enclose them in double quotes. For example:
  ```
  "C:/../../Desktop/Projects/Game.exe" "-data Project Name"
  ```
- **Administrative Rights**: If the program requires administrative rights, you may need to set the shortcut to run as administrator. In the properties window, go to the "Shortcut" tab, click "Advanced...", and check "Run as administrator".

By following these instructions, you can easily create and use a shortcut that passes command-line options to EFPSE in Windows 10 or 11.




## Setting up a command for Powershell 
Creating custom commands in PowerShell to run specific programs with parameters, like `game -data projectName`, involves defining functions and adding them to your PowerShell profile. Here’s how you can set this up:

### Step-by-Step Instructions

1. **Open PowerShell**: Press `Win + R`, type `powershell`, and press Enter.

2. **Check for PowerShell Profile**: First, check if you have a PowerShell profile file. In PowerShell, type:
   ```powershell
   Test-Path $PROFILE
   ```
   If it returns `True`, a profile already exists. If it returns `False`, create one using:
   ```powershell
   New-Item -Path $PROFILE -ItemType File -Force
   ```

3. **Open the Profile File**: Open the profile file in a text editor to add your custom command. Use:
   ```powershell
   notepad $PROFILE
   ```

4. **Define Your Custom Command**: Add a function to the profile file for your custom command. For example:

   ```powershell
   function game {
      param (
         [Parameter(ValueFromRemainingArguments=$true)]
         [string[]]$args
      )
      & "C:\Users\SeltT\OneDrive\Desktop\Projects\Game.exe" @args
   }

   ```

5. **Save and Close**: Save the changes and close the text editor.

6. **Reload Profile**: Reload the profile to apply the changes. In PowerShell, type:
   ```powershell
   . $PROFILE
   ```

### Using Your Custom Command

Now you can use your custom `game` command in PowerShell. Here are a few examples:

- To launch the game with the console:
  ```powershell
  game -console
  ```
- To launch the game with a specific project name:
  ```powershell
  game -data ProjectName
  ```
- To launch the game from a specific map number:
  ```powershell
  game -map 1
  ```


### Using the multiple flags

- To launch the game with multiple flags:
  ```powershell
  game -console -data -map 1
  ```

### Summary

## Disclaimer
AI DISCLAIMER: AI was used to format, arrange, and make edits to the above text

