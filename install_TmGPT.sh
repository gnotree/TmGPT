#!/bin/zsh

# Install OpenAI Python package and npm package
pip install openai
npm install openai
echo "OpenAI installation complete"

# Create the TmGPT script that runs the TmGPT.py file
echo '#!/bin/zsh' > TmGPT
echo 'python3 "$(dirname "$0")/TmGPT.py" "$@"' >> TmGPT
chmod +x TmGPT

# Move the TmGPT script to /usr/local/bin/ and copy the TmGPT.py file to /usr/local/bin/
sudo mv TmGPT /usr/local/bin/
sudo cp TmGPT.py /usr/local/bin/

echo "TmGPT successfully installed to /usr/local/bin/"

#Terminal GPT - Version 1.2 - Developed by GTAI
#In the updated .sh file, we first install the OpenAI packages and then create a TmGPT script that runs the TmGPT.py file using the python3 command. 
#We use $(dirname "$0") to get the path of the directory where the TmGPT script is located, so that we can reference the TmGPT.py file in the same directory.
#After creating the TmGPT script, we move it to /usr/local/bin/ using sudo mv, and then we copy the TmGPT.py file to the same directory using sudo cp. 
#This ensures that both the TmGPT script and the TmGPT.py file are in the same directory, and the script can access the file using the relative path.
#Finally, we print a message to the user indicating that the installation was successful.
