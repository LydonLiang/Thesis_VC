# Thesis_VC
This project is based on the [FastSpeech2 implementation](https://github.com/ming024/FastSpeech2) by Ming24.

The code has been modified and adapted for a cross-lingual voice conversion task, specifically between **Taiwanese Mandarin** and **American English**. It includes adjustments to training pipelines, phoneme processing, and prosody integration to support bilingual voice synthesis.

## Datasets

This project uses a subset of the following publicly available datasets:

- **Taiwanese Mandarin (Common Voice subset)**  
  Download from: [https://commonvoice.mozilla.org/zh-TW/datasets](https://commonvoice.mozilla.org/zh-TW/datasets) (the June 24th 2019 version)
  
Citation:
  > Ardila, R., Branson, M., Davis, K., Kohler, M., Meyer, J., Henretty, M., ... & Church, K. (2020). Common Voice: A massively-multilingual speech corpus. In *Proceedings of LREC*.

- **American English (LJSpeech)**  
  Download from: [https://keithito.com/LJ-Speech-Dataset/](https://keithito.com/LJ-Speech-Dataset/)
  
Citation:
  > Ito, K. (2017). The LJ Speech Dataset. [https://keithito.com/LJ-Speech-Dataset/](https://keithito.com/LJ-Speech-Dataset/)

## Resources  
To reproduce the experiments and inference results, the following preprocessed resources are available for download:

[Download Resources (checkpoint, TextGrid, label files, split lists)] (https://drive.google.com/drive/folders/1WF3kUR9l9YqVOvrRiMphB7YKJCrHpPnf?usp=sharing)

Contents include:

 `checkpoint_50000.pth`
  Trained FastSpeech2 model checkpoint for cross-lingual voice conversion between Taiwanese Mandarin and American English.

  `TextGrid/`  
  Phoneme-level alignments generated using Montreal Forced Aligner (MFA), for both Common Voice and LJSpeech subsets.

  `lab/`  
  Original `.lab` label files and processed phoneme/token sequences used during training and inference.

 `filelists/`
  Subset lists (`train.txt`, `val.txt`, `merged.txt`) specifying selected utterances used in the project.

## Inference

To run inference, please enter the following command in your terminal:

```bash
python3 synthesize.py \
  --restore_step 50000 \
  --mode batch \
  --source /[your path]/merged.txt\
  -p /config/Common_voice/preprocess.yaml \
  -m /config/Common_voice/model.yaml \
  -t /config/Common_voice/train.yaml
```

## Disclaimer

This repository is developed as part of a master's thesis project in the field of speech technology.  
It is intended solely for academic and research purposes. The code, configurations, and processed resources are provided "as is" without any warranty.

Please note:
- The original codebase is based on [ming024/FastSpeech2](https://github.com/ming024/FastSpeech2) and modified for cross-lingual voice conversion.
- This repository does not include any copyrighted or proprietary audio files.
- All datasets referenced (Common Voice, LJSpeech) are publicly available and used under their respective licenses.
- Any errors, modifications, or results presented here are solely the responsibility of the author and do not represent the views of the original authors or affiliated institutions.

If you use or adapt this work, please provide appropriate credit.


