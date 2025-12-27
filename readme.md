🏏 **Cricket Ball Detection \& Trajectory Tracking**



EdgeFleet.ai – AI/ML Engineering Assessment



📌 **Problem Statement**



Build a complete computer vision system to detect and track a cricket ball in videos captured from a single, fixed camera, and output:



Per-frame ball centroid annotations



A processed video with trajectory overlay



Fully reproducible training and inference code



✅ **Key Features**



Small-object detection using YOLOv8-N



Robust tracking under occlusion, motion blur, and missed detections



Per-frame CSV annotations: (frame\_index, x, y, visibility)



Trajectory visualization overlayed on video



CPU-friendly, deployment-ready pipeline



📂 **Repository Structure**

EdgeFleet\_Project/

│

├── code/

│   ├── image\_annotation.py      # Manual annotation tool (OpenCV click-based)

│   ├── yolo\_trainer.py          # YOLO training script + hyperparameters

│   └── model\_pipeline.py        # Detection + tracking + CSV/video output

│

├── dataset\_kaggle/

│   ├── train/

│   ├── val/

│   ├── test/

│   └── kaggle\_source\_screenshots/

│

├── raw\_videos/                  # Input videos (single static camera)

│

├── models/

│   └── final.pt                 # Best YOLO model used for inference

│

├── yolo\_robust\_model/

│   ├── weights/

│   │   ├── best.pt              # Best validation checkpoint

│   │   └── last.pt              # Final epoch checkpoint

│   ├── results.csv

│   ├── confusion\_matrix.png

│   ├── BoxP\_curve.png

│   ├── BoxR\_curve.png

│   └── training \& validation visualizations

│

├── outputs/

│   ├── \*.csv                    # Per-frame centroid annotations

│   └── \*.mp4                    # Processed videos with trajectory overlay

│

└── README.md



🧠 **Dataset Preparation**



Initial dataset sourced from Kaggle contained noisy and incorrect labels



Images were manually curated and cleaned



Additional screenshots extracted from match videos to improve variation



~300 images manually annotated using a custom OpenCV click-based tool



Final dataset favored quality over quantity, significantly improving stability



🧪 **Model Training**



Model: YOLOv8-Nano (lightweight, fast, CPU-deployable)



Input Resolution: 960 × 960



Optimizer: AdamW



LR Scheduler: Cosine Annealing



Epochs: 100



All training artifacts (metrics, curves, confusion matrices, checkpoints) are stored in

yolo\_robust\_model/.



The best checkpoint (best.pt) was copied to models/final.pt for clean inference usage.



🔁 **Tracking Pipeline (Core Logic)**



Detection alone is insufficient for cricket ball tracking due to:



Motion blur



Occlusion by players/bat



Missed detections across frames



To address this, a hybrid tracking strategy is used:



YOLO detection as primary signal



Motion-based gating to reject false jumps



Optical flow fallback during short occlusions



Short extrapolation for missed frames



Interpolation to stabilize trajectory



Hard jump constraints to prevent flickering



This produces a stable and realistic ball trajectory without relying on physics assumptions.



▶️ **Running Inference**

1\. Install Dependencies

pip install ultralytics opencv-python numpy tqdm



2\. Run Pipeline

python code/model\_pipeline.py \\

&nbsp; --model models/final.pt \\

&nbsp; --video raw\_videos/input.mp4 \\

&nbsp; --output outputs/



📤 **Output Format**

CSV (per video)

frame\_index, x\_centroid, y\_centroid, visibility



Video



Ball centroid drawn per frame



Trajectory path overlayed



🔬 **Reproducibility**



Fully deterministic inference



No cloud or Colab dependency



Clear separation between training, inference, and outputs



All scripts runnable locally



⚠️ **Limitations \& Future Work**



Multi-camera fusion for depth estimation



Higher FPS input for smoother trajectories



Ball spin and bounce behavior modeling



🏁 **Summary**



This project demonstrates an end-to-end production-style CV pipeline, combining:



Careful dataset curation



Lightweight model training



Robust post-processing logic



Clean, reproducible engineering



📎 **Notes**



yolo\_robust\_model/ contains training evidence, not runtime code



models/final.pt is the only model used during inference

