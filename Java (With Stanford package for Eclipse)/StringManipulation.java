import acm.program.*;
public class StringManipulation extends ConsoleProgram{
	public void run(){
		//Add commas to numeric string
		String line = readLine("Enter a numeric string: ");
		println(addCommas(line));
		//Delete Characters from String
		line = readLine("Enter a line (deleting): ");
		char character = readLine("Enter a character to be deleted: ").charAt(0);
		println(deleteCharacter(character, line));
		//Ceasar Cipher
		line = readLine("Enter your line here (ceasar cipher): ");
		println(ceasarCipher(line));
		//Count character in string
		line = readLine("Enter you line here (counting) : ");
		character = readLine("Enter a character to be counted: ").charAt(0);
		println(countChar(character, line));
		//Ceasar Cipher with input key
		line = readLine("Enter you line here (cipher 2) : ");
		int key = readInt("Enter an int for your key: ");
		println(ceasarCipher2(key, line));
		//Password
		line = readLine("Enter you line here (password) : ");
		println(password(line));
	}
	public String addCommas(String line) {
		String string = ""; 
		for(int i = 0; i < line.length(); i++) {
			if((i)%3==0 && i!=0) {
				string = "," + string;
			}
			string = line.charAt(line.length()-i-1) + string;
			
		}
		return string;
	}
	public String deleteCharacter(char character, String line) {
		String string = "";
		for(int i = 0; i < line.length(); i++) {
			if(line.charAt(i)!=character) {
				string = string + line.charAt(i);
			}
		}
		return string;
	}
	public String ceasarCipher(String line) {
		char temp;
		String newstring="";
		for(int i=0; i<line.length(); i++) {
			if(line.charAt(i)>='a' && line.charAt(i)<='z') {
				temp = (char) ((line.charAt(i)-'a'+1)%26+'a');
				newstring = newstring + temp;
			}
			else if(line.charAt(i)>='A' && line.charAt(i)<='Z') {
				temp = (char) ((line.charAt(i)-'A'+1)%26+'A');
				newstring = newstring + temp;
			}
			else newstring = newstring + line.charAt(i);
		}
		return newstring;
	}
	public String countChar(char character, String line) {
			int count = 0;
			for(int i =0; i < line.length(); i++) {
				if(line.charAt(i) == character) {
					count++;
				}
			}
			return character + " occurs " + count + " times.";
	}
	public String ceasarCipher2(int key, String line) {
		char temp;
		String newstring="";
		for(int i=0; i<line.length(); i++) {
			if(line.charAt(i)>='a' && line.charAt(i)<='z') {
				temp = (char) ((line.charAt(i)-'a'+key)%26+'a');
				newstring = newstring + temp;
			}
			else if(line.charAt(i)>='A' && line.charAt(i)<='Z') {
				temp = (char) ((line.charAt(i)-'A'+key)%26+'A');
				newstring = newstring + temp;
			}
			else newstring = newstring + line.charAt(i);
		}
		return newstring;
	}
	public String password(String line) {
		String password = "";
		for(int i =0; i < line.length(); i++) {
			if(line.charAt(i) == 'a') {
				password = password + "@";
			}
			else if(line.charAt(i) == 'e') {
				password = password + "3";
			}
			else if(line.charAt(i) == 's') {
				password = password + "5";
			}
			else {
				password = password + line.charAt(i);
			}
		}
		return password;
	}
}
