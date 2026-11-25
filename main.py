import os

LINE = ("fix: the bug was mine. i wrote it at 2am, found it at 3am, and at 4am i am quietly merging the evidence away")


def main():
    try:
        os.makedirs("/output", exist_ok=True)
    except OSError:
        pass
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
