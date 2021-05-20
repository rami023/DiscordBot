import discord
import random
from discord.ext import commands
import discord.ext
import pymysql
import nest_asyncio

client=commands.Bot(command_prefix='.')
bot = discord.ext.commands.Bot(command_prefix = '-')
@client.event
async def  on_ready():
    print('Hola bro')

@client.event
async def on_member_join(member):
    await ctx.send(f'{member} Hola gordo, espero que no tengas covid.')



@client.command(aliases=['termometro','temp'])
async def temperatura(ctx):
    await ctx.channel.purge(limit=1)
    temperature_value=round(random.uniform(33,40),1)
    print(float(temperature_value))
    await ctx.send(f'Tomando la Temperatura... \nTemperatura:{temperature_value}')
    if float(temperature_value) > float(37.5):
        await ctx.send(f'TENES COVID\nTe vas derechito a la Zona en Cuarentena')
    elif float(temperature_value) < float(35.5):
        await ctx.send(f'Demasiado baja\nSeguramente tambien es Covid')
    else:
        await ctx.send(f'Estas en regla bro')



@client.command(aliases=['casino'])
async def apostar(ctx,value,apuesta):
    await ctx.channel.purge(limit=1)
    if str.upper(value) == 'CARA':
        await ctx.send(f'Salio Seca\nPerdiste ${apuesta}\nGil')
    elif str.upper(value) == 'SECA':
        await ctx.send(f'Salio Cara\nPerdiste ${apuesta}\nGil')
    else:
        await ctx.send(f'Escribiste mal\nIgual Perdiste ${apuesta}\nBobo')



@client.command(aliases=['sendnudes'])
async def sendpics(ctx):
    await ctx.channel.purge(limit=1)
    await ctx.send('https://static.wikia.nocookie.net/leagueoflegends/images/3/34/Manamune_item_HD.png/revision/latest/scale-to-width-down/64?cb=20201110233117')



@client.command(aliases=['rt'])
async def Randomtilt(ctx):
    await ctx.channel.purge(limit=1)
    a=['Uri','Rama','Marian','Topa','Santi','Mamut','Luca','Guido','Martin','Manuelo','Pancho','Mati','Nacho','Fer','Ale']
    b=random.choice(a)
    await ctx.send(b)
    
    
    
@client.command(aliases=['ht'])
async def historiatilt(ctx):
    await ctx.channel.purge(limit=1)
    a=['Uri','Rama','Marian','Topa','Santi','Mamut','Luca','Guido','Martin','Manuelo','Pancho','Matt','Nacho','Fer','Ale']
    b=random.choice(a)
    c=['Era una noche lluviosa cuando a','Estabamos en una ranked cuando a','Nos juntamos en lo de Topa cuando a','Considere violar la cuarentena cuando a','Estaba mirando los ultimos precios de reposeras en Mercadolibre cuando a','Me levante temprano para analizar el mercado cuando a','Estaba analizando el contexto geopolitico de JOJO cuando a']
    d=random.choice(c)
    e=['le pinto el autismo','le llego sono el telefono y se tiro todo el cafe encima','le pinto mandarse una ranked de TFT y cortarse solo','le choreo la billetera un indigente','le copo la idea de comerse un Mcflurry de porongas','se le ocurrio ir a autistear a la toplane','se motivo y se rompio un incenso','se acordo que era un chupapija','se puso a robarle pokemons a chicos discapacitados','no se le guardaron las runas y fue soraka con PTA']
    f=random.choice(e)
    g=(d+' '+b+' '+f)
    await ctx.send(str(g))
   
    

    
#Blacklist command main.
@client.command(aliases=['bl'])
# Connect to the database
async def blacklist(ctx,name):
    await ctx.channel.purge(limit=1)
#    global name, reason, elo, ab, bb, cb,lit
#    lit=name2.rsplit("-",4)
#    print(lit)
#    bb=' '
#    cb=' '
#    ab,bb,cb =lit
#    name= map(str, (lit)) 
    connection = pymysql.connect(host='localhost',
                             user='newuser',
                             password='password',
                             database='mynewdatabase',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
    cursor= connection.cursor();
    insert_query = """insert into firsttest(name) values('%s')""" \
        %(name);
        
    cursor.execute(insert_query);
    connection.commit();
    connection.close();
    await ctx.send(f'The database has been updated\nFuck you {name}')
    
    
#Blacklist complete command, consider disable it   
@client.command(aliases=['blb'])
# Connect to the database
async def blacklistb(ctx,name2):
    await ctx.channel.purge(limit=1)
    global name, reason, elo, ab, bb, cb,lit
    lit=name2.rsplit("-",2)
    print(lit)
    ab,bb,cb =lit
    name, reason, elo = map(str, (ab,bb,cb))
    connection = pymysql.connect(host='localhost',
                             user='newuser',
                             password='password',
                             database='mynewdatabase',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
    cursor= connection.cursor();
    insert_query = """insert into firsttest(name,reason,elo) values('%s','%s','%s')""" \
        %(name, reason, elo);
        
    cursor.execute(insert_query);
    connection.commit();
    connection.close();
    await ctx.send(f'The database has been updated, Shame on You {name}\n{name} was turbobanned from this server because he might be a {reason}\nGood luck getting out of {elo}')
    
    
# BLACKLIST SEARCH COMMAND   
@client.command(aliases=['bls'])
# Connect to the database
async def blsearch(ctx,name2):
    await ctx.channel.purge(limit=1)
    connection = pymysql.connect(host='localhost',
                             user='newuser',
                             password='password',
                             database='mynewdatabase',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
    cursor= connection.cursor();
    insert_query = "SELECT `id`, `name`, `reason`, `elo` FROM `firsttest` WHERE `name`=%s"
    cursor.execute(insert_query, (name2,))
    result = cursor.fetchone()
    await ctx.send(f'{result}')


#BRO MOMENT COMMAND
@client.command(aliases=['bro'])
# Connect to the database
async def bromoment(ctx,bro1, bro2):
    await ctx.channel.purge(limit=1)
    connection = pymysql.connect(host='localhost',
                             user='newuser',
                             password='password',
                             database='mynewdatabase',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
    cursor= connection.cursor();
    insert_query = """insert into bromoment(bro1,bro2) values('%s','%s')""" \
        %(bro1, bro2);
        
        
    cursor.execute(insert_query);
    connection.commit();
    connection.close();
    
    
    await ctx.send(f'BRO MOMENT ON THE WAY\n{bro1} and {bro2} finally agreed on something')
    await ctx.send('https://i.redd.it/ouqgvxuynqv61.png')

#arrow MOMENT COMMAND
@client.command(aliases=['arrow','skrm','fucku','fu','fuck'])
# Connect to the database
async def sk(ctx,arrows):
    await ctx.channel.purge(limit=1)
    connection = pymysql.connect(host='localhost',
                             user='newuser',
                             password='password',
                             database='mynewdatabase',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
    cursor= connection.cursor();
    insert_query = """insert into arrowmoment(arrows) values('%s')""" \
        %(arrows);
        
    cursor.execute(insert_query);
    connection.commit();
    cursor= connection.cursor();
    insert_query = "SELECT COUNT(`arrows`) FROM `arrowmoment` WHERE `arrows`=%s"
    cursor.execute(insert_query, (arrows,))
    result = cursor.fetchone()
#    await ctx.send(f'{result}')
#    print(type(result))
#    arrows_number = result.get('COUNT(name)')
#    arrows_number = [elem[0] for elem in result.values()]
    
    connection.close();
    s = result
    newstr = ''.join((ch if ch in '0123456789' else ' ') for ch in str(s))
    listOfNumbers = [int(i) for i in newstr.split()]
#    await ctx.send(str(listOfNumbers))
    
    
    await ctx.send(f'FUCK YOU MOMENT\n{arrows} took an arrow to the knee')
    await ctx.send('https://i.ibb.co/fxJ6hk5/Aatrox-to-the-knee.png')
    await ctx.send(f'{arrows} has taken {str(listOfNumbers)} arrows to the knee')
#    await ctx.send(f'{result}')
    
#Purge Command
@client.command(aliases=['purge','l'])    
async def limpiar(ctx, amount: int):
    await ctx.channel.purge(limit=1)
    await ctx.channel.purge(limit=amount)


@client.command(aliases=['d'])
async def daily(ctx):
    await ctx.send(f'Mimimi daily daily\nChupate una pija Maki')
    
    
    
nest_asyncio.apply()   
client.run('')
'''Credentials Removed'''
