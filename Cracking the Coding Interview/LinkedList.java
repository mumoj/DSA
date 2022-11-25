import java.util.*;

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

public class MyLinkedList{

    public MyLinkedList(int a){
        int size = 0;
        ArrayList<Interger> list = new ArrayList<Integer>();
        ListIterator<Interger> it = list.listIterator();
    }

    public int get(int index){
        if (index > this.list.size()-1  || index < 0 ){
            return -1;
        }

        if (index == this.it.previousIndex()){
            return this.it.previous();
        }
        else if (index < this.it.nextIndex()){
            while (this.it.hasPrevious()){
                int curr = this.it.previous();
                if(this.it.nextIndex() == index){
                    return curr;
                    break;
                }
            }
        }

        else{
            while(this.it.hasNext()){
                this.it.next();

                if(this.it.previousIndex() == index){
                    this.it.add(value);
                    break;
                }
            }

        }
    }
    public void addAtHead(int value){
        this.list.add(0, value); 
    } 
    public void addAtTail(int value){
        this.list.add(value);
    }

    public void addAtIndex(int index, int value){

        if (index > this.list.size()  || index < 0 ){
            throw ArrayIndexOutOfBoundsException;
        }
        
        if (index == this.it.nextIndex()){
            this.it.next();
            this.it.add(index, value);
        }
        else if (index < this.it.nextIndex()){
            while (this.it.hasPrevious()){
                this.it.previous();
                if( this.it.nextIndex() == index){
                    this.it.add(index, value);
                    break;
                }
            }
        }

        else{
            while(this.it.hasNext()){
                this.it.next();

                if (this.it.nextIndex() == this.list.size()){
                    this.list.add(value);
                    break;
                }

                if (this.it.nextIndex() == index){
                    this.it.add(index, value);
                    break;
                }
            }

        }

    }

    public void  deleteAtIndex(int index){

        if (index > this.list.size()-1  || index < 0 ){
            throw ArrayIndexOutOfBoundsException;
        }
        
        if (index == this.it.nextIndex()){
            int value = this.it.next();
            this.it.remove(value);
        }
        else if (index < this.it.nextIndex()){
            while (this.it.hasPrevious()){
                int value = this.it.previous();
                if( this.it.nextIndex() == index){
                    this.it.remove(value);
                    break;
                }
            }
        }

        else{
            while(this.it.hasNext()){
                int value = this.it.next();

                if(this.it.nextIndex() == index){
                    this.it.remove(value);
                    break;
                }
            }

        }
    }

}

class Main{

    public static void main(String[] args){
        LinkeldList linkedList = MyLinkedList();
        System.out.println(linkedListlist);

    }


}