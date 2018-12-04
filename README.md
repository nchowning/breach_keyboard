# Breach Split Keyboard

This is a hobby project to create a keyboard that fits my needs. I figured why not share my progress.

## Firmware

On this, I took the lazy way out after finding an online firmware builder - [Keyboard Firmware Builder](http://kbfirmware.com/). This thing is awesome. You point it at a [keyboard-layout-editor.com](https://www.keyboard-layout-editor.com) layout, tweak the settings, then it spits out a compiled .hex file (or the [qmk](https://qmk.fm) source if you want). In this repo, I'm including the keyboard-layout-editor json file as well as the Keyboard Firmware Builder config json file. You can just upload that config & have Keyboard Firmware Builder deliver a hex file for you. In the future I might include the qmk source in this repo but I won't bother for now.

Since this keyboard uses a pro micro for each half, the firmware flashing process is a little bit different than if you'd used a teensy 2.0. I've added a reset tact switch so that you can easily program it. Just quickly hit the reset button twice & then fire off something like this:

```
avrdude -p atmega32u4 -P /dev/ttyACM0  -c avr109 -U flash:w:breach-left.hex
```

`/dev/ttyACM0` might be different on your machine so keep that in mind.
