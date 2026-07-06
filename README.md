# Chemical Engineering Question Data Cleaning

## What this project is about

This project takes a set of Chemical Engineering exam questions stored in an Excel file and cleans them up so the information is accurate, consistent, and ready to use.

## Steps done, from start to end

1. **Opened the original file.** The starting file, "Chemical Engineering.xlsx", contains several sheets, each holding a set of questions with their answer options, correct answers, and explanations.

2. **Went through each sheet one by one.** Two sheets that were not question data ("Cleaning SOP" and "Extraction_Log") were left untouched and skipped.

3. **Checked each sheet for problems**, such as missing details, repeated entries, and extra blank spaces in the text.

4. **Cleaned the question text** by removing extra spaces and any unwanted symbols, so every question reads clearly and consistently.

5. **Cleaned the answer options** (Option A, B, C, D, and E) in the same way, removing extra spaces and unwanted symbols.

6. **Marked each question and each option as "OK" or "Missing"**, depending on whether the information was filled in or left blank.

7. **Labelled every question with its department**, marking all of them as belonging to "Chemical Engineering".

8. **Created a clean, unique reference number for every question**, combining the topic name with the original reference number.

9. **Cleaned up the section names** by removing the repeated topic name that was showing up twice.

10. **Checked the correct answer for each question** and marked whether it was filled in or missing.

11. **Cleaned the explanation text**, removing a placeholder message that appeared when no real explanation was available.

12. **Cleaned the topic name** for each question and marked whether it was missing.

13. **Checked for questions that had failed during the original extraction** and flagged them so they can be reviewed by hand.

14. **Added new blank fields for future use**, such as difficulty level, thinking level, skill type, exam weightage, ideal time to answer, marks awarded, marks deducted for a wrong answer, and notes on common wrong-answer reasoning for each option.

15. **Saved all the cleaned sheets into a new file**, named "cleaned_output.xlsx", keeping the original file untouched.

16. **Reviewed the cleaned file manually** to double-check the results, producing a manually checked version, "chem engg cleaned output manual.xlsx".

17. **Saved and backed up all the work online.** The project files were placed under version control and uploaded to a GitHub repository, so the work is safely stored and can be tracked or shared going forward. Any further changes made will continue to be saved and uploaded the same way.

## Files in this project

- **Chemical Engineering.xlsx** — the original file with the raw questions.
- **read.py** — the set of instructions used to clean the data.
- **cleaned_output.xlsx** — the automatically cleaned result.
- **chem engg cleaned output manual.xlsx** — the cleaned result after a manual review.
