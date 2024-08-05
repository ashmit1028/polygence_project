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
    write_to_file    
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
    print(f"ChatGPT response:\n\n {message}")

    # write answer to file.

    if write_to_file:
        file_handle.write(f"sending request to ChatGPT: {q} \n\n")
        file_handle.write(f"ChatGPT response:\n\n {message}")
        file_handle.write("\n\n")

    print("pausing for 10 seconds.....")
    time.sleep(10)
    
    return message



# open math problems input file.
#f = open("/Users/rarasada/champ_ext/data/dummy_mini.txt", "r")
f = open("/Users/rarasada/champ_ext/data/dummy_105.txt", "r")

# open output file.
#f1 = open("/Users/rarasada/champ_ext/data/dummy_mini_output.txt", "w")
f1 = open("/Users/rarasada/champ_ext/data/dummy_105_output.txt", "w")

# create a ChatGPT client.
client = OpenAI()

##### BEGIN q1 ####
q1 = "You are an expert on mathematics."

execute_query(
    q1,
    "system",
    "gpt-4o-mini",
    f1,
    False
)

#### end q1 #####

#for q in f:
while True:
    q = f.readline()
    if not q:
        break

    ref_ans = f.readline()

    if not ref_ans:
        break


    #### BEGIN q2 ####
    # creating math problem.

    q2 = q[:-1]
    #q_with_prompt = "The question is:" + q
    q_with_prompt = q2

    message = execute_query(
        q_with_prompt,
        "user",
        "gpt-4o-mini",
        f1,
        True
    )

    #### END q2 #####

    #### BEGIN q3 ####
    q3 = f"Now, summarize the answer below in one sentence, without any intermediate steps or explanations: \n {message}."
    
    ai_answer = execute_query(
        q3,
        "user",
        "gpt-4o-mini",
        f1,
        True
    )
    #### END q3 ####
    
    q4 = f"Answer yes or no - are these 2 answers the same - {ref_ans} and ai answer: {ai_answer}"

    comparison = execute_query(
        q4,
        "user",
        "gpt-4o-mini",
        f1,
        True
    )

f.close()
f1.close() 

    
