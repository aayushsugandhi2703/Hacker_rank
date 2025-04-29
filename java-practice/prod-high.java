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
        int max=Integer.MIN_VALUE;
        int smax= Integer.MIN_VALUE;
        for(int i=0; i<n; i++){
            if (a[i]>max){
                smax= max;
                max = a[i];
            }
            else if (a[i]>smax && a[i] != max){
                smax=a[i];
            }
        }
        int prod= max*smax;
        System.out.print(prod);
    }
}