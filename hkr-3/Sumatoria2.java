//Java

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Sumatoria2 {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int arr[][] = new int[n][n];
        int resu[] = new int[n];
        for(int i=0; i < n; i++){
            for(int j=0; j < n; j++){
                arr[i][j] = in.nextInt();
            }
        }
      for(int i=0; i < n; i++){
            for(int j=0; j < n; j++){
                resu[i] += arr[j][i];
    }
}
    for(int i=0; i<n;i++){
        System.out.print(resu[i]+" ");

    }
        System.out.println(' ');
    }
}
