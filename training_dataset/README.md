##### What should our final submitted  code achieve?  
Your submission must be able to detect the emotion of a conversation.

##### Can i use any existing speech processing libraries to do this?
You are free to use any open source speech processing libraries.

##### What kind of classification of sentiment are you talking about?
Your code would need to classify an audio file as “happy”, “unhappy”, “neutral” or “angry”.
     
##### What type of conversations are these?
These are telephonic conversations involving two people in most cases.

##### What languages are these conversations in?
These conversations are in English, Kannada, Tamil, Telugu or Hindi

##### Would a conversation have multiple languages?
Yes. Some of the conversations might be in multiple languages (from the ones mentioned above)

##### How is the training data structured?
There are a set of audio files classified as “happy”, “angry”, “neutral” and “unhappy”. All these audio files are conversations stored in mp3 format. These audio files are 8  kHz, Mono and are all recorded over the telephone. Some part of the conversations might be beeped out. We have tried to ensure these conversations cover all common patterns. The number of conversations in the training data for each emotion also denotes the probability of such conversations happening. For example the number of happy conversations are lesser in the training data is indicative of the lesser probability of happy conversations occurring when compared to others

##### Are these real conversations?
They are a mix of simulated and real life conversations used with permissions. The simulated conversations have been created to match real life scenarios. These conversations must be used only for the purpose of the hackathon.

##### What if a conversation has a neutral tone to most part, but has a angry tone only for a smaller part?  How do these conversations need to be classified?
Most human conversations mix multiple emotions, but have a dominant emotion. Take the case of customer call which would initially start out as a neutral conversation and move towards a angry, happy or unhappy tone. For the case you mention, the conversation must be classified as angry. Your code needs to classify the conversation with the dominant emotion. You might also come across conversations that are unhappy for most part, but angry for a smaller part. For such cases you should classify them as angry. As a thumb rule neutral < happy < unhappy < angry

##### Can I convert voice samples to text and detect emotion based on words used?
You are free to use whatever algorithm/methodology you think would work. But do keep in mind that the conversations are in different languages Indian languages

##### How would the submissions be evaluated?
Your code will be run against thousands of conversations and evaluated for the accuracy with which it detects emotions. The submissions which are most accurate make the cut.
