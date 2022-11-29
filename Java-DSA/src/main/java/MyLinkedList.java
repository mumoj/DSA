import java.util.*;
import java.io.*;
// import java.util.ArrayList;
// import java.util.List;


// public class Node{
//     int a;
//     Node next;
//     Node prev;
//     public Node(int a, Node next, Node prev){
//         this.next = next;
//         this.prev = prev;
//         this.data = a;
//    }
// }

class Main {

    int size;
    ArrayList<Integer> list;
    ListIterator<Integer> iter;

    // public Main(){
    //     int size = 0;
    //     ArrayList<Integer> list = new ArrayList<Integer>();
    //     ListIterator<Integer> iter = list.listIterator();
    // }

    double get (int index, ArrayList<Integer> list,ListIterator<Integer> iter, int value){
        if (index > this.list.size()-1  || index < 0 ){
            return -1;
        }

        if (index == this.iter.previousIndex()){
            return this.iter.previous();
        }
        else if (index < this.iter.nextIndex()){
            while (this.iter.hasPrevious()){
                int curr = this.iter.previous();
                if(this.iter.nextIndex() == index){
                    return curr;
                }
            }
        }

        else{
            while(this.iter.hasNext()){
                this.iter.next();

                if(this.iter.previousIndex() == index){
                    this.iter.add(value);
                    break;
                }
            }

        }
    }
    void addAtHead(int value){
        this.list.add(0, value); 
    } 
    void addAtTail(int value){
        this.list.add(value);
    }

    void addAtIndex(int index, int value){

        if (index > this.list.size()  || index < 0 ){
            return;
        }
        
        if (index == this.iter.nextIndex()){
            this.iter.next();
            this.iter.add(value);
        }
        else if (index < this.iter.nextIndex()){
            while (this.iter.hasPrevious()){
                this.iter.previous();
                if( this.iter.nextIndex() == index){
                    this.iter.add(value);
                    break;
                }
            }
        }

        else{
            while(this.iter.hasNext()){
                this.iter.next();

                if (this.iter.nextIndex() == this.list.size()){
                    this.list.add(value);
                    break;
                }

                if (this.iter.nextIndex() == index){
                    this.iter.add(value);
                    break;
                }
            }

        }

    }

    void  deleteAtIndex(int index){

        if (index > this.list.size()-1  || index < 0 ){
            return;
        }
        
        if (index == this.iter.nextIndex()){
            int value = this.iter.next();
            this.iter.remove(value);
        }
        else if (index < this.iter.nextIndex()){
            while (this.iter.hasPrevious()){
                int value = this.iter.previous();
                if( this.iter.nextIndex() == index){
                    this.iter.remove(value);
                    break;
                }
            }
        }

        else{
            while(this.iter.hasNext()){
                int value = this.iter.next();

                if(this.iter.nextIndex() == index){
                    this.iter.remove(value);
                    break;
                }
            }

        }
    }

}

class MyLinkedList {

    public static void main(String[] args){
        Main list =  new Main();
        System.out.println(list.list);

    }


}