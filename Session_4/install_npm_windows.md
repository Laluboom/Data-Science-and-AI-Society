# Installing Node.js and npm on Windows

This document outlines the steps to install Node.js (which includes npm) on a Windows machine.

## 1. Check for Chocolatey (Optional but Recommended)

Chocolatey is a package manager for Windows, similar to `apt` on Linux or `brew` on macOS. It can simplify software installations.

To check if you have Chocolatey installed, open PowerShell (as Administrator) or Command Prompt and run:

```bash
choco -v
```

If it returns a version number, Chocolatey is installed. If not, you can install it by following the instructions on their official website: [https://chocolatey.org/install](https://chocolatey.org/install)

## 2. Download and Install Node.js

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

## 3. Verify the Installation

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

## 4. If you come across any issues, feel free to contact us in our groupchat!!