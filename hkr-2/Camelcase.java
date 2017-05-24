// Java 7
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Camelcase {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String s = in.nextLine();
        int g=1;
        for(int i=0; i < s.length(); i++){
                if(s.charAt(i)>64 && s.charAt(i)<91){
                    g+=1;
}
        }
            System.out.println(g);
    }
}
