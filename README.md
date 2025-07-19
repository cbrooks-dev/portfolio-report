
# 📈 Portfolio Report

**Portfolio Report** is a Python tool that automatically generates a **daily investment summary email** based on a user's portfolio and sends it directly to their inbox. Ideal for investors who want regular updates without logging into a platform.

---

## ✅ Features

- Sends daily portfolio reports via email  
- Supports any asset with ticker symbol  
- Easy setup using a CSV-based portfolio input  
- Secure with environment variable configuration  
- Easily schedule via cron (Linux/macOS) or Task Scheduler (Windows)

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/portfolio-report.git
cd portfolio-report
```

### 2. Install Required Packages

```bash
pip install -r requirements.txt
```

---

## 🗂️ Portfolio CSV Format

Create a `portfolio.csv` file with **no header**, formatted like this:

```csv
AAPL,10
MSFT,5
TSLA,2
```

- First column: Ticker symbol (e.g., `AAPL`, `MSFT`)  
- Second column: Number of shares owned

---

## 🔐 Encode Portfolio in Base64

Convert your CSV file to base64 so it can be securely stored in the `.env` file.

### Python example:
```python
import base64

with open("portfolio.csv", "rb") as f:
    encoded = base64.b64encode(f.read()).decode()
    print(encoded)
```

Copy the printed base64 string — you’ll paste this into the `.env` file in the next step.

---

## ⚙️ Environment Setup

Create a `.env` file in the root directory with the following content:

```env
SENDER_EMAIL=your_email@gmail.com
SENDER_PASSWORD=your_app_password
RECEIVER_EMAIL=recipient_email@example.com
PORTFOLIO_B64=PASTE_YOUR_BASE64_STRING_HERE
```

### Explanation of variables:

- `SENDER_EMAIL`: Your Gmail or SMTP-compatible email address  
- `SENDER_PASSWORD`: An [App Password](https://support.google.com/accounts/answer/185833) (not your regular email password)  
- `RECEIVER_EMAIL`: The address that should receive daily reports  
- `PORTFOLIO_B64`: The base64-encoded content of your portfolio CSV

---

## 🕒 Automate with a Scheduler

This script is designed to run daily. Here’s how to schedule it:

### Linux/macOS (Cron)

1. Open your crontab:

```bash
crontab -e
```

2. Add this line to run the script every day at 8:00 AM:

```bash
0 8 * * * /usr/bin/python3 /full/path/to/main.py
```

Make sure the path points to your Python installation and script location.

---

### Windows (Task Scheduler)

1. Open **Task Scheduler**  
2. Create a new **Basic Task**  
3. For the **Action**, choose “Start a program”  
4. Set the program/script to your Python executable (e.g. `pythonw.exe`)  
5. Add the path to `main.py` in the “Add arguments” field:
   ```
   C:\path\to\portfolio-report\main.py
   ```

---

## 📬 Example Email Output

Here’s an example of what the email might look like:

**Subject:**  Daily Portfolio Report

```
Total Portfolio Worth: $10762.10 USD
Daily % Increase: 0.10%
Daily $ Increase: $10.51 USD
Daily Best Performer: BTC-USD
```

---

## 🛠️ Future Features (Planned)
  
- ✅ Export daily reports as PDF or Excel  
- ✅ More detailed statistics  
- ✅ Mobile-optimized HTML email layout  
- ✅ Price history and performance tracking over time

---

## 👨‍💻 Contributing

We welcome contributions! Feel free to:

- Fork this repo  
- Submit a pull request  
- Open an issue to suggest new features or improvements

Please follow standard Python style conventions and keep code well-documented.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙌 Acknowledgments

This project was built with Python and a passion for automation, inspired by a desire to simplify portfolio tracking for long-term investors.
