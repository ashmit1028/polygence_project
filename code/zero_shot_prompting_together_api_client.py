from together import Together
import os
import time

def execute_together_api_query(
    q,
    role,
    file_handle,
    file_handle_ans,
    write_to_file,
    is_ans,
    problem_num,
    ref_ans,
    model_name
):
    # creating math problem.

    q = q[:-1]

    print(f"sending request to {model_name}: {q} \n\n")
    response = client.chat.completions.create(
            model=model_name,
            messages=[{"role": "user", "content": q}],
        )

    message = response.choices[0].message.content
    print(message)
    
    # write answer to file.

    if write_to_file:
        file_handle.write(f"sending request to {model_name}: {q} \n\n")
        file_handle.write(f"{model_name} response:\n\n {message}")
        file_handle.write("\n\n")

    if is_ans:
        file_handle_ans.write(f"problem_id:{problem_num} \n\n")
        file_handle_ans.write(f"{model_name} response:\n\n {message} \n\n")
        file_handle_ans.write(f"{ref_ans} \n\n")
        file_handle_ans.write("\n\n")

    print("pausing for 5 seconds.....")
    time.sleep(5)

    return message

#model_concise_name = "mistralai"
#model_name = "mistralai/Mixtral-8x7B-Instruct-v0.1"

#model_concise_name = "llama"
#model_name = "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo"

#model_concise_name = "gemma"
#model_name = "google/gemma-2-9b-it"

model_concise_name = "llama_405B"
model_name = "meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo"

# open math problems input file.
f = open("/Users/parasada/champ_ext/data/aime_set_2011_to_2020.txt", "r")

# open output file.
f1 = open(f"/Users/parasada/champ_ext/data/together/{model_concise_name}/aime_set_2011_to_2020_output.txt", "w")

# open output file to save answers.
f2 = open(f"/Users/parasada/champ_ext/data/together/{model_concise_name}/aime_set_2011_to_2020_answer.txt", "w")

# create a Gemini client.
#genai.configure(api_key = os.environ["API_KEY"])
#model = genai.GenerativeModel("gemini-1.5-flash")

# create a Together API client.
client = Together(api_key=os.environ.get("TOGETHER_API_KEY"))

##### BEGIN q1 ####
q1 = "You are an expert on mathematics."

execute_together_api_query(
    q1,
    "system",
    f1,
    f2,
    False,
    False,
    "",
    "",
    model_name
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

    message = execute_together_api_query(
        q_with_prompt,
        "user",
        f1,
        f2,
        True,
        False,
        "",
        "",
        model_name
    )

    #### END q2 #####

    #### BEGIN q3 ####
    q3 = f"Now, summarize the answer below in one sentence, without any intermediate steps or explanations: \n {message}."

    ai_answer = execute_together_api_query(
        q3,
        "user",
        f1,
        f2,
        True,
        True,
        problem_num,
        ref_ans,
        model_name
    )
    #### END q3 ####

f.close()
f1.close()
f2.close()
