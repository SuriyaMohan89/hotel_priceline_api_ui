# Hotel Grid UI using Priceline API

This is UI only project with a jab at adaptive UI and flex and bootstrap. The input comes from a static priceline API and the UI is rendered using the grid layout.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites and Installing

You need python. Once you have python, please make sure you have [pip](https://pip.pypa.io/en/stable/installing/). Once you have both python and pip, please follow the below steps


```
cd <git_clone_or_unzip_directory>
pip install -r requirements.txt
python server.py
```

Your server will be running in port ** 5000 **
Try localhost:5000 to see it running.

## Screenshots

*Please note that during snapshotting screenshots, the API wasn't sending some hotel's images, hence the screenshot has some thumbnail images missing. Apologies, will fix it later.*

### Homepage

<img width="875" alt="screen shot 2018-08-05 at 11 00 38 pm" src="https://user-images.githubusercontent.com/36581704/43699437-98b2deea-9903-11e8-8232-328db9119827.png">

### Adaptive css
<img width="369" alt="screen shot 2018-08-05 at 11 01 10 pm" src="https://user-images.githubusercontent.com/36581704/43699478-c0eacf58-9903-11e8-81f4-f66c1b580c3c.png">

### Dropdown
<img width="883" alt="screen shot 2018-08-05 at 11 01 29 pm" src="https://user-images.githubusercontent.com/36581704/43699490-ce690e24-9903-11e8-803a-a677e8dc8403.png">

## Known issue

The adaptive css overflows sometimes upon resizing. This is due to a pragmatic hack in the code, working on refactoring and removing this.
