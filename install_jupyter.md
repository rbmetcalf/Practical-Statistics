#Installing Python and Jupyter Notebooks

If you would like to install python on your computer I recommend installing [Minconda](https://docs.anaconda.com/miniconda/) or [Anaconda](https://www.anaconda.com/download/#macos).  It also has a simple a simple jupyter notebooks editor that works in a browser.  

However, I recommend editing and running jupyter notebooks with microsoft's [VS Code](https://code.visualstudio.com/download).  You can also run notebooks in google's [Colab](https://colab.research.google.com) which requires not installation or notebooks.


On the UNIBO system you need to:

From the command line in your home directory:

1) install jupyter

```
pip install jupyter --user
```
2) Make an alias for jupyter so that you don't need to type in the path every time you start it.

Create and open this file

```
pico ~/.bash_aliases
```
In the pico editor add the line

```
alias jupyter='~/.local/bin/jupyter'
```
and then save the file. (Ctr-x)


Now you need to re-source your .bashrc file.  Type 

```
source .bashrc
```
If all went well you should be able to start with jupyter:

```
jupyter notebook
```
