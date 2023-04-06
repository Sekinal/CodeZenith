import time
import custom_command_line as cml
import gpt_config as gptc
import memory as mm

user_message = ''
gpt_answer = ''
user_gpt_message = ''

# Print initial messages to the console
cml.pretty_print_system("This is a coding assistant. Please choose the GPT model to be used during this session.")
time.sleep(0.5)
cml.pretty_print_system("If you want to exit the assistant, just write 'EXIT' after entering the model name or press CTRL-C.")
time.sleep(0.5)
cml.pretty_print_system("The recommended GPT models to be used are the following:")
time.sleep(0.5)
cml.pretty_print_system("- gpt-3.5-turbo: Currently the best option. Good performance and somewhat cheap.")
cml.pretty_print_system("- gpt-4: Currently the state-of-the-art. The best performance and incredibly high-cost.")

# Prompt the user for the GPT model to use
gpt_model = cml.pretty_input_user()

while True:
    try:
        # Prompt the user for input and generate a GPT response
        user_message = cml.pretty_input_user()
        if user_message.upper() == 'EXIT':
            # Exit the program if the user inputs 'EXIT'
            break

        gpt_answer = gptc.gpt_answer(user_message, gpt_model)
        
        # Print the GPT response to the console
        cml.pretty_print_gpt(gpt_answer)
        
        gpt_answer.replace('\"\"\"', "///")
        user_gpt_message = f'User:{user_message}\nAssistant: {gpt_answer}'
        
        mm.store_to_memory(user_gpt_message)
        
    except KeyboardInterrupt:
        # Exit the program if the user presses Ctrl-C
        cml.pretty_print_system('Program terminated by user')
        break

    except Exception as exception:
        # Handle any other exceptions that might occur during program execution
        cml.pretty_print_system('There was an error during the execution of the program')
        cml.pretty_print_system(exception)