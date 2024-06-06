frame 11 0.25 0 0 0 HUDIMG test .25 .25 1 HUD/timer$map.doublePointsTimer.png 1
frame 11 0.25 0 0 0 HUDIMG test .25 .25 1 HUD/HP.png 1

"C:/Users/SeltT/OneDrive/Desktop/Projects/Game.exe"


function efpse {
    param (
        [string]$Version,
        [string]$EditorVersion,
        [switch]$Editor,
        [Parameter(ValueFromRemainingArguments=$true)]
        [string[]]$Args
    )

    if ($Editor) {
        switch ($EditorVersion.ToLower()) {
            "1.10.4" {
                $EditorPath = "C:/Users/SeltT/OneDrive/Desktop/EasyFPSEditor_CE.exe"  # Change this path to your editor executable path for version 1
            }
            "1.11 alpha 8" {
                $EditorPath = "C:/Users/SeltT/Documents/!EFPSEversions/1.11 alpha 8/EasyFPSEditor_CE_DEV_2024-06-04_2008.exe"  # Change this path to your editor executable path for version 2
            }
            default {
                Write-Host "Invalid editor version specified"
                return
            }
        }
        $Executable = $EditorPath
    }
    else {
        switch ($Version.ToLower()) {
            "1.10.4" {
                $GamePath = "C:/Users/SeltT/OneDrive/Desktop/Projects/Game.exe"  # Change this path to your game executable path for version 1
            }
            "1.11 alpha 8" {
                $GamePath = "C:/Users/SeltT/Documents/!EFPSEversions/1.11 alpha 8/Projects/Game.exe"  # Change this path to your game executable path for version 2
            }
            default {
                Write-Host "Invalid game version specified"
                return
            }
        }
        $Executable = $GamePath
    }

    $Command = "$Executable"
    if ($Args) {
        $Command += " $($Args -join ' ')"
    }
    Write-Host "Executing command: $Command"

    Invoke-Expression $Command
}
