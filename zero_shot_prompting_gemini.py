import google.generativeai as genai
import os
import time

#genai.configure(api_key = os.environ["API_KEY"])
#model = genai.GenerativeModel("gemini-1.5-flash")

def execute_gemini_query(
    q,
    role,
    file_handle,
    file_handle_ans,
    write_to_file,
    is_ans,
    problem_num,
    ref_ans
):
    # creating math problem.

    q = q[:-1]

    print(f"sending request to Gemini: {q} \n\n")
    response = model.generate_content(q)
    message = response.text
    print(message)
    
    # write answer to file.

    if write_to_file:
        file_handle.write(f"sending request to Gemini: {q} \n\n")
        file_handle.write(f"Gemini response:\n\n {message}")
        file_handle.write("\n\n")

    if is_ans:
        file_handle_ans.write(f"problem_id:{problem_num} \n\n")
        file_handle_ans.write(f"Gemini response:\n\n {message} \n\n")
        file_handle_ans.write(f"{ref_ans} \n\n")
        file_handle_ans.write("\n\n")

    print("pausing for 5 seconds.....")
    time.sleep(5)

    return message


# open math problems input file.
f = open("/Users/aarasada/champ_ext/data/gemini/aime_set_2003_to_2004.txt", "r")

# open output file.
f1 = open("/Users/aarasada/champ_ext/data/gemini/aime_set_2003_to_2004_output.txt", "w")

# open output file to save answers.
f2 = open("/Users/aarasada/champ_ext/data/gemini/aime_set_2003_to_2004_answer.txt", "w")

# create a Gemini client.
genai.configure(api_key = os.environ["API_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")

##### BEGIN q1 ####
q1 = "You are an expert on mathematics."

execute_gemini_query(
    q1,
    "system",
    f1,
    f2,
    False,
    False,
    "",
    ""
)

#### end q1 #####

while True:
    question_number = f.readline() #question_number:special_functions_p1
    if not question_number:
        break

    problem_num = question_number.split(':')[1]
    print("problem_num:" + problem_num)

    problem = f.readline()
    if not problem:
        break
    print("problem:" + problem)

    ref_ans = f.readline()
    if not ref_ans:
        break
    print("ref_ans:" + ref_ans)

    concept = f.readline()
    if not concept:
        break
    print("concept:" + concept)

    source = f.readline()
    if not source:
        break

    status = f.readline()
    if not status:
        break

    print("STATUS is:" + status)

    status = status.split(':')[1]
    if status == "do_not_run":
        continue

    line_break = f.readline()
    if not line_break:
        print("not line break")
        break

    #### BEGIN q2 ####
    # creating math problem.

    q_with_prompt = problem[:-1]

    message = execute_gemini_query(
        q_with_prompt,
        "user",
        f1,
        f2,
        True,
        False,
        "",
        ""
    )

    #### END q2 #####

    #### BEGIN q3 ####
    q3 = f"Now, summarize the answer below in one sentence, without any intermediate steps or explanations: \n {message}."

    ai_answer = execute_gemini_query(
        q3,
        "user",
        f1,
        f2,
        True,
        True,
        problem_num,
        ref_ans
    )
    #### END q3 ####

f.close()
f1.close()
f2.close()
