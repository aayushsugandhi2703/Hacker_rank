import java.util.*;
class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the size");
        int n = sc.nextInt();
        int arr[] = new int[n];
        System.out.println("Enter hte Elements");
        for(int i =0; i<n; i++){
            arr[i] = sc.nextInt();
        }
        int sum =0;
        int avg;
        for (int i=0; i<n; i++){
            sum = sum+arr[i];
        }
        avg = sum/n;
        System.out.println(sum);
    }
}