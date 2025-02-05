
## Discord interactions
![discord bot picture](https://www.jsnsmn.com/static/6cbe958fa92b1051f547c88386a6c3a6/b4748/143c4584-3731-440a-b1ff-9286bb22249b.png)

When working with the discord interactions there are certain things you can do with it such as slash commands *(writing `/` in chat and get a list of commands)* to perform different actions. Here are a few examples

Also do keep in mind that discord uses a *markdown-like* language, therefor, when you want to format text such as *italic* or **bold** you can write your messages as you would in a `.md` file. If uncertain on the syntax check this [guide](https://support.discord.com/hc/en-us/articles/210298617-Markdown-Text-101-Chat-Formatting-Bold-Italic-Underline).

- [Discord interactions](#discord-interactions)
  - [Send Message](#send-message)
  - [Slash Commands](#slash-commands)
    - [Explanation](#explanation)

---

### Send Message
> [Official Documentation](https://discord.com/developers/docs/interactions/receiving-and-responding)

If you want to send a message from the bot you need a way to reference where the bot should respond from. The important part here is that it depends on where you got your message from.

Here are a few exampels:
```py
# --- When someone has written something in chat --- #
async def on_message(message: discord.message.Message)
    await message.channel.send("<text here>")

# --- From slash commands --- #
async def slash_command(interaction: discord.Interaction)
    interaction.channel.send_message("<text here>")
```
This is ofcorse something you will have to figure out yourself what would be best. Whenever in doubt, take a look at [the api reference](https://discordpy.readthedocs.io/en/latest/api.html).

---

### Slash Commands
> [Official Documentation](https://discord.com/developers/docs/interactions/application-commands)

*Code snippet*
```py
@client.tree.command(name="test", discription="does nothing")
async def test_command(interaction:discord.Interaction, type:str):
    #Add your code here
```
#### Explanation

```py
@client.tree.command(name="test", discription="does nothing")
```

The first line has a decorator that, *simply put*, triggers when a specific event is triggerd. Here it will trigger if a user sends "`/test`" in discord. The description will show up while the user hovers over the available commands.


```py
async def test_command(interaction:discord.Interaction, type:str):
```
The important part here is that whatever you call the parameters *(past `interaction:discord.Interaction`)* will impact what the user can input. I recommend you check the documentation for more info.
