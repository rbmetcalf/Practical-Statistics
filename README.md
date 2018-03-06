#Intalling jupyter

From the command line in your home directory:

install jupyter

```
pip intall jupyter --user
```
Make an alias for jupter

```
pico ~/.bash_aliases
```
add the line

```
alias jupyter='~/.local/bin/jupyter'
```
and then save the file. (Ctr-x)

Then type:

```
source .bashrc
```

To start jupyter:

```
jupyter notebook
```