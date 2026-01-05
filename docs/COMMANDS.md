# Commands

To start the tool after installation it is (DONT use the inverted commas, these were purely used on GitHub to highlight where to put the target IP):

```bash
p-scan "insert target ip address"
```
If the user wanted to do a scan but with Verbose mode, the following command would be:

```bash
p-scan "insert target ip address" -v
```
Finally, if you want to execute a custom port scan you would issue the following command (for this example, I have selected to scan between 7000 - 8000):

```bash
p-scan "insert target ip address" -c 7000 8000
```

Below I have attached a screenshot of the help menu of all the different commands the user can execute.

<img width="413" height="184" alt="Screenshot 2026-01-05 at 21 28 22" src="https://github.com/user-attachments/assets/a02ad8e3-afb8-45d1-98df-afc450446318" />


