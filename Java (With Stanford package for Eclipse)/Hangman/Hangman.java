/*
 * File: Hangman.java
 * ------------------
 * This program will eventually play the Hangman game from
 * Assignment #4.
 */

import acm.graphics.*;
import acm.program.*;
import acm.util.*;

import java.awt.*;
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Hangman extends ConsoleProgram {
	private char guess;
	private boolean bool;
	private int count = 8;
	private HangmanLexicon lex = new HangmanLexicon();
	private String key = chooseWord(lex);
	private String word = initiateWord();
	
	
    public void run() {
		/* You fill this in */
    	initialize();
	    while (count > 0 && word.indexOf('_') != -1) {	
	    	guess = prompt();
	    	bool = findInKey(guess);
	    	if(bool == true) {
	    		readLine("That guess is correct!");
	    	}
	    	else {
	    		readLine("There are no " + guess + "'s in the word.");
	    		count--;
	    	}
	    }
	    if(count == 0) readLine("You Lost.\nThe word was: " + key);
	    if (word.indexOf('_') == -1) readLine("You won!\nYou guessed the word: " + word);
	    
	    	
    	

    	
    	
    	
    	
    	
	}
    private String chooseWord(HangmanLexicon lex) {
    	RandomGenerator rgen = RandomGenerator.getInstance();
		int index = (int) (rgen.nextDouble(0,1) * lex.getWordCount()+1);
		return lex.getWord(index);
    }
    private void initialize() {
    	readLine("Welcome to Hangman!");
    	
    }
    private char prompt() {
    	return readLine("The word now looks like this: " + word + "\nYou have " + count + " guesses left." + "\nYour guess: ").toUpperCase().charAt(0);
    	
    	
    }
    private void printWord() {
    	for(int i = 0; i < word.length(); i++) System.out.print(word.charAt(i)+"_");
    	println();
    }
    private String initiateWord() {
    	String str = "";
    	for(int i =0; i < key.length(); i++) {
    		str += "_";
    	}
    	return str;
    }
    private boolean findInKey(char character) {
    	boolean inKey = false;
    	for(int i = 0; i < key.length(); i++) {
    		if(key.charAt(i) == character) {
    			word = word.substring(0,i) + character + word.substring(i+1);
    			inKey = true;
    		}
    	}
    	return inKey;
    }

}
