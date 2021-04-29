# Motorola QuikCall II Python

Some tinkering to detect QuikCall II tones sent via radio. I use a RTL-SDR receiver hooked to GQRX and send the audio via a virtual interface to `detect_tones.py`. I wrote some A/B QuikCall II tones in a dictionary, with their corresponding frequencies. You might want to set these according to your needs. 

The result will be sent via Discord, to a Discord-Webhook previuosly defined.

I made this as a pager project for firefighters, but I think you can find many applications (like remote controling something with a Motorola Radio). It simply gets the loudest frequency of a signal and then finds the corresponding tone. If the A tone is heard (150 in this case), it "opens the squelch" and starts listening for the B tone 151 to 160 in this case.