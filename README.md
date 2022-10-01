# Jira CLI 

![Jira CLI](jira_logo.png)

The Jira CLI allows you to configure and manage your Jira instance using simple commands from your terminal.

## Setup

We strongly recommend that you use either a docker container or a python virtual environment to separate your configuration from your host.

To use a virtual environment, you can follow the steps below.

Where possible, we're going to use `make`, which wraps up some standard commands for us and helps us run through the same steps every time. Standardization comes in handy.

First, we need to set up and activate the virtual environment.

```shell
make setup
source .venv/bin/activate
```

After this, we are going to install our dependencies.
> Note: You have to have your virtual environment activated before running this command.

```shell
make install
```

There is a file called .example.env that contains a template for environment variables that are going to be used by the CLI. Using make, we're going to copy it, and then you should fill it in with values for your instance of Jira.

```shell
make environment
```
