import java.util.*;
class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the size:");
        int n = sc.nextInt();
        int sum =0;
        for (int i=2; i<n;i++){
            boolean isprime=true;
            for (int j=2; j<=i/2;j++){
                if (i%j==0){
                    isprime=false;
                    break;
                }
            }
        if (isprime) {
            sum+=i;
        }
        }
        System.out.println(sum);
    }
}