# Voice Cloning

A deep learning system for real-time voice cloning. This project provides an implementation of a neural voice cloning system that allows you to clone a voice from a few seconds of audio and generate speech in that voice.

## Project Overview

This voice cloning system consists of three independent components:

1. **Encoder** - A speaker encoder that generates a fixed-length embedding vector from a few seconds of speech
2. **Synthesizer** - A sequence-to-sequence model that converts text to a mel spectrogram, conditioned on the speaker embedding
3. **Vocoder** - A neural vocoder that converts mel spectrograms to waveforms

The project is based on the SV2TTS (Speaker Voice to Text-to-Speech) architecture, which enables few-shot voice cloning.

## Features

- Clone a voice from as little as 5 seconds of audio
- Synthesize speech in real-time
- User-friendly toolbox with GUI for quick experimentation
- Command-line interface for batch processing
- Pretrained models included
- Full training pipeline for custom models

## Installation

### Requirements
- Python 3.6 or higher
- PyTorch 1.0 or higher
- CUDA (optional for GPU support)

### Setup

1. Clone the repository
   ```bash
   git clone https://github.com/yourusername/Voice-Cloning.git
   cd Voice-Cloning
   ```

2. Create a virtual environment (optional but recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\\Scripts\\activate
   ```

3. Install the required packages
   ```bash
   pip install -r requirements.txt
   ```

4. **Download Pretrained Models**
   
   The pretrained models are too large for GitHub and must be downloaded separately. Please download them from the Google Drive link below:
   
   [Download Pretrained Models](https://drive.google.com/drive/folders/your_folder_id_here)
   
   After downloading, create a directory structure as follows:
   ```
   saved_models/
      default/
         encoder.pt     (~ 16 MB)
         synthesizer.pt (~ 353 MB)
         vocoder.pt     (~ 51 MB)
   ```
   
   Place the downloaded model files in the appropriate directory as shown above.

## Usage

### Using the Toolbox (GUI)

The toolbox provides a graphical interface that allows you to:
- Record or load utterances to clone a voice
- Synthesize speech from text with the cloned voice
- Visualize speaker embeddings and spectrograms

To launch the toolbox:

```bash
python demo_toolbox.py
```

Optional arguments:
- `--cpu`: Use CPU for inference (default uses GPU if available)
- `--seed`: Set a random seed for deterministic results
- `--models_dir`: Path to the directory containing models (default: saved_models)
- `--datasets_root`: Path to datasets directory (default: dataset)

### Using the Command Line Interface

For batch processing or scripted usage, use the CLI:

```bash
python demo_cli.py --text "Hello, this is a test." --weights_path saved_models/default/
```

## Training Your Own Models

### Data Preparation

1. Prepare datasets for the encoder:
   ```bash
   python encoder_preprocess.py --datasets_root=<datasets_root> --datasets=<dataset1,dataset2,...>
   ```

2. Prepare datasets for the synthesizer:
   ```bash
   python synthesizer_preprocess_audio.py --datasets_root=<datasets_root> --datasets=<dataset1,dataset2,...>
   python synthesizer_preprocess_embeds.py --synthesizer_root=<synthesizer_output_dir> --encoder_model_fpath=<encoder_model.pt>
   ```

3. Prepare datasets for the vocoder:
   ```bash
   python vocoder_preprocess.py --datasets_root=<datasets_root>
   ```

### Training

1. Train the encoder:
   ```bash
   python encoder_train.py --run_id=<run_name> --clean_data_root=<encoder_dataset_root>
   ```

2. Train the synthesizer:
   ```bash
   python synthesizer_train.py <run_id> <synthesizer_dataset_root> --models_dir=<models_dir>
   ```

3. Train the vocoder:
   ```bash
   python vocoder_train.py <run_id> <vocoder_dataset_root> --models_dir=<models_dir>
   ```

## Architecture

### Encoder
The encoder is based on the GE2E (Generalized End-to-End) loss model, which maps variable-length speech utterances to fixed-length embeddings that capture speaker characteristics.

### Synthesizer
The synthesizer is based on Tacotron 2, a sequence-to-sequence model with attention that generates mel spectrograms from text, conditioned on speaker embeddings.

### Vocoder
The vocoder is based on WaveRNN, which generates high-quality waveforms from mel spectrograms in real-time.

## Pretrained Models

This repository typically includes pretrained models, but due to GitHub file size limitations, they are now hosted separately. Please see the Installation section for download instructions.

Model specifications:
- Encoder trained on LibriSpeech and VoxCeleb datasets
- Synthesizer trained on the LibriSpeech dataset
- WaveRNN vocoder trained on the LibriSpeech dataset

## Sample Audio Files

The audio files in the samples folder are provided for toolbox testing and benchmarking purposes. These are the same reference utterances used by the SV2TTS authors to generate the audio samples.

The `p240_00000.mp3` and `p260_00000.mp3` files are compressed versions of audios from the VCTK corpus.
The `1320_00000.mp3`, `3575_00000.mp3`, `6829_00000.mp3` and `8230_00000.mp3` files are compressed versions of audios from the LibriSpeech dataset.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- This project is based on the SV2TTS framework
- The implementation is inspired by research from:
  - [Transfer Learning from Speaker Verification to Multispeaker Text-To-Speech Synthesis](https://arxiv.org/abs/1806.04558)
  - [Natural TTS Synthesis by Conditioning WaveNet on Mel Spectrogram Predictions](https://arxiv.org/abs/1712.05884)
  - [Efficient Neural Audio Synthesis](https://arxiv.org/abs/1802.08435)
