import subprocess

if __name__ == '__main__':
    while True:
        try:
            # subprocess.run(["/home/str/11astra/.venv/bin/python", "/home/str/11astra/start_all_bot.py"])
            subprocess.run(["/home/str/11astra/.venv/bin/python", r"/home/str/11astra/start_all_bot.py"])
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"Ошибка: {e}")
