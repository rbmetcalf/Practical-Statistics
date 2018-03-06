#Intalling jupyter

If you would like to install jupyter on your computer we recommend installing [Anaconda](https://www.anaconda.com/download/#macos).  It will have a simple way of launching jupyter.

On the UNIBO system you need to:

From the command line in your home directory:

1) install jupyter

```
pip intall jupyter --user
```
2) Make an alias for jupter so that you don't need to type in the path every time you start it.

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