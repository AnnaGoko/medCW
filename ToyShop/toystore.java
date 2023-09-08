import java.io.*;
import java.util.*;

public class ToyStore {
    private List<Toy> toys;

    public ToyStore() {
        toys = new ArrayList<>();
    }

    public void addToy(Toy toy) {
        toys.add(toy);
    }

    public void removeToy(int index) {
        toys.remove(index);
    }

    public void updateWeight(int index, double weight) {
        toys.get(index).setWeight(weight);
    }

    public Toy getToy(int index) {
        return toys.get(index);
    }

    public List<Toy> getToys() {
        return toys;
    }

    public void saveToFile(String fileName) throws IOException {
        ObjectOutputStream outputStream = new ObjectOutputStream(new FileOutputStream(fileName));
        outputStream.writeObject(toys);
        outputStream.close();
    }

    public void loadFromFile(String fileName) throws IOException, ClassNotFoundException {
        ObjectInputStream inputStream = new ObjectInputStream(new FileInputStream(fileName));
        toys = (List<Toy>) inputStream.readObject();
        inputStream.close();
    }

    public Toy drawToy() {
        double totalWeight = 0;
        for (Toy toy : toys) {
            totalWeight += toy.getWeight();
        }
        double randomValue = Math.random() * totalWeight;
        double weightSum = 0;
        for (Toy toy : toys) {
            weightSum += toy.getWeight();
            if (randomValue <= weightSum) {
                if (toy.getQuantity() > 0) {
                    toy.setQuantity(toy.getQuantity() - 1);
                    return toy;
                } else {
                    return null;
                }
            }
        }
        return null;
    }
}