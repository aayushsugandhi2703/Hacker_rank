import java.util.*;
class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the size");
        int n = sc.nextInt();
        int a[] = new int[n];
        System.out.println("Enter hte Elements");
        for(int i =0; i<n; i++){
            a[i] = sc.nextInt();
        }
        int temp;
        temp= a[0];
        a[0] =a[n-1];
        a[n-1] = temp;
        for(int i =0; i<n;i++){
            System.out.println(a[i]);
        }
    }
}