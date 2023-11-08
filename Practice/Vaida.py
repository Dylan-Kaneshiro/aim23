import gradio as gr

# tried saving the chat history and displaying it in a form of collapse and expand 
# it doesn't look pretty but achieves the objective of hiding and expanding the questions

def display_question_and_answer(question, answer, tuple_list):
    new_tuple = (question, answer)
    tuple_list.append(new_tuple)

    qa_history = ""
    for i, (q, a) in enumerate(tuple_list):
        qa_history += f"<details><summary>Q: {q}</summary><p>A: {a}</p></details>"

    return qa_history, tuple_list

with gr.Blocks() as demo:
    tuple_state = gr.State([])

    output_box = gr.Interface(
        fn=display_question_and_answer,
        inputs=[gr.Textbox(label="Enter question:"), gr.Textbox(label="Enter question:"), tuple_state],
        outputs=["html", gr.State()],
        live=False,
        title="QA History",
    )
    

demo.launch()
