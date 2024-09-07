from openai import OpenAI
import os
from dotenv import load_dotenv
import time

load_dotenv()

def execute_query(
    q, 
    role,
    model,
    file_handle,
    file_handle_ans,
    write_to_file,
    is_ans,
    problem_num,
    ref_ans    
):
    # creating math problem.

    q = q[:-1]

    # prep dictionary to send as request parameter to ChatGPT.
    dict = {}
    dict["role"] = role
    dict["content"] = q

    print(f"sending request to ChatGPT: {q} \n\n")
    chat_completion = client.chat.completions.create(
        model=model,
        messages=[dict]
    )

    # printing answer to output.
    message = chat_completion.choices[0].message.content
    print(f"ChatGPT response:\n\n {message[:1000]}")

    # write answer to file.

    if write_to_file:
        file_handle.write(f"sending request to ChatGPT: {q} \n\n")
        file_handle.write(f"ChatGPT response:\n\n {message}")
        file_handle.write("\n\n")

    if is_ans:
        file_handle_ans.write(f"problem_id:{problem_num} \n\n")
        file_handle_ans.write(f"ChatGPT response:\n\n {message} \n\n")
        file_handle_ans.write(f"{ref_ans} \n\n")
        file_handle_ans.write("\n\n") 
    
    print("pausing for 5 seconds.....")
    time.sleep(5)
    
    return message



# open math problems input file.
f = open("/Users/rarasada/champ_ext/data/aime_set_2003_to_2004.txt", "r")

# open output file.
f1 = open("/Users/rarasada/champ_ext/data/aime_set_2003_to_2004_output.txt", "w")

# open output file to save answers.
f2 = open("/Users/rarasada/champ_ext/data/aime_set_2003_to_2004_answer.txt", "w")

# create a ChatGPT client.
client = OpenAI()

##### BEGIN q1 ####
q1 = "You are an expert on mathematics."

execute_query(
    q1,
    "system",
    "gpt-4o-mini",
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

    message = execute_query(
        q_with_prompt,
        "user",
        "gpt-4o-mini",
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
    
    ai_answer = execute_query(
        q3,
        "user",
        "gpt-4o-mini",
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
