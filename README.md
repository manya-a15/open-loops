# Open Loops

A concept prototype for a Gmail feature that catches important emails you opened but never acted on, and brings them back before their deadline.

**Live demo:** https://manya-a15.github.io/open-loops/

## The problem

Gmail treats "read" as "done." Once you open an email, it loses its bold styling and blends into the inbox. Emails that need an action, like paying a fee, filling a registration form or submitting an assignment, are easy to forget. Gmail's Nudges only cover replies, and Snooze or Star only help if you remember to use them.

## How Open Loops works

1. **Detect.** When you open an email, it is scored for action clues: action words ("pay," "register," "submit"), a deadline, and a form or payment link. A score of 3 or more marks it as needing action.
2. **Capture.** If you leave the email without acting, a card asks when to remind you. Picking a time gives a push alert. Skipping it keeps the reminder quiet: morning card only, plus one alert the day before the deadline.
3. **Resurface.** A morning card shows how many open loops you have. Ignored reminders move to the top.
4. **Close only when done.** Opening a link moves the loop to "In progress." It closes automatically when a confirmation email arrives, such as a Google Forms response or payment receipt. If none comes, the next reminder asks "Did you finish this?"

## Try the demo

1. Open the WIEEE email and click the form link.
2. Press "Back to inbox." The email now shows "In progress."
3. In the Open Loops tab, press "Preview reminder" to see "Did you finish this?"
4. Press "Simulate confirmation email." The loop closes by itself.

"Reset demo" at the top starts over. The demo pretends today is 19 Oct 2026, so the sample deadlines make sense.

## Built with

- HTML, CSS and JavaScript, in a single `index.html` file
- Python for the detection logic (`detector.py`), the same scoring rule the prototype uses
- No backend: the sample emails live inside the page
- Hosted on GitHub Pages

## Files

| File | What it is |
| --- | --- |
| `index.html` | The prototype website |
| `detector.py` | The action-detection logic in Python, tested on sample emails |

## Run it locally

- **Prototype:** download `index.html` and open it in any web browser. No installation needed.
- **Detector:** run `python3 detector.py` to see which sample emails are flagged as open loops.

---

Made by Manya Agarwal, CSE Core, VIT Vellore.
