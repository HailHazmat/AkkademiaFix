# Akkademia
Akkademia is a tool for automatically transliterating Unicode cuneiform glyphs. It is written in python script and uses HMM, MEMM and BiLSTM neural networks to determine appropriate sign-readings and segmentation.

We trained these algorithms on the RINAP corpora (Royal Inscriptions of the Neo-Assyrian Period), which are available in JSON and XML/TEI formats thanks to the efforts of the Official Inscriptions of the Middle East in Antiquity (OIMEA) Munich Project of Karen Radner and Jamie Novotny, funded by the Alexander von Humboldt Foundation, available [here](<http://oracc.org/rinap/>). We achieve accuracy rates of 89.5% with HMM, 94% with MEMM, and 96.7% with BiLSTM on the trained corpora. Our model can also be used on texts from other periods and genres, with varying levels of success.

## Getting Started
Akkademia can be accessed in three different ways:
* Website
* Python package
* Github clone

The website and python package are meant to be accessible to people without advanced programming knowledge.

## Website
Go to the [Babylonian Engine website](<https://babylonian.herokuapp.com/>) (*under development*)

Go to the "Akkademia" tab and follow the instructions there for transliterating your signs.

## Python Package
Our python package "akkadian" will enable you to use Akkademia on your local machine.

### Prerequisites
You will need a Python 3.7.x installed. Our package currently does not work with other versions of python. You can follow the installation instructions [here](<https://realpython.com/installing-python/>) or go straight ahead to [python's downloads page](<https://www.python.org/downloads/>) and pick an appropriate version.

Mac comes preinstalled with python 2.7, which may remain the default python version even after installing 3.7.x. To check, type ``python --version`` into terminal. If the running version is python 2.7, the simplest short-term solution is to type ``python3`` or ``pip3`` in Terminal throughout instead of ``python`` and ``pip`` as in the instructions below.

### Package Installation
You can install the package using the pip install function. If you do not have pip installed on your computer, or you are not sure whether it is installed or not, you can follow the instructions [here](<https://www.makeuseof.com/tag/install-pip-for-python/>)

Before installing the package akkadian, you will need to install the torch package. For Windows, copy the following into Command Prompt (CMD):

```
pip install torch==1.0.0 torchvision==0.2.1 -f https://download.pytorch.org/whl/torch_stable.html
```
For Mac and Linux copy the following into Terminal:

```
pip install torch torchvision
```
Then, type the following in Command Prompt (Windows), or Terminal (Mac and Linux):

```
pip install akkadian
```
your installation should be executed. This will take several minutes.

### Running
Open a python IDE (Integrated development environment) where a python code can be run. There are many possible IDEs, see [realpython's guide](<https://realpython.com/python-ides-code-editors-guide/>) or [wiki python's list](<https://wiki.python.org/moin/IntegratedDevelopmentEnvironments>). For beginners, we recommend using Jupyter Notebook: see downloading instructions [here](<https://jupyter.org/install>), or see downloading instructions and beginners' tutorial [here](<https://realpython.com/jupyter-notebook-introduction/>).

First, import ```akkadian.transliterate``` into your coding environment:

```
import akkadian.transliterate as akk
```

Then, you can use HMM, MEMM, or BiLSTM to transliterate the signs. The functions are:

```
akk.transliterate_hmm("Unicode_signs_here")
akk.transliterate_memm("Unicode_signs_here")
akk.transliterate_bilstm("Unicode_signs_here")
akk.transliterate_bilstm_top3("Unicode_signs_here")
```
```akk.transliterate_bilstm_top3``` gives the top three BiLSTM options, while ```akk.transliterate_bilstm``` gives only the top one.

For an immediate output of the results, put the ```akk.transliterate()``` function inside the ```print()``` function. Here are some examples with their output:
```
print(akk.transliterate_hmm("𒃻𒅘𒁀𒄿𒈬𒊒𒅖𒁲𒈠𒀀𒋾"))
ša₂ nak-ba-i-mu-ru iš-di-ma-a-ti
```
```
print(akk.transliterate_memm("𒃻𒅘𒁀𒄿𒈬𒊒𒅖𒁲𒈠𒀀𒋾"))
ša₂ SILIM ba-i-mu-ru-iš-di-ma-a-ti
```
```
print(akk.transliterate_bilstm("𒃻𒅘𒁀𒄿𒈬𒊒𒅖𒁲𒈠𒀀𒋾"))
ša₂ nak-ba-i-mu-ru iš-di-ma-a-ti 
```
```
print(akk.transliterate_bilstm_top3("𒃻𒅘𒁀𒄿𒈬𒊒𒅖𒁲𒈠𒀀𒋾"))
('ša₂ nak-ba-i-mu-ru iš-di-ma-a-ti ', 'ša₂-di-ba i mu ru-iš di ma tukul-tu ', 'MUN kis BA še-MU-šub-šah-ṭi-nab-nu-ti-')
```

This line was taken from the first line of the Epic of Gilgamesh: *ša₂ naq-ba i-mu-ru iš-di ma-a-ti*; "He who saw the Deep, the foundation of the country" (George, A.R. 2003. *The Babylonian Gilgamesh Epic: Introduction, Critical Edition and Cuneiform Texts*. 2 vols. Oxford: Oxford University Press). Although the algorithms were not trained on this text genre, they show promising, useful results.

## Github
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
You will need a Python 3.7.x installed. Our package currently does not work with other versions of python. Go to [python's downloads page](<https://www.python.org/downloads/>) and pick an appropriate version.

If you don't have git installed, install git [here](<https://git-scm.com/downloads>) (Choose the appropriate operating system).

If you don't have a Github user, create one [here](<https://github.com/join?source=header-home>).

### Simple conda env install
Copy the following into Command Prompt (with windows) or Terminal (with mac) to clone the project:
```
git clone https://github.com/gaigutherz/Akkademia.git
```
Then download your prefered version of conda, such as [miniconda](https://docs.anaconda.com/free/miniconda/index.html). We use conda because we want to create specific enviroments where we can manage dependencies without impacting the overall system.

Then create your environment with the right version of python:
```
conda create -n akkadian python=3.7
```
You can then activate as follows:
```
conda activate akkadian
```
To then install dependencies, run the following (assuming you store your git pulls from a folder in your home directory named 'GitHub'. You may need to customize this line to your system if it is stored elsewhere):
```
pip install -r ~/GitHub/Akkademia/requirements.txt
```
You will then have a specific enviornment which meets all requirements of this project without otherwise affecting operations on you linux or mac system. For a more customized install, see below. 

### Installing the python dependencies

In order to run the code, you will need the torch and allennlp libraries. If you have already installed the package akkadian, these were installed on your computer and you can skip to the next step.

Install torch: For Windows, copy the following to Command Prompt
```
pip install torch===1.3.1 torchvision===0.4.2 -f https://download.pytorch.org/whl/torch_stable.html
```

for Mac and Linux, copy the following to Terminal
```
pip install torch torchvision
```

Install overrides and allennlp: copy the following to Command Prompt (with windows) or Terminal (with mac): 
```
pip install overrides==3.1.0
pip install allennlp==0.8.5
```
### Cloning the project

Copy the following into Command Prompt (with windows) or Terminal (with mac) to clone the project:
```
git clone https://github.com/gaigutherz/Akkademia.git
```

### Included Virtual Environment (venv)

This repository ships with a pre-built Python virtual environment in the `venv/` folder. It is committed to Git intentionally so that you can clone the repo and start working immediately without having to track down specific package versions yourself.

**Why the venv is included:** The project depends on exact versions of packages such as `allennlp==0.8.5`, `overrides==3.1.0`, `spacy`, `scipy`, `pytorch-pretrained-bert`, and many others that have complex interdependencies and are difficult to install correctly from scratch. Previous attempts to recreate the environment from `requirements.txt` alone often failed due to version conflicts, deprecated packages, or missing build dependencies. By including the venv directly, all of these issues are avoided — you get the exact working environment that was tested with the code.

**PyTorch must be installed separately.** The PyTorch (`torch`) package and its CUDA libraries are excluded from the committed venv because they contain files exceeding GitHub's 100 MB per-file limit (~4 GB total). After cloning, activate the venv and install torch:

```bash
# Activate the venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install the exact torch version used by this project (Windows with CUDA 11.7):
pip install torch==1.13.1+cu117 torchvision==0.14.1+cu117 --extra-index-url https://download.pytorch.org/whl/cu117

# For CPU-only (Mac/Linux or no NVIDIA GPU):
pip install torch==1.13.1 torchvision==0.14.1
```

A fully pinned list of all installed packages is also available in `requirements_pinned.txt` for reference.

### Windows: UTF-8 Encoding Setup

When running translation scripts on Windows, you must set the Python I/O encoding to UTF-8 to correctly handle cuneiform Unicode characters. Run this command in your PowerShell window before running the translation script again:

```powershell
$env:PYTHONIOENCODING = "utf-8"
python akkadian\translate_cuneiform.py
```

Without this, you may encounter encoding errors such as `UnicodeEncodeError` when processing cuneiform signs.

### Running
Now you can develop the Akkademia repository and add your improvements!

#### Training
Use the file train.py in order to train the models using the datasets. There is a function for each model that trains, stores the pickle and tests its performance on a specific corpora.

The functions are as follows:
```
hmm_train_and_test(corpora)
memm_train_and_test(corpora)
biLSTM_train_and_test(corpora)
```

#### Transliterating
Use the file transliterate.py in order to transliterate using the models. There is a function for each model that takes Unicode cuneiform signs as parameter and returns its transliteration.

Example of usage:
```
cuneiform_signs = "𒃻𒅘𒁀𒄿𒈬𒊒𒅖𒁲𒈠𒀀𒋾"
print(transliterate(cuneiform_signs))
print(transliterate_bilstm(cuneiform_signs))
print(transliterate_bilstm_top3(cuneiform_signs))
print(transliterate_hmm(cuneiform_signs))
print(transliterate_memm(cuneiform_signs))
```

#### Interactive Translation
Use `translate_interactive.py` for a REPL-style interactive translator powered by BiLSTM. It logs all translations with timestamps to `translation_log.txt`:

```
python translate_interactive.py
```

#### Multi-Model Comparison
Use `translate_all_formats.py` to compare results from all models (BiLSTM, HMM, MEMM) plus a combined classifier side-by-side. It also highlights disputed signs where models disagree, and logs results to `full_comparison_log.txt`:

```
python translate_all_formats.py
```

#### Batch Translation
Use `batch_translate.py` to translate all `.txt` files in a folder at once. It supports both cuneiform sign translation and transliteration-to-English translation:

```
python batch_translate.py
```

Place your input files in a folder (e.g., `input_texts/`) and select the translation mode when prompted.

#### Checkpoint Repair
If Fairseq model checkpoints become corrupted or have mismatched architecture metadata, use `repair_checkpoints.py` to fix them:

```
python repair_checkpoints.py
```

This resets the checkpoint's architecture to `fconv` (convolutional) and corrects source/target language settings.

#### Testing
Use `test_akkadian.py` for a quick smoke test of the BiLSTM transliteration on sample cuneiform signs:

```
python test_akkadian.py
```

## Datasets
For training the algorithms, we used the RINAP corpora (Royal Inscriptions of the Neo-Assyrian Period), which are available in JSON and XML/TEI formats thanks to the efforts of the Humboldt Foundation-funded Official Inscriptions of the Middle East in Antiquity (OIMEA) Munich Project led by Karen Radner and Jamie Novotny, available [here](<http://oracc.org/rinap/>). The current output in our website, package and code is based on training done on these corpora alone.

For additional future training, we added the following corpora (in JSON file format) to the repository: 
		
* **RIAO** - [Royal Inscriptions of Assyria online](<http://oracc.museum.upenn.edu/riao/>)
		
* **RIBO** - [Royal Inscriptions of Babylonia online](<http://oracc.museum.upenn.edu/ribo/>)
		
* **SAAO** - [State Archives of Assyria online](<http://oracc.museum.upenn.edu/saao/>)
		
* **SUHU** - [The Inscriptions of Suhu online Project](<http://oracc.museum.upenn.edu/suhu/>)

These corpora were all prepared by the Munich Open-access Cuneiform Corpus Initiative (MOCCI) and OIMEA project teams, both led by Karen Radner and Jamie Novotny, and are fully accessible for download in JSON or XML/TEI format in their respective project webpages (see left side-panel on project webpages and look for project-name downloads).

We also included a separate dataset which includes all the corpora in XML/TEI format.

### Datasets deployment

All the dataset are taken from their respective project webpages (see left side-panel on project webpages and look for project_name downloads) and are fully accessible from there.

In our repository the datasets are located in the "raw_data" directory. They can also be downloaded from the Github repository using git clone or zip download.

## Recent Changes & Updates

This section documents all changes made to the codebase when updating from the original AkkademiaFix to the current working version.

### 1. Modified Existing Scripts

#### `akkadian/translate_from_cuneiform.py`
File-based cuneiform-to-English translation via Fairseq. Key modifications:

- **Windows Python compatibility**: Changed subprocess calls from hardcoded `python` to `sys.executable`, ensuring the correct Python interpreter is used regardless of environment (venv, conda, system install).
- **Temporary directory handling**: Added `os.makedirs("tmp", exist_ok=True)` so the `tmp/` working directory is automatically created if missing, preventing `FileNotFoundError` on first run.
- **Explicit Fairseq flags**: Added `--task translation`, `--source-lang ak`, `--target-lang en` to the Fairseq interactive CLI invocation. Without these, Fairseq may fail to locate the correct model or data-bin directory.
- **Diagnostic error output**: Added stderr capture and diagnostic printing on subprocess failure, making it easier to debug Fairseq configuration or checkpoint issues.
- **Model paths**: Uses `data-bin-not-divided-by-three-dots/` for data and `not_divided_by_three_dots_result.LR_0.1.MAX_TOKENS_4000/checkpoint_best.pt` for the cuneiform→English model checkpoint.

#### `akkadian/translate_from_transliteration.py`
File-based transliteration-to-English translation with input normalization. Key modifications:

- **Same Windows compatibility fixes** as `translate_from_cuneiform.py`: `sys.executable`, `os.makedirs`, explicit Fairseq flags, and diagnostic error output.
- **Input normalization**: Contains extensive substitution dictionaries (`letter_substitutions`, `number_substitutions`, `acute_grave_substitutions`, `logogram_substitutions`, `exception_substitutions`) applied via `organize_transliteration_line()` to normalize transliteration input before passing it to Fairseq.
- **Model paths**: Uses `data-bin-transliteration/` for data and `trans_result.LR_0.1.MAX_TOKENS_4000/checkpoint_best.pt` for the transliteration→English model checkpoint.

#### `akkadian/translate_cuneiform.py`
Single-sentence cuneiform translation via temp file. Key modifications:

- **UTF-8 encoding**: Added `encoding="utf-8"` to the temp file write (`cuneiform.tmp`), fixing `UnicodeEncodeError` on Windows when writing cuneiform Unicode characters.
- Writes input to `cuneiform.tmp`, calls `translate_cuneiform_base()`, and removes the temp file after translation.

#### `akkadian/translate_transliteration.py`
Single-sentence transliteration translation via temp file. Same pattern as `translate_cuneiform.py`:

- Writes input to `transliteration.tmp`, calls `translate_transliteration_base()`, and removes the temp file after translation.

### 2. New Scripts Created

#### `repair_checkpoints.py`
Utility to repair Fairseq `.pt` checkpoint files that have missing or corrupted metadata. Injects the correct architecture and task settings:

- Architecture: `fconv` (convolutional sequence-to-sequence, **not** transformer)
- Task: `translation`
- Settings: `share_all_embeddings=False`, `criterion='label_smoothed_cross_entropy'`
- Uses `torch.load` / `torch.save` with `argparse.Namespace` to patch checkpoint args.
- Repairs both checkpoint files: `not_divided_by_three_dots_result.LR_0.1.MAX_TOKENS_4000/checkpoint_best.pt` (cuneiform→en) and `trans_result.LR_0.1.MAX_TOKENS_4000/checkpoint_best.pt` (transliteration→en).

#### `batch_translate.py`
Batch translator for processing entire folders of `.txt` files:

- Menu-driven: option 1 = cuneiform sign translation, option 2 = transliteration-to-English.
- Iterates all `.txt` files in a user-specified input folder and writes results to a `results/` output folder (created at runtime).
- Uses `sys.path` manipulation to import from the `akkadian/` package.

#### `translate_all_formats.py`
Multi-model comparison tool that transliterates cuneiform signs using all available models side-by-side:

- Runs BiLSTM, HMM, MEMM, and a Combined classifier (gamma1=0.4, gamma2=0.2).
- Highlights disputed signs where models disagree on the reading.
- Logs detailed comparison results to `full_comparison_log.txt`.

#### `translate_interactive.py`
REPL-style interactive translator powered by BiLSTM:

- Continuously accepts cuneiform input and prints transliteration output.
- Logs all translations with timestamps to `translation_log.txt`.
- Type `quit` or `exit` to stop.

#### `test_akkadian.py`
Quick smoke test for BiLSTM transliteration:

- Tests on sample cuneiform signs to verify the model loads and produces output.
- Useful for validating the environment is correctly set up.

### 3. Modified Model & Project Files

#### Fairseq Checkpoint Files (`.pt`)
The two model checkpoint files were repaired using `repair_checkpoints.py`:

- `not_divided_by_three_dots_result.LR_0.1.MAX_TOKENS_4000/checkpoint_best.pt` — cuneiform→English model
- `trans_result.LR_0.1.MAX_TOKENS_4000/checkpoint_best.pt` — transliteration→English model

Both had their internal metadata corrected to specify `fconv` architecture (convolutional seq2seq) and proper source/target language codes (`ak`→`en` and `tr`→`en` respectively).

#### Virtual Environment
A Python virtual environment (`venv/`) is included in the repository with all required dependencies pre-installed (allennlp, spacy, scipy, fairseq, etc.). PyTorch (`torch`) is excluded from the committed venv because its CUDA/cuDNN DLLs exceed GitHub's 100 MB per-file limit (~4 GB). After cloning, users only need to activate the venv and install torch (see the "Included Virtual Environment" section above). A fully pinned `requirements_pinned.txt` is also provided for reference.

### 4. Temporary and Output Files & Directories

| Path | Purpose |
|------|---------|
| `tmp/` | Working directory for temporary files created during translation (auto-created by scripts via `os.makedirs`) |
| `results/` | Output directory for batch translations (created at runtime by `batch_translate.py`) |
| `input_texts/` | Folder for placing input `.txt` files for batch translation |
| `antiochus.txt` | Sample cuneiform test input (Antiochus inscription) |
| `babylonking.txt` | Sample cuneiform test input (Babylonian king inscription) |
| `translation_log.txt` | Automatic log of interactive translations with timestamps |
| `translation_log_comparison.txt` | Log of translation comparisons |
| `full_comparison_log.txt` | Detailed multi-model comparison log from `translate_all_formats.py` |

## Project Structure

**Root-level scripts**:

	batch_translate.py: Batch translator for processing folders of cuneiform or transliteration text files.
	
	translate_all_formats.py: Multi-model comparison tool (BiLSTM, HMM, MEMM, Combined) with disputed-sign highlighting.
	
	translate_interactive.py: Interactive REPL translator with automatic logging to translation_log.txt.
	
	test_akkadian.py: Quick smoke test for BiLSTM transliteration on sample cuneiform signs.
	
	repair_checkpoints.py: Utility to repair Fairseq checkpoint metadata (architecture, language settings).

**BiLSTM_input**: 

	Contains dictionaries used for transliteration by BiLSTM.

**NMT_input**:

	Contains dictionaries used for natural machine translation.

**input_texts**:

	Folder for placing input text files for batch translation.

**tmp**:

	Working directory for temporary files created during Fairseq translation subprocess calls.

**akkadian.egg-info**:

	Information and settings for akkadian python package.
	
**akkadian**:

	Sources and train's output.
	
	output:	Train's output for HMM, MEMM and BiLSTM - mostly pickles.
		
	__init__.py: Init script for akkadian python package. Initializes global variables.
	
	bilstm.py: Class for BiLSTM train and prediction using AllenNLP implementation.
	
	build_data.py: Code for organizing the data in dictionaries.
	
	check_translation.py: Code for translation accuracy checking.
	
	combine_algorithms.py: Code for prediction using both HMM, MEMM and BiLSTM.
	
	data.py: Utils for accuracy checks and dictionaries interpretations.
	
	full_translation_build_data.py: Code for organizing the data for full translation task.
	
	get_texts_details.py: Util for getting more information about the text.
	
	hmm.py: Implementation of HMM for train and prediction.
	
	memm.py: Implementation of MEMM for train and prediction.
	
	parse_json: Json parsing used for data organizing.
	
	parse_xml.py: XML parsing used for data organizing.
	
	train.py: API for training all 3 algorithms and store the output.
	
	translation_tokenize.py: Code for tokenization of translation task.
	
	translate_cuneiform.py: Translates cuneiform sentences to English via Fairseq NMT (UTF-8 encoding fix applied).
	
	translate_from_cuneiform.py: File-based cuneiform-to-English translation with Windows compatibility and Fairseq diagnostics.
	
	translate_from_transliteration.py: File-based transliteration-to-English translation with input normalization and Windows compatibility.
	
	translate_transliteration.py: Translates transliteration sentences to English via Fairseq NMT.
	
	transliterate.py: API for transliterating using all 3 algorithms.

**not_divided_by_three_dots_result.LR_0.1.MAX_TOKENS_4000**:

	Contains the trained Fairseq fconv checkpoint for cuneiform→English translation (checkpoint_best.pt).

**trans_result.LR_0.1.MAX_TOKENS_4000**:

	Contains the trained Fairseq fconv checkpoint for transliteration→English translation (checkpoint_best.pt).

**data-bin-not-divided-by-three-dots**:

	Binarized Fairseq training data for cuneiform→English translation.

**data-bin-transliteration**:

	Binarized Fairseq training data for transliteration→English translation.

**venv**:

	Pre-built Python virtual environment committed to the repository. Contains all project dependencies except PyTorch (which must be installed after cloning due to GitHub file size limits). This eliminates the need to manually resolve complex version dependencies.
	
**build/lib/akkadian**:

	Information and settings for akkadian python package.
	
**dist**:

	Akkadian python package - wheel and tar.
	
**raw_data**:

	Databases used for training the models:
	
	RINAP 1, 3-5
	
	Additional databases for future training:
		
	RIAO
		
	RIBO
		
	SAAO
		
	SUHU
		
	Miscellanea:
	
	tei - the same databases (RINAP, RIAO, RIBO, SAAO, SUHU) in XML/TEI format.
	
	random - 4 texts used for testing texts outside of the training corpora. They were randomly selected from RIAO and RIBO.
		
# Licensing

This repository is made freely available under the Attribution-ShareAlike 3.0 Unported (CC BY-SA 3.0) license. This means you are free to share and adapt the code and datasets, under the conditions that you cite the project appropriately, note any changes you have made to the original code and datasets, and if you are redistributing the project or a part thereof, you must release it under the same license or a similar one.

For more information about the license, see [here](<https://creativecommons.org/licenses/by-sa/3.0/>).

# Issues and Bugs

If you are experiencing any issues with the website, the python package akkadian or the git repository, please contact us at dhl.arieluni@gmail.com, and we would gladly assist you. We would also much appreciate feedback about using the code via the website or the python package, or about the repository itself, so please send us any comments or suggestions.

### Authors
* Gai Gutherz
* Ariel Elazary
* Avital Romach
* Shai Gordin
