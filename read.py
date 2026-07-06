import copy
import pandas as pd

excel = pd.ExcelFile("Chemical Engineering.xlsx")
print(excel.sheet_names)
print(len(excel.sheet_names))

excel_file = pd.ExcelFile("Chemical Engineering.xlsx")

#cleaning func begins
def clean_sheet(df):

    #checking the data
    print(df.head())
    print(df.columns)
    print(df.shape)
    print(df.isnull().sum())
    print(df.duplicated().sum())

    # copy the column
    df["Question_Clean"] = df["Question"]
    #remove extra space 
    df["Question_Clean"] = df["Question_Clean"].str.strip()
    #checking
    print(df[["Question", "Question_Clean"]].head())

    #craetion of small list
    text_columns = ["Question", "Option A", "Option B", "Option C", "Option D"]

    #clean all given
    for col in text_columns:
        #remove space outside the text
        df[col + "_Clean"] = df[col].str.strip()
        #remove spaces between the text
        df[col + "_Clean"] = df[col + "_Clean"].str.replace(r"\s+", " ", regex=True)
        #checking
        print(df["Question"].head())

    #flag col creation
    df["Question_Flag"] = df["Question_Clean"].isnull()

    #marking the ques is fine or not fine 
    df["Question_Flag"] = df["Question_Clean"].isnull().map({True: "Missing", False: "OK"})
    #check
    print(df[["Question_Clean", "Question_Flag"]].head())

    #marking the opt is fine or not fine 
    for col in text_columns:
        df[col + "_Flag"] = df[col + "_Clean"].isnull().map({True: "Missing", False: "OK"})


    #dept new col name add
    df["Department"] = "Chemical Engineering"

    #id new col add
    df["Topic_ID"] = df["Topic"].str.replace(" ", "_")
    #check
    print(df[["ID", "Topic", "Topic_ID"]].head())

    #id with topic_id merged
    df["ID_Clean"] = "IB-MCQ-CHEM-" + df["Topic_ID"] + "-" + df["ID"].str.split("-").str[-1]
    #check
    print(df[["ID", "ID_Clean"]].head())

    #remove topic from section
    df["Section_Clean"] = df["Section"]

    df["Section_Clean"] = df.apply(lambda x: x["Section"].replace(x["Topic"] + " - ", ""), axis=1)
    #check
    print(df[["Section", "Section_Clean"]].head())

    #clean ques:Remove double spaces, Remove unsupported characters, Create Clean column,Create Flag column
    df["Question_Clean"] = (
        df["Question"]
        .fillna("")
        .str.strip()
        .str.replace(r"\s+", " ", regex=True)
        .str.replace(r"[^\w\s?.,()%/-]", "", regex=True)
    )

    #flag ques
    df["Question_Flag"] = df["Question_Clean"].eq("").map({
        True: "Missing",
        False: "OK"
    })

    #clean options
    option_cols = ["Option A", "Option B", "Option C", "Option D", "Option E"]

    for col in option_cols:
        df[col + "_Clean"] = (
            df[col]
            .fillna("")
            .str.strip()
            .str.replace(r"\s+", " ", regex=True)
            .str.replace(r"[^\w\s?.,()%/-]", "", regex=True)
        )

        df[col + "_Flag"] = df[col + "_Clean"].eq("").map({
            True: "Missing",
            False: "OK"
        })

    #answer flag
    df["Answer_Flag"] = df["Answer"].fillna("").eq("").map({
        True: "Missing",
        False: "OK"
    })

    #explanation clean
    df["explanation"] = df["Explanation"].str.replace(
        r"No answer description is available\.\s*Let's discuss\.",
        "",
        regex=True
    )

    #topic clean
    df["Topic"] = df["Topic"].fillna("").str.strip()
    df["Topic_Flag"] = df["Topic"].eq("").map({True: "Missing", False: "OK"})

    #extract failed flag
    df["Extract_Failed_Flag"] = "OK"
    df.loc[df["Extract Failed"].notna(), "Extract_Failed_Flag"] = "Check manually"

    #p3 columns
    new_columns = {
        "difficulty": "",
        "bloom_level": "",
        "skill_type": "",
        "exam_weightage": "",
        "ideal_time_sec": "",
        "marks": 1,
        "negative_marks": 0,
        "misconception_a": "",
        "misconception_b": "",
        "misconception_c": "",
        "misconception_d": "",
        "misconception_e": ""
    }

    for col, value in new_columns.items():
        df[col] = value

    return df


#skipping the 2 sheets
skip_sheets = ["Cleaning SOP", "Extraction_Log"]


# all sheets
output_sheets = {}

for sheet in excel_file.sheet_names:

    # skip system sheets
    if sheet in skip_sheets:
        print(f"Skipping sheet: {sheet}")
        continue

    # read sheet
    df = pd.read_excel(excel_file, sheet_name=sheet)

    # clean sheet
    cleaned_df = clean_sheet(df)

    # store result
    output_sheets[sheet] = cleaned_df


#saving the output file
with pd.ExcelWriter("cleaned_output.xlsx") as writer:
    for sheet_name, df in output_sheets.items():
        df.to_excel(writer, sheet_name=sheet_name, index=False)

print("All sheets cleaned successfully")