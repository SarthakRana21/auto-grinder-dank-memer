# auto-grinder-dank-memer
use this python script to auto send commands in dank memer bot 

install `python3` and `multiprocessing library`

**How to get your authorization token?**

1. open discord and go to the channel where you want to grind
2. then if in `windows` press `ctrl+shift+i` and if in `osx` select any text within the channel and use `secondary click` to open `inspect element`
3. then on the top bar you will notice `'elements 'console' 'source' 'network'`, click on `network` 
4. send a message into that channel and you will notice `messages` under `name` column in inspect element 
<img width="1075" alt="Screenshot 2022-06-28 at 7 06 48 PM" src="https://user-images.githubusercontent.com/107024368/176193032-9c3d4dd4-cbdb-4cd9-9707-3bd9c1411ccf.png">

5. click on `messages`
6. scroll down to `request headers` , under accept language you will se `authorization: MNJzNzMwNTEzOT54UzODsdffysdfgyMTEz.G19sdfqaF.hz5fxvque3RUl_tWde3IdfdVENd9_oqw9jUsqyFJHN` "some thing like that" 
<img width="1075" alt="Screenshot 2022-06-28 at 7 10 04 PM" src="https://user-images.githubusercontent.com/107024368/176193716-af5f8486-4a53-4c66-a38f-148c1d07b92a.png">

7. copy and paste it into authorization section in between single quotes in all defined classes 'def beg' 'def hunt' 'def fish' 'def dig'

**How to get your request.post url?**
1. navigate back to the networks section in inspect element of the channel where you want to grind 
2. check `general` section 
3. copy `Request URL:` and paste it in `request.post` in between single quotes in all defined classes 'def beg' 'def hunt' 'def fish' 'def dig'.
<img width="1075" alt="Screenshot 2022-06-28 at 7 12 47 PM" src="https://user-images.githubusercontent.com/107024368/176194219-74413c94-72fa-41c5-8fe7-64421642dc6c.png">



