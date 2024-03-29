# python-copebot
A machine learning chatbot based off of csvance's armchair-expert (https://github.com/csvance/armchair-expert)

# Windows Setup
Currently, Copebot Python Edition has been tested to work with the following dependencies:
- Python 3.7.7 [LINK](https://www.python.org/downloads/release/python-377/)
- Cuda 10.0.130 [LINK](https://developer.nvidia.com/cuda-10.0-download-archive)
- Cudnn v7.6.5.32 for Cuda 10.0 [LINK](https://developer.nvidia.com/rdp/cudnn-download#a-collapse765-10)

After installing these, use pip to install [requirements.txt](https://gist.githubusercontent.com/collectioncard/ec212a338400b003a72a6ac7d75d3fc7/raw/c7e354204dcaa59f458b8beff5f24f460d9632bb/requirements.txt) via the command ``pip install --no-cache-dir -r requirements.txt``

Finally, install spacy with the command ``python -m spacy download en_core_web_sm``

Now that all of the requirements are installed, add your discord bot information to the bot_config.py file under /config

You should now be able to run copebot by double clicking the copebot_python_edition.py file

\*NOTE: If you have multiple versions of python installed on your system and python 3.7 is not your default, you can run copebot with the correct version of python using the [python launcher](https://docs.python.org/3/using/windows.html#launcher). CD into the same folder as the .py file and run   
`py -3.7 copebot_python_edition.py`

# Mac OS Setup (Note: No GPU Support)
Currently, Copebot Python Edition requires Python 3.7.7 [LINK](https://www.python.org/downloads/release/python-377/)

After installing python, use pip to install [requirements.txt](https://gist.githubusercontent.com/collectioncard/130e0fa0c626020e32611c1c8d18366a/raw/0f05c35f71b6641785b2f93c266803e382f378ac/requirements.txt) via the command ``pip3 install --no-cache-dir -r requirements.txt``

Finally, install spacy with the command ``python3 -m spacy download en_core_web_sm``

Now that all of the requirements are installed, add your discord bot information to the bot_config.py file under /config
   
   Next, set "USE_GPU" to false in ai_config.py

You should now be able to cd into the copebot folder and launch it via the command `python3 copebot_python_edition.py`

\*NOTE: NOTE: If you get a certificate error, run the 'install certificates.command' file located in the python folder in the applications folder. 



##Having issues running copebot?
Try updating your version of discord.py to the latest version of discord.py. (check to make sure the version you are running is at least the same as the one listed in your systems requirements.txt file)

## License
The source code in this repository is licenced under the [AGPL-3.0 license](LICENSE), with portions code licensed under the MIT License, which is as follows:
```
MIT License

Copyright (c) 2017 Carroll Vance

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
