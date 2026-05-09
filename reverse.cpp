#include <iostream>
#include <fstream>
#include <string>

using namespace std;

void reverseString(string &);

int main () 
{
    ifstream inputFile;
    ofstream outputFile("text1.txt");
    inputFile.open("text.txt");

    if (!inputFile.is_open()) 
    {
        cout << "InputFile did not open!";
        return 1;
    }
    if (!outputFile.is_open()) 
    {
        cout << "OutputFile did not open!";
        return 1;
    }

    string word;
    while (inputFile >> word) 
    {
        reverseString(word);
        outputFile << word << endl;
    }

    inputFile.close();
    outputFile.close();
    return 0;
}

void reverseString(string & word) 
{
    string newWord;
    for (int i = 0; i < word.length(); i++) 
    {
        if (i >= word.length() - 1 - i)
            return;
        char temp = word[word.length() - 1 - i];
        word[word.length() - 1 - i] = word[i];
        word[i] = temp;
    }
}