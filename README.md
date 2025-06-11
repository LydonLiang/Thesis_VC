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
  
## Inference

To run inference, please enter the following command in your terminal:

```bash
python3 synthesize.py \
  --restore_step 50000 \
  --mode batch \
  --source /Thesis_commonvoice/inference_sentence/merged.txt\
  -p /config/Common_voice/preprocess.yaml \
  -m /config/Common_voice/model.yaml \
  -t /config/Common_voice/train.yaml
```
### Checkpoint

To reproduce the inference results, please download the pre-trained checkpoint from the following link:

➡️ [Download checkpoint (step 50000)](https://drive.google.com/drive/folders/1WF3kUR9l9YqVOvrRiMphB7YKJCrHpPnf?usp=sharing) 

## Disclaimer

This repository is currently under development as part of an academic thesis. Feel free to use or modify the code, but please provide appropriate credit.


