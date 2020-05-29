# python-copebot
A machine learning chatbot based off of csvance's armchair-expert (https://github.com/csvance/armchair-expert)

# Windows Setup
Currently, Copebot Python Edition has been tested to work with the following dependencies:
- Python 3.7.7 [LINK](https://www.python.org/downloads/release/python-377/)
- Cuda 10.0.130 [LINK](https://developer.nvidia.com/cuda-10.0-download-archive)
- Cudnn v7.6.5.32 for Cuda 10.0 [LINK](https://developer.nvidia.com/rdp/cudnn-download#a-collapse765-10)

After installing these, use pip to install [requirements.txt](https://gist.githubusercontent.com/collectioncard/ec212a338400b003a72a6ac7d75d3fc7/raw/c7e354204dcaa59f458b8beff5f24f460d9632bb/requirements.txt) via the command ``pip install --no-cache-dir -r requirements.txt``

Finally, install spacy with the command ``python -m spacy download en_core_web_sm``

You should now be able to run copbot by double clicking the copebot_python_edition.py file


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
