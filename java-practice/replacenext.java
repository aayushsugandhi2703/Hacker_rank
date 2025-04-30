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
        for (int i=0; i<n; i++){
            for (int j=i+1;j<n;j++){
                if (a[j]>a[i]){
                    a[i]=a[j];
                }
            }
        }
        a[n-1]=-1;
        for (int i=0; i<n;i++){
            System.out.print(a[i]);
        }
    }
}