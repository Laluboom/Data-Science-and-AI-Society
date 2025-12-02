# Installing Node.js and npm on Windows

This document outlines the steps to install Node.js (which includes npm) on a Windows machine. We will cover two methods: using Chocolatey (recommended) and the traditional installer.

## Method 1: Installing Node.js and npm using the Official Installer (Recommended)

You can install Node.js and npm directly using the official installer.

### 1. Download and Install Node.js 

Node.js comes bundled with npm (Node Package Manager).

1.  **Go to the official Node.js website:** Open your web browser and navigate to [https://nodejs.org/en/download/](https://nodejs.org/en/download/)
2.  **Choose the Windows Installer:**
    *   You will see two main options: "LTS" (Long Term Support) and "Current" (latest features). For most users, the **LTS** version is recommended for stability.
    *   Under the "Windows Installer" section, click on the appropriate link for your system (e.g., "Windows Installer (.msi) 64-bit").
3.  **Run the Installer:**
    *   Once the download is complete, run the `.msi` installer file.
    *   Follow the prompts in the installation wizard.
    *   It's generally safe to accept the default settings, especially regarding the installation location and components to install (ensure "npm package manager" is selected, which it is by default).
    *   Click "Next", accept the license agreement, choose the destination folder, and then click "Install".
    *   You may be prompted by User Account Control (UAC) to allow the installer to make changes; click "Yes".
    *   Click "Finish" once the installation is complete.

### 2. Verify the Installation

After the installation is complete, you can verify that both Node.js and npm are correctly installed.

1.  **Open a new Command Prompt or PowerShell window.** (It's important to open a *new* one, as the old one might not have the updated PATH environment variables).
2.  **Check Node.js version:** Type the following command and press Enter:

    ```bash
    node -v
    ```

    This should output the installed Node.js version (e.g., `v18.18.0`).
3.  **Check npm version:** Type the following command and press Enter:

    ```bash
    npm -v
    ```

    This should output the installed npm version (e.g., `9.8.1`).

If both commands return version numbers, Node.js and npm are successfully installed on your system!

## Method 2: Installing Node.js and npm with Chocolatey

If you do not prefer the official installer, for a streamlined and efficient setup on Windows, you can use Chocolatey, a package manager for Windows.

### 1. Install Chocolatey

If you don't have Chocolatey installed, open PowerShell as an administrator and run the following command:

```powershell
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```

After the installation is complete, close and reopen your administrator PowerShell to ensure Chocolatey is in your PATH.

### 2. Install Node.js LTS

With Chocolatey installed, you can now install the Long-Term Support (LTS) version of Node.js. This is the recommended version for most users as it is stable and well-supported.

```powershell
choco install nodejs-lts
```

Chocolatey will handle the download and installation of Node.js and npm.

### 3. Verify the Installation

Once the installation is complete, you can verify that Node.js and npm are installed correctly by running the following commands in your terminal:

```bash
node -v
npm -v
```

These commands should output the installed versions of Node.js and npm, respectively.

### Common Errors and Fixes (Chocolatey Method)

**Error: `choco` is not recognized as an internal or external command...**

*   **Fix:** This error usually means that the Chocolatey installation path is not in your system's PATH environment variable. Close and reopen your terminal. If the issue persists, you may need to add `C:\ProgramData\chocolatey\bin` to your PATH manually.

**Error: The term 'choco' is not recognized as the name of a cmdlet, function, script file, or operable program.**

*   **Fix:** This is the PowerShell equivalent of the previous error. Ensure you have opened a new administrative PowerShell session after installing Chocolatey.

**Error: EACCES: permission denied, access '/usr/local/lib/node_modules'**

*   **Fix:** While more common on Unix-like systems, this can occur on Windows. It indicates that npm does not have the necessary permissions to install packages globally. On Windows, running your terminal as an administrator can often resolve this. Alternatively, you can configure npm to use a different directory for global packages.

**Error: `npm` is not recognized as an internal or external command...**

*   **Fix:** This error indicates that the npm installation directory is not in your PATH. The Chocolatey installation should handle this, but if it fails, you may need to add the npm directory to your PATH. The default location is usually `C:\Program Files\nodejs`.

## If you come across any issues, feel free to contact us in our groupchat or socials!!