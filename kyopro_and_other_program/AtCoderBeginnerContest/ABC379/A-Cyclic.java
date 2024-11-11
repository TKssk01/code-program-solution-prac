import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // 入力の読み込み
        int N = sc.nextInt();
        
        int a = N / 100;
        int b = (N % 100) / 10;
        int c = N % 10;
        // System.out.println(a);
        // System.out.println(b);
        // System.out.println(c);

        int M1 = b*100 + c*10 + a;
        int M2 = c*100 + a*10 + b;

        System.out.println(M1 +" "+ M2);
        
        
        // 結果の出力
        // System.out.println(result);
    }
}