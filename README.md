# Chatbot API

## Setup

To get this API up and running will require a few steps after cloning. First, you'll need to create a virtual environment for the app. Next, you'll need to download the model parameters into the app. Finally, upon initialization the flask app will download the model for the chatbot itself. This last step does not require you to do anything aside from starting the flask app but I feel it is important to mention nonetheless. 

First, create two empty folders at the root directory: "models" and "checkpoint".

## Setting Up the Virtual Environment

To setup the virtual environment one can follow the link [here](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/). I'll include some instructions below for Linux and Windows but I program on a Windows computer so take the Linux instructions with a grain of salt.

If on macOS or Linux run the following command to create the virtual environment (untested):

```cmd
python3 -m pip install --user virtualenv
python3 -m venv venv
```

If on Windows run the following instead:

```
virturalenv -p python3 venv 
```

Once the virtual environment has been installed you can activate the environment through the commands below.

If on macOS or Linux run the following:

```
source env/bin/activate
python3 -m pip install -r requirements.txt
```

If on Windows run the follwoing:

```
venv\Scripts\activate
py -m pip install -r requirements.txt
```

Doing this will activate the virtual environment and install all required libraries. 

## Loading the Model Parameters

Access the  shared google drive link [here](https://drive.google.com/file/d/1jSkhxORWsdds1UQn4b6oh6rH5CBvnw3c/view?usp=sharing) and download the tar file containing the model parameters. Once this has been downloaded, add it to the root directory of the flask app and extract. This will inform the neural net of the parameters it has been trained to learn.

## Downloading the GTP355 Model

Upon running the flask app with `flask run`  (note that you must have your virtual  environment running at the time) the python program will begin downloading the gtp335 model (our chatbot). The model is rather large at about 3 gigabytes so the download may take a while. Once it is completed it will be ready to properly function. 

## Sending API Calls

API calls are done through `/generate` take the form of the following POST request:

```json
{
    "prefixHistory": "",
    "text": "Hey",
    "model": "Aryeh"
}
```

Note that prefixHistory should contain the history of the conversation so far. An example looks like so:

```
Person: You up? \nAryeh Bookbinder: I'm doing something with Mark and his family tomorrow \nAryeh Bookbinder: I'm super excited \nPerson: Could I ask you something? \nAryeh Bookbinder: Sure, what's up
```

It is important to keep the speaker's name as  "Person" when passing in this string.

The response taking the form:

```json
{
    "result": "Aryeh Bookbinder: Hey man, I'm at work\nAryeh Bookbinder: I'll be with the owner of the business later tonight"
}
```

Note that if we want a  persistent conversation - one that maintains a consistent topic - we need to pass in the entire conversation history in the `"text"` key when we send our POST requests. 

