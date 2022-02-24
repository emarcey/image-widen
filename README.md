# Image Widen

Little utility to widen square images with a white background to appease our Notion docs

## Run with local image

1. Put your original image in the `originals` folder
1. Run `python main.py --original_file={name of your file, without directory}`, e.g. `python main.py --original_file=guang.jpg`
1. Output will be placed in `modified` folder


## Run from url

1. Run `python main.py --original_url={name of your file, without directory}`, e.g. `python main.py --original_url="https://media-exp1.licdn.com/dms/image/C4D03AQE5cgP4rzpHeQ/profile-displayphoto-shrink_200_200/0/1628015750830?e=1651104000&v=beta&t=aQ51hfnG_i7wca_wePFHiubG1o0Wxi1HQHdI0Vg_iWo"`
1. Output will be placed in `modified` folder