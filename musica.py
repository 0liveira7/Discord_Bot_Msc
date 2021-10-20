import discord
from discord.channel import VoiceChannel
import youtube_dl
from discord.ext import commands
from discord.ext.commands import CommandNotFound


class music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="join", help="Comando para chamar o bot para o canal")
    async def join(self,ctx):
        if ctx.author.voice is None:
            await ctx.send("You're not in a voice channel!")
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await voice_channel.connect()
        else:
            await ctx.voice_client.move.to(voice_channel)

    @commands.command(name="disconnect", help="Comando para desconectar o bot do canal")
    async def disconnect(self,ctx):
            await ctx.voice_client.disconnect()

    @commands.command(name="play", help="Comando para dar play na música")
    async def play(self,ctx,url):
        ctx.voice_client.stop()
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        YDL_OPTIONS = {'format': "bestaudio"}
        vc = ctx.voice_client

        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info['formats'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(url2,**FFMPEG_OPTIONS)
            vc.play(source)


    @commands.command(name="pause", help="Comando para pausar a música")
    async def pause(self,ctx):
        await ctx.voice_client.pause()
        await ctx.send("Paused ")


    @commands.command(name="resume", help="Comando para continuar a música")
    async def resume(self,ctx):
        await ctx.voice_client.resume()
        await ctx.send("Resume ")


    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, CommandNotFound):
            await ctx.send("O comando não existe. Digite !help para ver todos os comandos")
        else:
            raise error





def setup(bot):
    bot.add_cog(music(bot))

