// Java 7
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Cesarcipher {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        String a = in.next(), solo="";
        int k = in.nextInt();
        for(int i=0; i < a.length(); i++){
            int p =(a.charAt(i)+(k%26));
            if(a.charAt(i)>=65 && a.charAt(i)<=90 || a.charAt(i)>=97 && a.charAt(i)<=122){
                if(p>=65 && p<=90 && a.charAt(i)>=65 && a.charAt(i)<=90){

                    System.out.print((char)(p));
                }
              else if(a.charAt(i)>=97 && a.charAt(i)<=122 && p>=97 && p<=122){
                    System.out.print((char)(p));
                }
                else{
                  if(a.charAt(i)>=65 && a.charAt(i)<=90 && p>90){

                      System.out.print((char)(64 + p%90));
                  }
                 else{

                     System.out.print((char)(96 + p%122));
                     }
                 }
                }
            else{

                System.out.print((char)(a.charAt(i)));
        }
    }

        }

    }
