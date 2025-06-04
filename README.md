# Thesis_VC
This project is based on the [FastSpeech2 implementation](https://github.com/ming024/FastSpeech2) by Ming24.

The code has been modified and adapted for a cross-lingual voice conversion task, specifically between **Taiwan Mandarin** and **American English**. It includes adjustments to training pipelines, phoneme processing, and prosody integration to support bilingual voice synthesis.

## Datasets

To reproduce the experiments, the following datasets are required (all the needed data had been zipped as one folder):

- **Thesis_commonvoice**  
  Download from: [https://drive.google.com/file/d/1NtGghWkhH1E183XI3yPX_9w-SpBwhWu3/view?usp=sharing)
Make sure to preprocess the datasets according to the structure defined in the `preprocessed_data/` folder and follow the alignment instructions using MFA.

## Inference

To run inference, please enter the following command in your terminal:

```bash
python3 synthesize.py \
  --restore_step 50000 \
  --mode batch \
  --source /Thesis_commonvoice/inference_sentence/tw_inference_phonemized.txt\
  -p /config/Common_voice/preprocess.yaml \
  -m /config/Common_voice/model.yaml \
  -t /config/Common_voice/train.yaml
```

## Disclaimer

This repository is currently under development as part of an academic thesis. Feel free to use or modify the code, but please provide appropriate credit.


