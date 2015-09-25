# hack-the-talk-exotel
This is a skeleton repository indicating the directory structure for the code submission.

Refer to the challenge here - https://www.hackerearth.com/sprints/hack-the-talk/

### Rules for Submission

The submission must be in a tar.gz format. It should have a install.sh in the top directory that will take care of compilation and creating the executable. The final executable will be run as ./executable . The Input File will have a list of audio files like:

 - one.mp3
 - two.mp3
 - three.mp3
 - four.mp3... and So on.

These files one.mp3, two.mp3 etc will be files in the current directory. Your program would need to output the emotion detected for each file (one.mp3, two.mp3 etc) as happy, sad, angry, or neutral in separate lines:

happy  
sad  
neutral  
neutral  

The above output means one.mp3 was a "happy" conversation, two.mp3 was a "sad" conversation etc.


### Trainig dataset

This repo also contains the training data in training_dataset directoy.
