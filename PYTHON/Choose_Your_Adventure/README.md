#### Making a Decision Tree  
We will learn some new concepts and harness some others of computer science and programming we have learned so far to create our own text adventure game! We first went over what a decision tree is and how to make one (catered to this project). We first took a look at an example decision tree.  

![whiteboard](images/text-advent.jpg)  

Students got started on making a diagram on paper to show the flow of their game; complete with a starting scenario and use of condition statements to make up decision branches stemming from the scenario (the trunk of the tree).  

The following is an excerpt taken from a [blog post](http://blog.techemstudios.com/hardcore-programming-camp-summer-2016.html) earlier this summer:  

### Choose Your Own Adventure  

#### Essentially Making a Decision Tree  

A "Decision Tree" is one of many ways to display an algorithm, a step-by-step process for reaching a result or solution to a problem. The first decision "branches" into two possibilities, each of which is another decision. By looking at the whole, it forms a tree, a decision tree! The procedural flow of traveling down the tree from the very first decision is nicely implemented with the Choose Your Adventure challenge camper completed using Python/Pythonista. You can compare this to a series of game books, Choose Your Own Adventure by [Edward Packard](https://en.wikipedia.org/wiki/Choose_Your_Own_Adventure) and the text adventure, [Zork](https://en.wikipedia.org/wiki/Zork) or tons of other written books where the reader commandeers the actions of the protagonist; leading to distinct endings.  

Students started their program by sketching on paper their ideas for their game's procedure flow to ultimately implement in their program. This challenge applies advanced branching logic and allows students to design their algorithm by literally drawing their program flow. The nodes in the tree are decision points -rooted in the very first decision. A first decision point could be, you land on Mars and you spot something in the distance. From here, you may have a few choices (or nodes) to choose from: Leave Mars, Go to Object, or Scan the Object. You can choose Go to Object, and you arrive at another decision point or node in the tree and the flow continues. Take a look at this example displayed on paper and translated into an interactive Python program. Try contrasting the decision tree on paper to the written program on python.  

![land on mars](images/hc-wray-example-mars.jpg)  

<script src="https://gist.github.com/wray/48cef3a6766ece0d8370.js"></script>[^4]  

This exercise replicates modeling decisions and their outcomes. These outcomes can also include chance event outcomes. Campers mapped out all the paths based on the decision made at each node.  

Decision trees are used in the real world all the time. Call Center Reps use these as print-outs or portrayed in apps. For example, tech hotlines, their script will start with "is the computer plugged in" and if the person answers yes, they take one route or if "no" they take another route. They follow the decision tree to help them assist the customer in troubleshooting problems.  

Another system that models a decision tree, identifying bugs. Really?? Yes. A dichotomous key, a tool used to identify something in the natural world is a great example to model decisions. Take a look at how a dichotomous key can be used by an Entomologist (someone who studies bugs; let's call him Steve) to identify something they collected from a stream.   

To use this key, Steve starts at the first decision point: is it something that has a shell or does not have a shell? This question knocks either With Shell or No Shell out of contention to be the thing's identity. If the condition is false, it is not a snail or clam, so Steve would then arrive at the next node: Does it Have a Backbone or No Backbone. If that condition is true, then he would arrive at another subnode, and his search continues for the bug's identity by following the outcome of each node until he arrives at its most likely identity and, ta-da, Steve knows the identity of the bug. If Steve was so inclined, he could look to another key to determine what Phylum, Class, Order, Family, Genus and finally species that bug belongs to. But, we'll save that story for later! Snapshot of a dichotomous key:  

![descision tree](images/decision-tree.jpg)  
[^2]  