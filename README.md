Holiday Chimes
==============

This project is a battery powered musical chime set, loosely inspired by the 
[Ye Merry Minstrel Caroling Christmas Bells](https://amzn.to/3rfPTJp)
we had as kids.  Built with a black walnut stand using copper tubing, 3d-printed hangers and controlled by an ESP32 running MicroPython.

Watch it playing "Silent Night" 
-------------------------------

Click [here](https://youtu.be/6GucSdeh5fI) or the image below.

[![Chimes playing 'Silent Night'"](http://img.youtube.com/vi/6GucSdeh5fI/0.jpg)](https://youtu.be/6GucSdeh5fI "Playing 'Silent Night'")

I chose to implement these 12 notes (which cover a decent number of songs), but it can be extended as needed (up to the free GPIO pins):

- C5, D, E, F, F#, G, A, B, C6, D, E, F

I mapped C5 (and like) to C4 in software since an actual C4 chime didn't really sound like C4 due to secondary frequencies.  [This guide](http://leehite.org/Chimes.htm#Note%20Selection) was very useful to understand what's going on.


Parts
-----
- [3/8" steel rod](https://www.homedepot.com/p/3-8-in-x-48-in-Plain-Steel-Round-Rod-801597/204273966)
- [#8 Nuts](https://www.homedepot.com/p/Everbilt-8-32-Zinc-Plated-Machine-Screw-Nut-100-Pack-800252/204273373)
- [1/2 in. x 10 ft. Copper Type M Pipe](https://www.homedepot.com/p/Cerro-1-2-in-x-10-ft-Copper-Type-M-Hard-Temper-Straight-Pipe-1-2-M-10/100354198)
- [Springs](https://amzn.to/3h4naSZ)
- [Wood beads](https://amzn.to/3h4RPQa)
- [5V regulator](https://amzn.to/37yTkTy)
- [Battery charger circuit](https://amzn.to/38i1DCt)
- [Motor drivers](https://amzn.to/2KKibus)
- [18650 batteries](https://amzn.to/3hba7iQ) (Amazon doesn't seem to sell these directly, but they have these "flashlights" packages. =)
- [Barrel jack power connector](https://amzn.to/3mAEZdm)
- [Charger](https://amzn.to/3r7OgNP)
- [Battery holders](https://amzn.to/37zQsGc)
- [Wooden dowels](https://amzn.to/2Kooy79)
- [Magnet wire](https://amzn.to/34u02sd)
- [OLED display](https://amzn.to/3rbWZP1)
- [Power switch](https://amzn.to/34rKfKe)
- [ESP-32 microcontroller](https://amzn.to/3mCeJzv)
- [Thread](https://amzn.to/3h3diJ4)
- Wood!

Tools I Used
------------
Use what you have around, this is just what I used.

- [Chisel set](https://amzn.to/3r7Otk5)
- [Pipe cutter](https://www.homedepot.com/p/Husky-5-8-in-Junior-Tube-Cutter-80-511-111/304384093)
- [Metal ruler](https://www.homedepot.com/p/Empire-36-in-Aluminum-Straight-Edge-Ruler-403/100185157) (for accuracy)
- [Mortiser](https://amzn.to/3pbRD4e) (Total overkill / recent present to myself - a drill press or hand tools will work as well.)
- [Table saw](https://www.homedepot.com/p/RIDGID-13-Amp-10-in-Professional-Cast-Iron-Table-Saw-R4520/309412843)
- [Miter saw](https://www.homedepot.com/p/RIDGID-15-Amp-Corded-12-in-Dual-Bevel-Sliding-Miter-Saw-with-70-Deg-Miter-Capacity-and-LED-Cut-Line-Indicator-R4222/306939244)
- [Tenoning Jig](https://www.grizzly.com/products/grizzly-tenoning-jig/h7583)
- [Disc sander](https://www.harborfreight.com/12-inch-direct-drive-bench-top-disc-sander-43468.html)
- [3D printer](https://amzn.to/37xKRjq)
- [Planer](https://amzn.to/3h0KYr0)
- [Center punch](https://amzn.to/2LRZKou)
- [Chamfer/Countersink Bit Set](https://amzn.to/3h1kUvV)
- [Sawmill](https://www.harborfreight.com/saw-mill-with-301cc-gas-engine-62366.html)


Build
-----
This took me somewhere between 40-80 hours to design, code and build, starting with a "mandatory fun day" event at work.

Get some wood.  This is some black walnut I slabbed a year or two ago:

![image](https://user-images.githubusercontent.com/2049665/102702249-96ff6b00-4215-11eb-849c-a9716fe64e0c.png)

Make sure it's big enough to fit everything:

![image](https://user-images.githubusercontent.com/2049665/102702250-a2eb2d00-4215-11eb-9040-bb3f6c20401c.png)

Cut and plane and do all the normal stuff to make it look pretty:

![image](https://user-images.githubusercontent.com/2049665/102702256-c2825580-4215-11eb-8120-5dce243a681c.png)
![image](https://user-images.githubusercontent.com/2049665/102702261-cd3cea80-4215-11eb-9d49-f5bffe7f8cb9.png)
![image](https://user-images.githubusercontent.com/2049665/102702264-d6c65280-4215-11eb-908a-e0dd0e920c2f.png)

Cut 12 copper tubes to length.  I found an excellent guide at http://leehite.org/Chimes.htm.  I bought two 
[10' sections of type M 1/2" copper pipe](https://www.homedepot.com/p/Cerro-1-2-in-x-10-ft-Copper-Type-M-Hard-Temper-Straight-Pipe-1-2-M-10/100354198)
and cut them accorting to [this guide](https://github.com/keredson/chimes/blob/main/Family%20Copper%20Type%20M%20Red.pdf).

![image](https://user-images.githubusercontent.com/2049665/102702271-e34aab00-4215-11eb-9d40-00a2437a84ce.png)
![image](https://user-images.githubusercontent.com/2049665/102702273-ecd41300-4215-11eb-8255-d61dbe1a16a2.png)

Drill and chamfer holes to hang them by at the hang points. 

![image](https://user-images.githubusercontent.com/2049665/102702281-fb222f00-4215-11eb-945c-c75a601db80f.png)
![image](https://user-images.githubusercontent.com/2049665/102702283-04ab9700-4216-11eb-9c3a-2b977c92734c.png)

Make the stand as you please.  I chose some pretty simple feet and through tenons.  

![image](https://user-images.githubusercontent.com/2049665/102702285-0f662c00-4216-11eb-8685-34240e227f43.png)
![image](https://user-images.githubusercontent.com/2049665/102702291-1a20c100-4216-11eb-9706-3aa75b4c06bd.png)
![image](https://user-images.githubusercontent.com/2049665/102702296-24db5600-4216-11eb-8f52-7c8bdf99a038.png)
![image](https://user-images.githubusercontent.com/2049665/102702298-2dcc2780-4216-11eb-87cd-e25b7ad3813a.png)

Make some electromagnets using 1.25" pieces of [3/8 in. Plain Steel Round Rod](https://www.homedepot.com/p/3-8-in-x-48-in-Plain-Steel-Round-Rod-801597/204273966).  3D print [end caps](https://github.com/keredson/chimes/blob/main/em_end.scad).

![image](https://user-images.githubusercontent.com/2049665/102702306-3ae91680-4216-11eb-9b23-7a1c36903ef4.png)
![image](https://user-images.githubusercontent.com/2049665/102702315-463c4200-4216-11eb-88c3-10a62acd6512.png)

Use a helper if available!

![image](https://user-images.githubusercontent.com/2049665/102700994-5567c380-4207-11eb-8e13-0ee3ea44d71e.png)
![image](https://user-images.githubusercontent.com/2049665/102702318-505e4080-4216-11eb-894d-95c9a2d9caae.png)

Make some recesses in the underside of your wood for 12 hanger modules:

![image](https://user-images.githubusercontent.com/2049665/102702324-59e7a880-4216-11eb-8714-84de8dd71748.png)

3D print [hangers](https://github.com/keredson/chimes/blob/main/striker_hanger.scad) and assemble:

![image](https://user-images.githubusercontent.com/2049665/102702326-623fe380-4216-11eb-99d8-1a630ce088e5.png)
![image](https://user-images.githubusercontent.com/2049665/102702328-6bc94b80-4216-11eb-818b-56ed46fceff5.png)
![image](https://user-images.githubusercontent.com/2049665/102702340-87345680-4216-11eb-9f3a-ff1f14fe876c.png)
![image](https://user-images.githubusercontent.com/2049665/102702350-97e4cc80-4216-11eb-9469-be85dcb31acf.png)

Dead bug solder up each electromagnet.

![image](https://user-images.githubusercontent.com/2049665/102702356-a16e3480-4216-11eb-90a5-15460b81e54b.png)

Space is tight, I used more of the magnet wire for signaling.

![image](https://user-images.githubusercontent.com/2049665/102702359-aaf79c80-4216-11eb-80d2-cf54ebd11f90.png)

Stainless screws for the capacitive buttons.  (Line them up better than I did!)

![image](https://user-images.githubusercontent.com/2049665/102702362-b3e86e00-4216-11eb-8903-960e62b0df63.png)

Use a nice power button:

![image](https://user-images.githubusercontent.com/2049665/102702368-bea30300-4216-11eb-8b7f-3339952a6eb4.png)

Batteries...

![image](https://user-images.githubusercontent.com/2049665/102701267-21da6880-420a-11eb-8d11-eb0b757a56b9.png)

Assemble:

![image](https://user-images.githubusercontent.com/2049665/102702371-ca8ec500-4216-11eb-8448-fd507ae952f6.png)
![image](https://user-images.githubusercontent.com/2049665/102702377-d37f9680-4216-11eb-9fe2-da9f9a839ddd.png)
![image](https://user-images.githubusercontent.com/2049665/102702380-dbd7d180-4216-11eb-8e5e-46ed8a79a9d6.png)

OLED screen and [holder](https://github.com/keredson/chimes/blob/main/screen.scad):

![image](https://user-images.githubusercontent.com/2049665/102702385-e98d5700-4216-11eb-8b67-769d342b1fc0.png)

Finish with Danish Oil.

![image](https://user-images.githubusercontent.com/2049665/102702387-f0b46500-4216-11eb-80f0-575639b15f3c.png)

Software
--------

The software uses regular MIDI files I whittled down in [LMMS](https://lmms.io/) to simple melodies.  I used a version of [Mido](https://github.com/mido/mido) I stripped down for memory reasons.  The ESP-32 runs [MicroPython](https://micropython.org/).

The main code is in [main.py](https://github.com/keredson/chimes/blob/main/main.py).  It's MVP (but not much more).

