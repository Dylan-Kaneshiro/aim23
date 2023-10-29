import gradio as gr

with gr.Blocks(theme='upsatwal/mlsc_tiet') as demo:

    count = 0

    def hello(name):
      return "Hello " + name + "!"

    def add(number1, number2):
      return int(number1) + int(number2)

    def counter():
      global count
      count += 1
      return int(count)

    def performActions(name, number1, number2):
      first = hello(name)
      second = add(number1, number2)
      third = counter()
      return first, second, third


    name = gr.Textbox(label="Name")
    greet = gr.Textbox(label="Greeting Output")

    number1 = gr.Textbox(label="First Number")
    number2 = gr.Textbox(label="Second Number")
    finalAddition = gr.Textbox(label="The addition of both numbers:")

    displayCount = gr.Textbox(label="Times Pressed")

    finalActionButton = gr.Button("Push for greeting, addition, and counter")
    finalActionButton.click(fn=performActions, inputs = [name, number1, number2], outputs = [ greet, finalAddition, displayCount])

demo.launch()