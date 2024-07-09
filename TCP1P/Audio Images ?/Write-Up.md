# Audio Images?

## Description:
Welcome to the future of explorer, where an image can output audio and audio can also output images. However, the future also has problems, so we hope you can help

The future has a special image about the developer of the future world which has special audio in it, but someone managed to hack the image and change the audio into a hidden message. Help us to track and get special messages from these hackers.

## Write-Up:
After obtaining the file, utilize [Cyberchief](https://gchq.github.io/CyberChef/) to extract its contents.

From the extracted data, a `.wav` file is identified.

Next, analyze the `spectrogram` of the `.wav` file to unveil its hidden content.

This process reveals the flag: `TCP1P{4nn0y1ng_f0r3ns1cs_1m4g3_4nd_4ud10!!!}`

This flag was discovered through detailed spectrogram analysis of the `.wav` file.