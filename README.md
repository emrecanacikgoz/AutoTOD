# AutoTOD emrecan version

AutoTOD is a novel fully zero-shot autonomous agent for task-oriented dialogues. It deprecates all the delicate modules in traditional TOD systems and only uses an instruction-following language model to autonomously call external APIs and communicate with the user, which greatly reduces the construction cost and improves the generalization ability.

# Requirements
```bash
conda create --name autotod python=3.10 -y
conda activate autotod
pipi install -r requirments.txt
```

# Run User Simulator

## 1. Download preprocessed data

Download the preprocessed data from [Google Drive](https://drive.google.com/file/d/18ULn5nmzMMM9dMgGvtdybYcKniwdE3dL/view?usp=sharing) and extract it to the `data` directory.

## 2. Set OpenAI API Key

Provide the `OPENAI_API_KEY` in the environment variable.

```bash
export OPENAI_API_KEY=<your api key>
```
**Warning:** Only support openai, please open pr for AzureOpenAI versions.

# Run User Simulator
```bash
python user.py --data_path <path/to/data/autotod-data/mwoz/origin/data.json> --model gpt-3.5-turbo
```
# Get User Simulator Evalution Results
To get evalution results, you should run:
```bash
python run_multiwoz.py --model gpt-3.5-turbo --user_simulator_prompt_path user_simulator_prompt.txt
```
Please modify **user_simulator_prompt.txt** for changing the user simulator prompt.
