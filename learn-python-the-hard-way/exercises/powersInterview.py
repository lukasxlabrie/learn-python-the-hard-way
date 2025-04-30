# Ask if the user is feeling randy
while True:
    randy = input("Do I make you randy, baby? (yes or no) ").strip().lower()
    if randy in ['yes', 'no', 'y', 'n']:
        break
    print("Come again? Just a simple yes or no, baby!")

print("")  # spacing

# Ask if we should shag now or later
while True:
    shag = input("Shall we shag now or shag later? (now or later) ").strip().lower()
    if shag in ['now', 'later']:
        break
    print("Don’t be shy, baby—just say 'now' or 'later'!")

print("")  # spacing

evil = input("Are you working with Dr. Evil? Be honest now: ")

print("")  # spacing

# Summary with responses
print(f"Smashing! So you're feeling {'quite' if randy in ['yes', 'y'] else 'not very'} randy, prefer to shag {shag}, and you're {'not ' if evil.lower() in ['no', 'n'] else ''}working with Dr. Evil.")
print("Yeahhh baby, YEAHHH!")