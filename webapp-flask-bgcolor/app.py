from flask import Flask, render_template
import socket
import random
import os
import argparse

app = Flask(__name__)

color_codes = {
    "#ff0000":"red",
    "#00ff00":"green",
    "#0000ff":"blue",
    "#808000":"olive",
    "#800080":"purple",
    "#000080":"navy"
}

SUPPORTED_COLORS = ",".join(color_codes.keys())

# Get color from Environment variable
COLORCODE_FROM_ENV = os.environ.get('APP_COLORCODE')
# Generate a random colorcode
COLORCODE = random.choice(["#ff0000", "#00ff00", "#0000ff", "#808000", "#800080", "#000080"])
# Get dynamic title from Environment variable
TITLE_FROM_ENV = os.environ.get('APP_TITLE')
# Set default title
TITLE = "Cloud Computing - University of West Attica"

@app.route("/")
def main():
    # return 'Hello'
    return render_template('index.html', name=socket.gethostname(), colorcode=color_codes[COLORCODE], colorname=COLORCODE, title=TITLE)


if __name__ == "__main__":
    print("This is a simple flask webapp that displays a colored background and a greeting message. \n"
          "The color can be specified in two different ways: \n"
          "    1. As a command line argument with --colorcode as the argument. Accepts one of the following \n"
          "       colors according the list below. \n"
          "    2. As an Environment variable APP_COLORCODE. Accepts one of the following colors according \n"
          "       the list below.\n"
          "In any other case, a random color is picked from the list below.\n"
          "\n"
          "Note 1: Accepted colors [" + SUPPORTED_COLORS + "] \n"
          "Note 2: Command line argument precedes over environment variable.\n"
          "\n"
          "")


    # Check for Command Line Parameters for colorcode
    parser = argparse.ArgumentParser()
    parser.add_argument('--colorcode', required=False)
    # Check for Command Line Parameters for title
    parser.add_argument('--title', required=False)
    args = parser.parse_args()

    if args.color:
        print("Colorcode from command line argument =" + args.colorcode)
        COLORCODE = args.color
        if COLORCODE_FROM_ENV:
            print("A colorcode was set through environment variable -" + COLORCODE_FROM_ENV + ". However, colorcode from command line argument takes precendence.")
    elif COLORCODE_FROM_ENV:
        print("No Command line argument. Colorcode from environment variable =" + COLORCODE_FROM_ENV)
        COLORCODE= COLORCODE_FROM_ENV
    else:
        print("No command line argument or environment variable. Picking a Random Color =" + COLORCODE)

    # Check if input colorcode is a supported one
    if COLORCODE not in color_codes:
        print("Colorcode not supported. Received '" + COLORCODE + "' expected one of " + SUPPORTED_COLORS)
        exit(1)

    if args.title:
        print("Title from command line argument =" + args.title)
        TITLE = args.title
        if TITLE_FROM_ENV:
            print("A title was set through environment variable -" + TITLE_FROM_ENV + ". However, title from command line argument takes precendence.")
    elif TITLE_FROM_ENV:
        print("No Command line argument. Title from environment variable =" + TITLE_FROM_ENV)
        TITLE = TITLE_FROM_ENV
    else:
        print("No command line argument or environment variable. Picking a default title =" + TITLE)


    # Run Flask Application
    app.run(host="0.0.0.0", port=8000)
