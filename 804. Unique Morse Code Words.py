'''
Tag: String; Difficulty: Easy
International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, 
as follows: "a" maps to ".-", "b" maps to "-...", "c" maps to "-.-.", and so on.

For convenience, the full table for the 26 letters of the English alphabet is given below:

[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--",
"-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
Now, given a list of words, each word can be written as a concatenation of the Morse code of each letter. 
For example, "cba" can be written as "-.-..--...", (which is the concatenation "-.-." + "-..." + ".-"). 
We'll call such a concatenation, the transformation of a word.
Return the number of different transformations among all words we have.

Example:
Input: words = ["gin", "zen", "gig", "msg"]
Output: 2
Explanation: 
The transformation of each word is:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."

There are 2 different transformations, "--...-." and "--...--.".
Note:
The length of words will be at most 100.
Each words[i] will have length in range [1, 12].
words[i] will only consist of lowercase letters.
'''
class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse = [".-","-...","-.-.","-..",
                 ".","..-.","--.","....",
                 "..",".---","-.-",".-..",
                 "--","-.","---",".--.",
                 "--.-",".-.","...","-",
                 "..-","...-",".--","-..-",
                 "-.--","--.."]
        transformations = set()
        for word in words:
            transf = ""
            for c in word:
                transf = transf + morse[(ord(c) - ord('a'))]
            transformations.add(transf)
        return len(transformations)

'''
solution by myself
'''
class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        trans = set()
        moscode = ""
        words = ["gin", "zen", "gig", "msg"]
        dic = {"a":".-",
               "b":"-...",
               "c":"-.-.",
               "d":"-..",
               "e":".",
               "f":"..-.",
               "g":"--.",
               "h":"....",
               "i":"..",
               "j":".---",
               "k":"-.-",
               "l":".-..",
               "m":"--",
               "n":"-.",
               "o":"---",
               "p":".--.",
               "q":"--.-",
               "r":".-.",
               "s":"...",
               "t":"-",
               "u":"..-",
               "v":"...-",
               "w":".--",
               "x":"-..-",
               "y":"-.--",
               "z":"--.."}
        for i in words:
            #print(i)
            for m in i:
                #print(m)
                if m in dic:
                    moscode += dic[m]
                else:
                    return 0
                    #print(moscode)
            if moscode not in trans:
                trans.add(moscode)
            #print(trans)
            moscode = ""
        return(len(trans))
