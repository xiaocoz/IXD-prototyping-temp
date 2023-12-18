# The Empathy Pipe 
![Slide 16_9 - 2](https://github.com/xiaocoz/IXD-prototyping-temp/assets/137859417/b59d2381-00bb-4653-a589-db1fe8b9d252)

### Introduction
Our project is an exploration of the evolution of communication, starting from the basic string telephone to the modern digital era. We delved into the idea of transcending auditory communication by converting sound into visual representation. Initially, we were intrigued by the potential of using a light strip to visually express sound volumes captured by a microphone; this formed the foundation of our concept. As our research progressed, we found a profound connection between our concept and the theme of cyberbullying - a scenario where victims often face a barrage of silent yet echoing written abuse. We hypothesized that the principle of karma is relevant in such contexts, where the negative actions directed at others could eventually reverberate back to the abuser. Thus, we incorporated a dynamic visual effect using p5.js, which visually amplifies the spoken attacks by increasing the number and size of red dots projected onto the abuser, correlating with the volume of their speech.
![Slide 16_9 - 4](https://github.com/xiaocoz/IXD-prototyping-temp/assets/137859417/2f0f23f7-f561-4003-baec-0e2fb419e354)
![Slide 16_9 - 6](https://github.com/xiaocoz/IXD-prototyping-temp/assets/137859417/86d60768-ae29-4a6b-83fe-06e70b03dda2)


### Hardware
For our project, we utilized the following hardware components:

- AtomS3 Lite ESP32S3 Dev Kit: This development kit served as the brain of our project, processing the input from the microphone and controlling the LED strip's color changes.
- Microphone Unit (LM393): This sensor detected the sound levels, allowing us to translate volume into visual data.
- Digital RGB LED Weatherproof Strip SK6812: The LED strip provided visual feedback, changing colors based on the sound input to represent the varying intensities of cyberbullying.

### Firmware (MicroPython Code)
Running in the background via Thonny, our MicroPython firmware was crucial for interpreting the sound levels from the microphone and manipulating the LED strip's colors to create a gradient effect. The code continuously sampled the microphone's input and calculated an average volume, which was then used to adjust the LED colors, representing the harshness of spoken words.

