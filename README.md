<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/github_username/repo_name">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Med Object Detection: Drink or Dose</h3>

  <p align="center">
    build during Botnoi internship

    Using AI to detect an object in the video and recognize the object whether ti is drink or dose.
</p>
</div>


## Tech Stack
### Code Editor
![Google Colab](https://img.shields.io/badge/Colab-F9AB00?style=for-the-badge&logo=googlecolab&color=525252) ![VS Code](https://img.shields.io/badge/Visual_Studio_Code-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white)  
### Languages, Libraries, and Framework
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)  ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white) ![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![OpenCV](https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white) ![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white) ![YOLO Badge](https://img.shields.io/badge/YOLO-0FF?logo=yolo&logoColor=000&style=for-the-badge)

## Dataset
### Detail
- **Data Format:** Video.mp4
- **Tool for labeling:** Roboflow
- **Number of Classes:** 2, Drink and Dose
### Data Split
- ***Train:*** 648
- ***Valid:*** 176
- ***Test:*** 115

## Run the program (app.py)
to use with video
```shell
python3 app.py --media "video" --video "sample_2.mp4"
```
to use real time
```shell
 python3 app.py --media "live"
```

## Contribution
@pangineering
