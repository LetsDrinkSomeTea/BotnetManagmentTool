# Botnet Management Tool

This project is a Botnet Management Tool developed by LetsDrinkSomeTea for Aalen University.
It Brute Forces a given IP range and tries to connect via SSH. If the connection is successful, the botnet will be able to execute commands on the target machine.

## Educational Purpose

This tool is intended for educational purposes only. It is designed to provide a practical understanding of how botnets work and how they can be managed. It is not intended to be used for malicious purposes. The knowledge gained from this tool should be used responsibly.

## Legal Disclaimer

Unauthorized access to computer systems is illegal under the Computer Fraud and Abuse Act (CFAA) in the United States, the Police and Justice Act 2006 in the United Kingdom, and similar laws in other jurisdictions. This tool is provided for educational purposes only. Any misuse of this tool, including unauthorized access to computer systems, is strictly prohibited and may result in severe civil and criminal penalties.

## Usage

To use this tool, you need to have Python and pip installed on your system. You can then clone this repository and install the required dependencies using pip.

```bash
git clone https://github.com/LetsDrinkSomeTea/BotnetManagementTool.git
cd BotnetManagementTool
pip install -r requirements.txt
```

You can then run the tool using the following command:

```bash
python3 main.py -t num_threads
```

Replace `num_threads` with the number of threads you want to use.



## License

This project is licensed under the MIT License. See the LICENSE file for more details.
