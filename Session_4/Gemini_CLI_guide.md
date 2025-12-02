# Gemini CLI Guide

This guide provides a simplified way to install and use the Gemini CLI.

## Installation

Here are two methods to install the Gemini CLI.

### Method 1: Using `npm` (Node Package Manager)

This is the recommended method for most users.

**Windows:**

1.  Install Node.js from the official website: [https://nodejs.org/](https://nodejs.org/)
2.  Open Command Prompt or PowerShell and run the following command:
    ```bash
    npm install -g @google/gemini-cli
    ```

**macOS:**

1.  Install Node.js. You can use Homebrew for this:
    ```bash
    brew install node
    ```
2.  Open Terminal and run the following command:
    ```bash
    npm install -g @google/gemini-cli
    ```

### Method 2: Manual Installation

This method is for advanced users who want more control over the installation process.

**Windows:**

1.  Download the latest release from the official GitHub repository.
2.  Extract the archive to a directory of your choice.
3.  Add the `bin` directory to your system's `PATH` environment variable.

**macOS:**

1.  Download the latest release from the official GitHub repository.
2.  Extract the archive.
3.  Move the `gemini` binary to a directory in your `PATH`, such as `/usr/local/bin`.

## Verifying Your Installation and Basic Usage

After installation, follow these steps to ensure Gemini CLI is working correctly and to perform a basic login.

### 1. Verify Installation

Open your terminal or command prompt and run:

```bash
gemini --version
```

You should see the installed version of the Gemini CLI. If you get a "command not found" error, refer to the FAQ section.

### 2. Basic Login

The Gemini CLI allows you to log in with your Google account. This process typically opens a browser window for authentication.

Run the following command:

```bash
gemini login
```

Follow the on-screen prompts in your browser to log in with your Google account. Once successful, your terminal will confirm the login.

### 3. Test with a Basic Prompt

Now that you're logged in, you can test if Gemini is working by sending a simple prompt.

```bash
gemini ask "What is the capital of France?"
```

You should receive a response from Gemini with the answer.

## FAQ

**Q: I'm getting a `command not found` error after installation.**

**A:** This usually means that the installation directory is not in your system's `PATH`. Make sure you have added the `bin` directory to your `PATH` environment variable if you used the manual installation method. If you used `npm`, ensure that the `npm` global directory is in your `PATH`.

**Q: I'm getting permission errors when installing with `npm` on macOS.**

**A:** This can happen if you are trying to install the package globally without the necessary permissions. Try running the command with `sudo`:
```bash
sudo npm install -g @google/gemini-cli
```

**Q: How do I update the Gemini CLI?**

**A:** If you installed it using `npm`, you can update it by running:
```bash
npm update -g @google/gemini-cli
```
