import re
def classify_with_regex(log_message):
    regex_patterns = {
        r"User User\d+ logged (in|out)": "User action",
        r"Backup (started|ended) at .*": "System notification",
        r"Backup completed successfully.": "System notification",
        r"System updated to version .*": "System notification",
        r"File .* uploaded successfully by user .*": "System notification",
        r"Disk cleanup  completed successfully.": "System notification",
        r"System reboot initiated by user .*": "System notification",
        r"Account with ID .* created by .*": "User Action"
    }
    for pattern, label in regex_patterns.items():
        if re.search(pattern, log_message):
            return label
    return None

if __name__ == "__main__":
    print(classify_with_regex("Backup completed successfully."))
    print(classify_with_regex("Account with ID 1234 created by User1."))
    print(classify_with_regex("Hey Bro, chill ya!"))