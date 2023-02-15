#!/bin/zsh
pip install openai
npm install openai
echo "OpenAI installation complete"

echo "#!/bin/zsh
python3 /TmGPT.py" > TmGPT
chmod +x TmGPT

sudo mv TmGPT /usr/local/bin/
echo "TmGPT successfully moved to /usr/local/bin/"

