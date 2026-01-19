# Quran Recitation Classification using Wav2Vec 2.0

This project implements a deep learning pipeline to classify Quranic recitations (Surahs) using a fine-tuned **Wav2Vec 2.0** model. The workflow includes audio preprocessing (silence removal), dataset cleaning, contrastive learning (Triplet Loss), and visualization of embeddings using t-SNE.

## 📋 Prerequisites

### System Requirements

* **Python 3.8+**
* **FFmpeg**: Required for audio processing with `pydub` and `torchaudio`.
* *Ubuntu:* `sudo apt install ffmpeg`
* *Windows:* Download and add to system PATH.



### Python Libraries

Install the required dependencies using pip:

```bash
pip install torch torchaudio transformers pydub pandas numpy scikit-learn matplotlib seaborn tqdm audiomentations jupyter

```

---

## 🚀 Usage Pipeline

Follow these steps strictly to reproduce the dataset processing, training, and evaluation results.

### 1. Download Dataset

Download the Quranic Multi-Reciter Dataset from OpenSLR.

* **Link:** [https://www.openslr.org/132/](https://www.openslr.org/132/)
* **Action:** Download and extract the dataset. Rename the root folder of the extracted files to `audio_data` (or ensure the scripts point to the correct location).

### 2. Filter Dataset Range

Run the script to remove files outside the target range (e.g., keeping only early Surahs or specific ranges defined in the script).

```bash
python mp3_delete.py

```

### 3. Audio Preprocessing (Silence Removal)

Process the raw audio to remove silence, normalizing the input for the model.

```bash
python remove_silence.py

```

* *Effect:* Deletes MP3 files with numerical names outside the range `1002` to `77050`.

### 4. Remove Specific Artifacts

Run the script to delete specific files (e.g., `001001.mp3`, often the Basmalah) that might cause class overlap.

```bash
python delete_01.py

```

* *Input:* `audio_data/`
* *Output:* Creates a new directory `audio_data_processed/` containing the cleaned audio.
* *Note:* Ensure the `INPUT_DIR` variable in the script matches your raw dataset location.

### 5. Dataset Statistics

Analyze the processed dataset to compare original vs. post-processed statistics (duration, clip counts).

* **Open and Run:** `dataset_visual.ipynb`
* *Output:* Displays a comparison table of the dataset metrics.

### 6. Train the Model (Contrastive Learning)

Perform fine-tuning on the Wav2Vec 2.0 model using Contrastive Learning (Triplet Margin Loss).

* **Open and Run:** `contrastive_first.ipynb`
* *Process:*
* Loads `audio_data_processed`.
* Fine-tunes the top 2 layers of Wav2Vec 2.0.
* Trains a Projection Head using Triplet Loss.
* Evaluates using k-NN (Baseline) and MLP classifiers.



### 7. Visualization & Final Evaluation

Visualize the resulting embeddings and decision boundaries.

* **Open and Run:** `visualization.ipynb`
* *Process:*
* Extracts embeddings from the Test Set.
* Runs **t-SNE** to project high-dimensional embeddings into 2D.
* Generates `comparison_tsne_knn_mlp.png` comparing Ground Truth vs. k-NN vs. MLP predictions.



---

## 📂 File Descriptions

| File Name | Description |
| --- | --- |
| **`mp3_delete.py`** | Utility script to bulk delete MP3 files based on a specific numerical range (e.g., to reduce dataset size). |
| **`remove_silence.py`** | Preprocessing script using `pydub` to split audio on silence and merge non-silent chunks. |
| **`delete_01.py`** | Utility script to remove a specific file (`001001.mp3`) across all subdirectories. |
| **`dataset_visual.ipynb`** | Notebook for calculating and displaying dataset statistics (duration, file counts) before and after augmentation logic. |
| **`contrastive_first.ipynb`** | **Main Training Notebook.** Handles data loading, Triplet Dataset creation, and Wav2Vec 2.0 fine-tuning. |
| **`visualization.ipynb`** | **Demo/Inference Notebook.** Replicates the full evaluation pipeline and produces t-SNE visualizations. |
| **`contrastive_final.ipynb`** | (Optional) An alternate/final version of the training notebook containing refined logic or evaluation steps. |

---

## 📊 Results

After running Step 7 (`visualization.ipynb`), you will generate a visualization similar to the one below, showing how well the model clusters different Surahs:

* **Output File:** `comparison_tsne_knn_mlp.png`

* **Metrics:** Accuracy scores for k-NN and MLP classifiers are printed at the end of the notebook.

