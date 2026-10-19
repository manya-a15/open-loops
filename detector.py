# Open Loops - action detector
# ------------------------------------------------------------
# This is the "brain" of the Open Loops feature.
# It reads an email and decides two things:
#   1. Does this email need me to DO something? (an "open loop")
#   2. Is there a deadline in it?
#
# It only uses things from basic Python: lists, loops, if/else.
# In a real product, Gmail would use a machine-learning model,
# but the idea is exactly the same: look for clues in the text.
# ------------------------------------------------------------

# Words that usually mean "you need to take action"
ACTION_WORDS = [
    "register", "submit", "fill", "form", "deadline", "last date",
    "due", "pay", "fee", "apply", "rsvp", "confirm", "upload",
    "before", "by tomorrow", "mandatory", "required",
]

# Month names, so we can spot dates like "24 October" or "Oct 24"
MONTHS = [
    "jan", "feb", "mar", "apr", "may", "jun",
    "jul", "aug", "sep", "oct", "nov", "dec",
]


def find_action_words(text):
    """Return a list of action words found in the email."""
    text = text.lower()
    found = []
    for word in ACTION_WORDS:
        if word in text:
            found.append(word)
    return found


def find_deadline(text):
    """Look for a simple date like '24 Oct' or 'Oct 24'. Return it or None."""
    words = text.lower().replace(",", " ").replace(".", " ").split()
    for i in range(len(words)):
        for month in MONTHS:
            if words[i].startswith(month):
                # number BEFORE the month, e.g. "24 october"
                if i > 0 and words[i - 1].isdigit():
                    return words[i - 1] + " " + month.capitalize()
                # number AFTER the month, e.g. "october 24"
                if i + 1 < len(words) and words[i + 1].rstrip("thndrs").isdigit():
                    return words[i + 1].rstrip("thndrs") + " " + month.capitalize()
    return None


def has_link(text):
    """Forms and payment pages usually come as links."""
    return "http" in text.lower() or "forms.gle" in text.lower()


def check_email(subject, body):
    """Give the email a score. Score 3 or more = open loop."""
    full_text = subject + " " + body
    actions = find_action_words(full_text)
    deadline = find_deadline(full_text)

    score = len(actions)
    if deadline:
        score = score + 2
    if has_link(full_text):
        score = score + 1

    is_open_loop = score >= 3
    return is_open_loop, deadline, actions, score


# ------------------------------------------------------------
# Try it on some sample emails
# ------------------------------------------------------------
emails = [
    {
        "subject": "Hostel fee payment - last date 24 Oct",
        "body": "Dear students, please pay the hostel fee on the portal before 24 October. "
                "Link: https://vtop.example/pay",
    },
    {
        "subject": "Hackathon registrations open!",
        "body": "Register your team using forms.gle/abc123 by Oct 28th. Mandatory for all members.",
    },
    {
        "subject": "Photos from Freshers' Night",
        "body": "Thanks for coming everyone! Here are the photos from last night.",
    },
    {
        "subject": "Weekly newsletter",
        "body": "Here is what happened on campus this week. Have a great weekend!",
    },
]

# Pretend the user opened every email and closed it without doing anything
for email in emails:
    is_loop, deadline, actions, score = check_email(email["subject"], email["body"])
    print("Email:", email["subject"])
    if is_loop:
        print("  -> OPEN LOOP (score", str(score) + ")")
        print("     clues found:", ", ".join(actions))
        if deadline:
            print("     deadline:", deadline, "-> remind 2 days before")
        else:
            print("     no deadline -> remind tonight")
    else:
        print("  -> just info, no reminder (score", str(score) + ")")
    print()
