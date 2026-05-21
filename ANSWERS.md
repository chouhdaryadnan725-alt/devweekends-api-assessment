# Assessment Answers
1. How to run
To run this project, make sure you have Python installed along with the `requests` library. Follow these exact steps:
. Install the required library using terminal:
   ```bash
2.  Run the application command:
. First write pip install requests so internet library installs
. Than write the code python app.py to run the code
3. Stack choice
Language: Python 
Library: Requests (for handling public API calls)
Why this choice? As a Chemical Engineering student, Python is the most practical language for data management, process modeling, and future automation tools. It has a very clean syntax and readable structure, making it perfect for building quick utility scripts.
4. One real edge case:
File & Line Number: In app.py, from Line 11 to Line 13.
if response.status_code == 404:
    print("Country Name is invalid ! Write Correct spelling.")
5. AI usage:
Tool Used: Gemini AI
What I asked & what it gave: Since my core background is in Chemical Engineering and my coding basics are at an absolute beginner level, I asked the AI to provide a lightweight, beginner-friendly Python script that fetches data from restcountries.com and handles a 404 response. It gave me a basic structural blueprint.
What I changed and why: The AI initially generated a more complex script using advanced try-except blocks and nested exception tracking. I manually stripped it down to a direct if-else condition based on the API status_code to align with my beginner level. I also customized the user-facing print statement on Line 12 to be more descriptive ("Country Name is invalid ! Write Correct spelling.") so that the error message sounds straightforward and clear.
6. Honest gap:
What isn't good enough: The script is currently a text-based Command Line Interface (CLI) tool. While it successfully handles basic invalid inputs (404 errors), it doesn't gracefully handle complete internet disconnection/network failure
What I would do to fix it with another day:** Given an extra day and more learning, I would first add proper network error handling (`try-except`) so the app doesn't crash when offline.
