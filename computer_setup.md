# Environment preparation
Step-by-step instructions to prepare your laptop for the introductory tutorials.


1. Get a laptop
2. If you don't have it yet, install [Anaconda - python 3.7](https://www.anaconda.com/distribution/). Install for your user only and choose as location C:/Users/{username}/anaconda3
3. Make sure you have something installed to handle your GitHub business - [GitKraken](https://www.gitkraken.com), 
[Fork](https://git-fork.com), [Turtuoise git](https://tortoisegit.org)
4. Clone the stytra_hackathon repo (recommended folder to clone into: (C:)/Users/{username}/python_code/)
5. Inside the repo, locate the `environment.yml` file (you can also find it in the [lab-docs repo](https://raw.githubusercontent.com/portugueslab/lab-docs/master/environment.yml))
6. Open a shell or the anaconda prompt
7. Navigate (with `cd`) to the `environment.yml` file
8. Type:
    ```
      conda env create -f {path to the envinroment.yml file}
    ```
9. Now activate the environment with
    ```
      conda activate rplab
    ```
    Note that if you close the prompt, you will have to activate again the environmwnt to use it!
10. Clone the stytra repository (recommended folder to clone into: (C:)/Users/{username}/python_code/)
11. from the terminal (with the activated environment)
    ```
    pip install -e {path to stytra}
    ```
