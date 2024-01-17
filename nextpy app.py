# This file has been modified by the Nextpy Team in 2023 using AI tools and automation scripts. 
# We have rigorously tested these modifications to ensure reliability and performance. Based on successful test results, we are confident in the quality and stability of these changes.

import nextpy as xt
# Construct the filename to display 
#from xtconfig import config
#filename = f"{config.app_name}/{config.app_name}.py"

# define index page. Frontend Pages are just functions that return a frontend components
class State(xt.State):
    content: str="Registration form"
    def submit(self):
        self.content="You are successfully registered"
    
def index():
    layout = xt.vstack(
        xt.text(State.content),
        xt.hstack(
            xt.text(
            "Customer name"
            ),
            xt.input()
        ),
        xt.hstack(
           xt.text(
               "Enter your age"
           ),
           xt.input()
        ),
        xt.hstack(
            xt.text(
                "Contact Number"
            ),
            xt.input()
        ),
        xt.hstack(
            xt.text(
                "Email id"
            ),
            xt.input()
        ),
        xt.hstack(
            xt.text(
                "Locality"
            ),
            xt.input()
        ),
        xt.hstack(
            xt.text(
                "City"
            ),
            xt.input()
        ),
        xt.button("Submit",on_click=State.submit,color="black"),
        background="black",
        height="100vh",
        padding_top="7%",
        color="white",
        font_size="25px",
    )

    return layout
style={
    "text_align":"center",
}
app = xt.App(style=style)
app.add_page(index)
  
