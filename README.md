# DOE 23 Discord bot
![discord bot](https://miro.medium.com/v2/resize:fit:481/1*yKCbOTFZ5yQmQCOPt8PX4g.jpeg)

- [How to participate](#how-to-participate)
- [Things to keep in mind](#things-to-keep-in-mind)


## Dev Setup
1. Clone the repo from `main`
2. Switch to /create a new branch in Gitbash or on the repo and switch to it.
3. Set up your virtual environment and install all packages from `requirements.txt`
    * Go to root directory of the cloned repo
    * Run `$ python -m venv <venv>`
    * To activate your venv, run:
        *  Linux terminal: `$ source <venv>/bin/activate`
        *  Windows PS: `PS> <venv>\Scripts\Activate.ps1`
4. Run `$ pip install -r requirements.txt`
5. Everything should be good to go. If you have any problems message me on discord `@soup`

---

## Things to keep in mind

**`TRY YOUR PYTHON LOGIC LOCALLY AND AVOID THE DISCORD MODULE`**
> When working with the discord bot there can be problems if multiple people start and stop the discord bot, try to `user_input = Input('Write human interaction here: ')` or write test cases to simulate how it will react when a user interacts with the bot from discord. Because *(spoiler)* you 90% of the time, the discord module will only send and read strings from the discord client.

---

**`WHEN YOU WORK WITH A NEW FEATURE/BUG CREATE A SEPARATE BRANCH FOR IT`**
> This is just to avoid everyone pushing to `main`.

---

**`BEFORE CREATING A PULL REQUEST, MAKE SURE IT IS COMPATIBLE WITH`** `main`
> This is to avoid complicated merge conflicts.
> 1. `$ git checkout main`
> 2. `$ git pull`
> 3. `$ git checkout <your-branch>`
> 4. `$ git merge main`
> 5. Check if your code still works and fix potential issues/merge conflicts.
> 6. Done!

---

**`WHEN MAKING A PULL REQUEST, WRITE A SHORT DESCRIPTION OF WHAT YOU'VE DONE`**
> This is just to make each pull request easy to handle. If you've implemented a command that users can call, then please specify it. 

