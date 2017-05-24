//Java 7

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class 2DArray {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int arr[][] = new int[6][6];
        for(int arr_i=0; arr_i < 6; arr_i++){
            for(int arr_j=0; arr_j < 6; arr_j++){
                arr[arr_i][arr_j] = in.nextInt();
            }
        }

        int suma=-80;
        int ok=-80;
        int i=1;
        int j=1;
        while(i<5){
        while(j<5){
            suma = arr[i][j]+(arr[i-1][j]+arr[i-1][j-1]+arr[i-1][j+1])+(arr[i+1][j]+arr[i+1][j-1]+arr[i+1][j+1]);

            if(suma>ok){
                ok=suma;
            }
            j++;
        }
            j=1;
            i++;
        }
        System.out.println(ok);
    }
}
