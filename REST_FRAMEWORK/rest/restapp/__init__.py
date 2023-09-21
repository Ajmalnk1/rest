import subprocess


def get_wifi_passwords():
    try:
        output = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('cp1252')
        profiles = [line.split(':')[1].strip() for line in output.split('\n') if 'All User Profile' in line]
        passwords = []

        for profile in profiles:
            try:
                password_output = subprocess.check_output(
                    ['netsh', 'wlan', 'show', 'profiles', profile, 'key=clear']).decode('cp1252')
                password_lines = [line.split(':')[1].strip() for line in password_output.split('\n') if
                                  'Key Content' in line]

                if len(password_lines) > 0:
                    passwords.append((profile, password_lines[0]))
            except subprocess.CalledProcessError:
                continue

        return passwords
    except subprocess.CalledProcessError:
        return None


saved_passwords = get_wifi_passwords()

if saved_passwords:
    for profile, password in saved_passwords:
        print(f"Wi-Fi network: {profile}")
        print(f"Password: {password}")
        print()
else:
    print('Unable To Retrieve Saved Wi-Fi Password')

result = []
for a in range(10000):
    for b in range(10000):
        if (a + b) % 11 == 0:
            result.append((a, b))
