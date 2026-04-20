# SCT_CS_4
The system records keystrokes within the application window, masks sensitive inputs, and logs events with timestamps. The data can be exported for analysis while maintaining user privacy.
# 🔐 Safe Key Event Logger (Python & Tkinter)

## 📌 Description

This project is a **Safe Key Event Logger** developed using **Python and Tkinter**. It captures keyboard events **only within the application window** and logs them in a secure and privacy-preserving manner.

This project is part of my **SkillCraft Technology Internship (Task 04)** and focuses on understanding event handling, logging mechanisms, and ethical considerations in cybersecurity.
## 🚀 Features

* ▶️ Start and Stop logging with user consent
* ⌨️ Captures keystrokes within the app only
* 🔐 Masks sensitive input (letters shown as `*`)
* 🕒 Logs each key with timestamp
* 🧹 Clear log functionality
* 📁 Export logs to a file
* 🖥️ User-friendly GUI
## 🛠️ Technologies Used

* Python 3
* Tkinter (GUI Library)
* Datetime module
## 📂 Project Structure

```id="struct04"
safe-key-logger/
│
├── safe_key_logger.py
├── README.md
```
## ▶️ How to Run

1. Install Python (3.x recommended)
2. Open terminal / command prompt
3. Navigate to project folder
4. Run the program:

```id="run04"
python safe_key_logger.py
```
## 💡 How It Works

* The application listens for keyboard events inside the input field
* Logging starts only when the user clicks **Start**
* Each key press is:

  * Masked for privacy (`*`)
  * Timestamped
* Logs are displayed in real-time and can be exported
## 📝 Example

```id="ex04"
Input: Hello123!

Output:
12:10:05 - *
12:10:06 - *
12:10:06 - *
12:10:07 - *
12:10:07 - *
12:10:08 - <1>
12:10:08 - <2>
12:10:09 - <3>
12:10:09 - <!>
```
## 🎯 Applications

* Learning event handling in Python
* Understanding logging systems
* Cybersecurity awareness
* Ethical hacking education

## ⚠️ Ethical Note

This project is designed for **educational purposes only**.
It logs input **only within the application** and ensures user privacy by masking sensitive data. It should not be used for unauthorized monitoring.

## 🔮 Future Enhancements

* Real-time visualization dashboard
* Log encryption for added security
* Multi-user logging system
* Web-based version

## 👨‍💻 Author

Palla Venkata Mahesh
GitHub: https://github.com/palla-mahesh

## 📜 License

This project is licensed under the MIT License.

## ✅ Conclusion

This project demonstrates how keyboard event logging can be implemented in a secure and ethical way. It highlights the importance of user consent, privacy protection, and responsible use of cybersecurity tools. By combining event handling, file management, and GUI development, this project provides a strong foundation for understanding real-world security concepts.

⭐ If you like this project, give it a **star**!
